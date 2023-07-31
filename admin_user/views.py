from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from student_app.models import *
from admin_user.models import *
from datetime import datetime
from exhibitor_app.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from executive_app.models import *




# Create your views here.
def admin_navbar(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        
        return render(request, 'admin/admin_navbar.html', {'admin': admin})
    else:
        return redirect('/')

def admin_dashboard(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        regs = Student_Registration.objects.all().count()
        events = Events.objects.all().count()
        execut = Executives.objects.all().count()
        exhib = Exhibitors.objects.all().count()

        today = datetime.today()
        upcoming_events = Events.objects.filter(from_date__gt=today)
        upcoming_events = upcoming_events.order_by('from_date')
        if upcoming_events.exists():
            latest_event = upcoming_events.first()
            latest_studen = Student_Registration.objects.filter(event = latest_event.id).count()
            latest_exhi = Exhibitors.objects.filter(event = latest_event.id).count()
            latest_exec = Executives.objects.filter(event = latest_event.id).count()
            return render(request, 'admin/admin_dashboard.html', {'admin': admin,'regs':regs,'events':events,'execut':execut,'exhib':exhib,'latest_event':latest_event,'latest_studen':latest_studen,'latest_exhi':latest_exhi,'latest_exec':latest_exec})
        else:
            print("No upcoming events found.")

        return render(request, 'admin/admin_dashboard.html', {'admin': admin,'regs':regs,'events':events,'execut':execut,'exhib':exhib,'latest_event':latest_event})
    else:
        return redirect('/')

def admin_register_view(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        regs  =Student_Registration.objects.all()
        return render(request, 'admin/admin_register_view.html', {'admin': admin,'regs':regs})
    else:
        return redirect('/')


def remove_regs(request,id):
    reg = Student_Registration.objects.get(id=id)
    reg.delete()
    return redirect(admin_register_view)


def admin_events(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        event = Events.objects.all()
        if request.method == 'POST':
            eventname = request.POST["event-name"]
            datefrom = request.POST['event-date-from']
            dateto = request.POST['event-date-to']
            timeform = request.POST['event-time-from']
            timeto = request.POST['event-time-to']
            location = request.POST['event-location']
            e = Events()
            e.event = eventname
            e.from_date = datefrom
            e.to_date = dateto
            e.from_time = timeform
            e.to_time = timeto
            e.location = location
            e.status = '0'
            e.created_at = datetime.today()
            e.save()

            return redirect (admin_events)
        return render(request, 'admin/admin_events.html', {'admin': admin,'event':event})
    else:
        return redirect('/')

def edit_event(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        event = Events.objects.get(id=id)
        if request.method == 'POST':
            eventname = request.POST["event-name"]
            datefrom = request.POST['event-date-from']
            dateto = request.POST['event-date-to']
            timeform = request.POST['event-time-from']
            timeto = request.POST['event-time-to']
            location = request.POST['event-location']

            event = Events.objects.get(id=id)
            event.event = eventname
            event.from_date = datefrom
            event.to_date = dateto
            event.from_time = timeform
            event.to_time = timeto
            event.location = location
            event.status = '0'
            event.created_at = datetime.today()
            event.save()

            return redirect (admin_events)

        return render(request, 'admin/admin_edit-events.html', {'admin': admin,'event':event})
    else:
        return redirect('/')

def delete_event(request,id):
    event = Events.objects.get(id=id)
    event.delete()
    return redirect(admin_events)


def admin_exhibitors(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        eve = Events.objects.all()
        exe = Exhibitors.objects.all()
        try:
            latest_exhibitor = Exhibitors.objects.latest('id')
            last_id = latest_exhibitor.id + 1
        except:
            last_id = 1

        if request.method == 'POST':
            event = request.POST["event"]
            exhibitors = request.POST['exhibitors']
            bno = request.POST['btno']
            cperson = request.POST['c_person']
            cemail = request.POST['c_email']
            c_number = request.POST['c_number']
            c_username = request.POST['c_username']
            c_pass = request.POST['c_pass']

            eve = Events.objects.get(id=event)
            exe = Exhibitors()
            exe.event = eve
            exe.exhibitors = exhibitors
            exe.boothnumber = bno
            exe.contactperson = cperson
            exe.contactemail = cemail
            exe.contactnumber = c_number
            exe.username = c_username
            exe.password = c_pass
            exe.save()

            current_url = f"{request.scheme}://{request.META['HTTP_HOST']}/"
            applinks = current_url+'AppStore/'
            weblinks = current_url+'as_Exhibitor'


            sender_email = 'emailserveratsh@gmail.com'
            receiver_email = cemail
            password = 'ftxmwatzwkpadzpz'

            subject = 'Approval Granted: Inclusion of Booth in '+(eve.event)+' Program + App Details'
            message = 'Dear '+exhibitors
            message += '\nI hope this email finds you well. We are delighted to inform you that your request to add a booth to the '+(eve.event)+' program has been approved! \n We believe your presence will add significant value to the event, and we are excited to have you as part of our esteemed exhibitor lineup.\n'
            message += '\nDetails  :\nUsername : '+c_username+' \n Password : '+c_pass+'\n\n WebLink :'+weblinks+'\n\n App Link :'+applinks 
            message += '\n\nPlease use the provided link to download the app onto your device. It will enable you to scan APK URLs and original web app links effortlessly during the event.\n Your exhibitor credentials will be required to log in securely.'
            message += '\nIf you encounter any concerns or have questions regarding the app`s security, please feel free to reach out to our support team.'
            message += '\nWe look forward to your participation and wish you a successful exhibition!'
            message += '\n\nBest regards,'
            message += '\nGCCEXHIBITION Team'


            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                text = msg.as_string()
                server.sendmail(sender_email, receiver_email, text)
                print('Email sent successfully!')
            except Exception as e:
                print(f'An error occurred while sending the email: {str(e)}')
            finally:
                server.quit()
            return redirect(admin_exhibitors)

        return render(request, 'admin/admin_exhibitors.html', {'admin': admin,'eve':eve,'last_id':last_id,'exe':exe})
    else:
        return redirect('/')


def admin_view_exhibitors(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        exe = Exhibitors.objects.filter(id=id)
    
        total_reg = Student_Registration.objects.all().count()
        total_std = Student_Registration.objects.filter(who = 'Student').count()
        total_par = Student_Registration.objects.filter(who = 'Parent').count()
        total_aca = Student_Registration.objects.filter(who = 'Acadmic').count()
        total_school = Student_Registration.objects.filter(status = 'school').count()

        
        return render(request, 'admin/admin_view_exhibitors.html', {'admin': admin,'exe':exe,'total_reg':total_reg,'total_std':total_std,'total_par':total_par,'total_aca':total_aca,'total_school':total_school})
    else:
        return redirect('/')



def Update_admin_exhibitors(request,id):
    exe = Exhibitors.objects.get(id=id)
    if request.method == 'POST':
        event = request.POST["events"]
        print(event)
        exhibitors = request.POST['exhibitors']
        bno = request.POST['btno']
        cperson = request.POST['c_person']
        cemail = request.POST['c_email']
        c_number = request.POST['c_number']

        eve = Events.objects.get(id=event)
        exe.event = eve
        exe.exhibitors = exhibitors
        exe.boothnumber = bno
        exe.contactperson = cperson
        exe.contactemail = cemail
        exe.contactnumber = c_number

        exe.save()
    return redirect(admin_exhibitors)

def delete_Exhibitors(request,id):
    exe = Exhibitors.objects.get(id=id)
    exe.delete()
    return redirect(admin_exhibitors)

def admin_executives(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
       
        exess = Executives.objects.all()
        eve = Events.objects.all()
        return render(request, 'admin/admin_executives.html', {'admin': admin,'eve':eve,'exess':exess})
    else:
        return redirect('/')

def saveExecutive(request):
    if request.method == 'POST':
        eventid = request.POST["events"]
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        phone = request.POST["phone"]

        eve = Events.objects.get(id=eventid)
        execut = Executives()
        execut.event = eve
        execut.fullname = fullname
        execut.email = email
        execut.phone = phone
        execut.save()

        execut.username = "EXEGCC@" + \
                    str(execut.id).zfill(3)
        execut.password = 'GCC@'+\
                    str(execut.id).zfill(3)
        execut.save()
    return redirect(admin_executives)

def deleteExecutive(request,id):
    execu = Executives.objects.get(id=id)
    execu.delete()
    return redirect(admin_executives)

