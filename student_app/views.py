from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
import random
import qrcode
from student_app.models import *
from django.conf import settings
import os
from io import BytesIO
from django.core.files.base import ContentFile

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from django.http import HttpResponse
from django.contrib.staticfiles import finders
from django.template import loader,Engine



# Create your views here.

def registration_save(request):
    if request.method == 'POST':

        whichform = request.POST['whichform']

        full_name = request.POST['s_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        event = request.POST['event']
        eve = Events.objects.get(id=event)
        

        date=datetime.today()

        if whichform == '0':
            dob = request.POST['dob']
            country = request.POST['country']
            nation = request.POST['nation']
            who = request.POST['membershipRadios']
            school = request.POST['school']
            quali = request.POST['quali']
            studyabroad = request.POST['membershipRadios1']
            intrest = request.POST['intrest']
            others = request.POST['others']


            sr = Student_Registration()
            sr.fullname = full_name
            sr.email = email
            sr.mobile = mobile
            sr.dob = dob
            sr.country = country
            sr.nationality = nation
            sr.who = who
            sr.school = school
            sr.qualification = quali
            sr.study_abroad = studyabroad
            sr.interest = intrest
            sr.others = others
            sr.event = eve
            sr.register_DT = date
            sr.status = 'student'
            sr.save()

            #booking id
            myid = str(sr.id)
            first_letter = full_name[0].capitalize()
            codeis = f"{myid:0>5}"
            count_zeros = codeis.index(myid)
            random_letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=count_zeros))
            generated_code = f"{first_letter}GCC{random_letters}{myid}"
            sr.booking_ID  = generated_code
            sr.save()

            #qrcodegenerate
            qr = qrcode.QRCode(
                version=2,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=2,
            )
            qr.add_data(generated_code)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            filename = f"{generated_code}_qrcode.png"
            file_path = os.path.join(settings.MEDIA_ROOT, "qrcodes", filename)
            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)
            content_file = ContentFile(buffer.read())
            sr.QR.save(filename, content_file)
            sr.save()




            # Email configuration
            sender_email = "anwarsadik.disk1@gmail.com"
            receiver_email = email
            password = "ogxemcnlxvvbflhx"
            smtp_server = "smtp.gmail.com"
            smtp_port = 587  #

            # Email content
            subject = "Event Entry Pass"


            # html_file_path = os.path.join(os.path.dirname(__file__), "./")
            parent_directory = os.path.dirname(os.path.dirname(__file__))
            print(parent_directory)

            # Append the desired file name to the parent directory path
            html_file_path = os.path.join(parent_directory, "templates/email_template.html")

            with open(html_file_path, "r", encoding="utf-8") as file:
                html_content = file.read()


            html_content = html_content.replace("{name}", full_name)
            html_content = html_content.replace("{code}", generated_code)
            html_content = html_content.replace("{event}", eve.event)

            # Create the email message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject

                # Attach the HTML content to the email
            html_part = MIMEText(html_content, "html")
            message.attach(html_part)

            with open(finders.find('logo/bookbadge.png'), 'rb') as f:
                bookbadge = f.read()
            qr_file_path = os.path.join(settings.MEDIA_ROOT, "qrcodes", filename)
            with open(qr_file_path, 'rb') as f:
                QRcode = f.read()

            # Attach the images
            bookbadge = MIMEImage(bookbadge, 'png')
            QRcode = MIMEImage(QRcode, 'png')
            bookbadge.add_header('Content-ID', '<bookbadge>')
            QRcode.add_header('Content-ID', '<QRcode>')
            message.attach(QRcode)
            message.attach(bookbadge)

        
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls() 
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                server.quit()
                print("Email sent successfully!")
                return redirect('/')
            except smtplib.SMTPException as e:
                error_message = 'Invalid credentials. Please try again.'
                return render(request, 'register.html', {'error_message': error_message})

        else :
            address = request.POST['address']
            schoolid = request.POST['schoolid']

            sr = Student_Registration()
            sr.fullname = full_name
            sr.email = email
            sr.mobile = mobile
            sr.address = address
            sr.school_ID = schoolid
            sr.status = 'school'
            sr.event = eve
            sr.register_DT = date
            sr.save()

            #booking id
            myid = str(sr.id)
            first_letter = full_name[0].capitalize()
            codeis = f"{myid:0>5}"
            count_zeros = codeis.index(myid)
            random_letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=count_zeros))
            generated_code = f"{first_letter}GCC{random_letters}{myid}"
            sr.booking_ID  = generated_code
            sr.save()

            #qrcodegenerate
            qr = qrcode.QRCode(
                version=2,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=2,
            )
            qr.add_data(generated_code)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            filename = f"{generated_code}_qrcode.png"
            file_path = os.path.join(settings.MEDIA_ROOT, "qrcodes", filename)
            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)
            content_file = ContentFile(buffer.read())
            sr.QR.save(filename, content_file)
            sr.save()


            # Email configuration
            sender_email = "anwarsadik.disk1@gmail.com"
            receiver_email = email
            password = "ogxemcnlxvvbflhx"
            smtp_server = "smtp.gmail.com"
            smtp_port = 587  #

            # Email content
            subject = "Event Entry Pass"


            # html_file_path = os.path.join(os.path.dirname(__file__), "./")
            parent_directory = os.path.dirname(os.path.dirname(__file__))
            html_file_path = os.path.join(parent_directory, "templates/email_template.html")

            with open(html_file_path, "r", encoding="utf-8") as file:
                html_content = file.read()


            html_content = html_content.replace("{name}", full_name)
            html_content = html_content.replace("{code}", generated_code)
            html_content = html_content.replace("{event}", eve.event)

            # Create the email message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject

                # Attach the HTML content to the email
            html_part = MIMEText(html_content, "html")
            message.attach(html_part)

            with open(finders.find('logo/bookbadge.png'), 'rb') as f:
                bookbadge = f.read()
            qr_file_path = os.path.join(settings.MEDIA_ROOT, "qrcodes", filename)
            with open(qr_file_path, 'rb') as f:
                    QRcode = f.read()

            # Attach the images
            bookbadge = MIMEImage(bookbadge, 'png')
            QRcode = MIMEImage(QRcode, 'png')
            bookbadge.add_header('Content-ID', '<bookbadge>')
            QRcode.add_header('Content-ID', '<QRcode>')
            message.attach(QRcode)
            message.attach(bookbadge)

        
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls() 
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                server.quit()
                print("Email sent successfully!")
                return redirect('/')
            except smtplib.SMTPException as e:
                error_message = 'Invalid credentials. Please try again.'
                return render(request, 'register.html', {'error_message': error_message})






