from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from app.models import AppStore
from exhibitor_app.models import *
from executive_app.models import *
# Create your views here.




def landing_page(request):
    return render(request,'Landing_page.html')

def admin_login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['Adm_id'] = user.id
            return redirect('admin_user/admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'INVALID CREDENTIALS'})
    return render(request,'admin_login.html')

def register(request):
    eve = Events.objects.all()
    return render(request,'register.html',{'eve':eve})


def exhibitor_login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
    
        if Exhibitors.objects.filter( username=username, password=password).exists():
            user = Exhibitors.objects.get(username = request.POST['username'],password = request.POST['password'])
            request.session['EUser_id'] = user.id
            return redirect('exhibitor_app/exhibitor_scanner')
        else:
            return render(request, 'exhibitor_login.html', {'error': 'INVALID CREDENTIALS'})
    return render(request,'exhibitor_login.html')



def executive_login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        print(username,password)
    
        if Executives.objects.filter( username=username, password=password).exists():
            user = Executives.objects.get(username = request.POST['username'],password = request.POST['password'])
            request.session['ExUser_id'] = user.id
            return redirect('executive_app/executive_scanner')
        else:
            return render(request, 'executive_login.html', {'error': 'INVALID CREDENTIALS'})
    return render(request,'executive_login.html')
















# def emailsent(request):
#     # Email configuration
#     sender_email = "anwarsadik.disk1@gmail.com"
#     receiver_email = "anwar.se6285@gmail.com"
#     password = "ogxemcnlxvvbflhx"
#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587  #

#      # Email content
#     subject = "Event Entry Pass"

#     html_file_path = os.path.join(os.path.dirname(__file__), "/Users/macair/Desktop/SilverHost/GCCExhibition/GCCExhibition/templates/email_template.html")
#     with open(html_file_path, "r", encoding="utf-8") as file:
#         html_content = file.read()
#         # Create the email message
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject

#         # Attach the HTML content to the email
#     html_part = MIMEText(html_content, "html")
#     message.attach(html_part)

#     with open(finders.find('logo/bookbadge.png'), 'rb') as f:
#         bookbadge = f.read()

#         # Attach the images
#     bookbadge = MIMEImage(bookbadge, 'png')
#     # tickMime = MIMEImage(tick, 'png')
#     bookbadge.add_header('Content-ID', '<bookbadge>')
#     # logoMime.add_header('Content-ID', '<logoMime>')
#     # message.attach(logoMime)
#     message.attach(bookbadge)
    

#     try:
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()  # For secure connections
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message.as_string())
#         server.quit()
#         print("Email sent successfully!")
#         return HttpResponse("Email sent successfully!")
#     except smtplib.SMTPException as e:
#         print("Error: Unable to send the email.")
#         print(e)
#         return HttpResponse("Error: Unable to send the email.")



    
def appstore(request):
    app = AppStore.objects.all()
    return render(request,'AppStore.html',{'app':app})
