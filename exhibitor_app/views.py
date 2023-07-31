from django.shortcuts import render,redirect
from exhibitor_app.models import *
from student_app.models import *
from django.http import JsonResponse
from datetime import datetime

# Create your views here.
def exhibitor_navbar(request):
    if 'EUser_id' in request.session:
        if request.session.has_key('EUser_id'):
            EUser_id = request.session['EUser_id']
        else:
            return redirect('/')
        EUser = Exhibitors.objects.filter(id=EUser_id)
        
        return render(request,'Exhibitor/exhibitor_navbar.html',{'EUser':EUser})
    else:
        return redirect('/as_Exhibitor')

def exhibitor_dashboard(request):
    if 'EUser_id' in request.session:
        if request.session.has_key('EUser_id'):
            EUser_id = request.session['EUser_id']
        else:
            return redirect('/')
        EUser = Exhibitors.objects.filter(id=EUser_id)

        boothvisitorss = BoothVisitors.objects.filter(Booth = EUser_id)
        EUser__id = Exhibitors.objects.get(id=EUser_id)
        total_reg = Student_Registration.objects.all().count()
        total_std = Student_Registration.objects.filter(who = 'Student').filter(event = EUser__id.event).count()
        total_par = Student_Registration.objects.filter(who = 'Parent').filter(event = EUser__id.event).count()
        total_aca = Student_Registration.objects.filter(who = 'Academic').filter(event = EUser__id.event).count()
        total_school = Student_Registration.objects.filter(status = 'school').filter(event = EUser__id.event).count()
        return render(request,'Exhibitor/exhibitor_dashboard.html',{'EUser':EUser,'boothvisitorss':boothvisitorss,'total_reg':total_reg,'total_std':total_std,'total_par':total_par,'total_aca':total_aca,'total_school':total_school})
    else:
        return redirect('/as_Exhibitor')
    
def exhibitor_scanner(request):
    if 'EUser_id' in request.session:
        if request.session.has_key('EUser_id'):
            EUser_id = request.session['EUser_id']
        else:
            return redirect('/')
        EUser = Exhibitors.objects.filter(id=EUser_id)
        return render(request,'Exhibitor/exhibitor_scanner.html',{'EUser':EUser})
    else:
        return redirect('/as_Exhibitor')
    
def exhibitor_settings(request):
    if 'EUser_id' in request.session:
        if request.session.has_key('EUser_id'):
            EUser_id = request.session['EUser_id']
        else:
            return redirect('/')
        EUser = Exhibitors.objects.filter(id=EUser_id)
        return render(request,'Exhibitor/exhibitor_settings.html',{'EUser':EUser})
    else:
        return redirect('/as_Exhibitor')


def boothvisitor_qrscan(request):
    if request.method == 'POST':
        QrCode = request.POST.get('QrCode')
        exeid = request.POST.get('ExeID')
        boothis = Exhibitors.objects.get(id=exeid)
        details = Student_Registration.objects.get(booking_ID=QrCode)

        if Student_Registration.objects.filter(booking_ID=QrCode).exists():
            if BoothVisitors.objects.filter(booking_ID=QrCode).filter(Booth=exeid).exists():
                response_data = {'status': 'exist'}
                return JsonResponse(response_data)
            else:
                if boothis.event.id == details.event.id :
                    visitorname = details.fullname
                    bv = BoothVisitors()
                    bv.Booth = boothis
                    bv.visitor = details
                    bv.booking_ID = QrCode
                    bv.visited_DT = datetime.today()
                    bv.status = '1'
                    bv.save()
                    response_data = {'status': 'success','visitorname':visitorname}
                    return JsonResponse(response_data)
                else:
                    response_data = {'status': 'eventerror'}
                    return JsonResponse(response_data)
        else:
            response_data = {'status': 'error', 'message': 'Invalid or missing doc_number.'}
            return JsonResponse(response_data) 


def exhibitor_logout(request):
    if 'EUser_id' in request.session:
        request.session.flush()
    return redirect('/as_Exhibitor')