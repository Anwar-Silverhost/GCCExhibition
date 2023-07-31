from django.shortcuts import render,redirect
from executive_app.models import *
from student_app.models import *
from django.http import JsonResponse
from datetime import datetime




# Create your views here.

# Create your views here.
def executive_navbar(request):
    if 'ExUser_id' in request.session:
        if request.session.has_key('ExUser_id'):
            ExUser_id = request.session['ExUser_id']
        else:
            return redirect('/')
        ExUser = Executives.objects.filter(id=ExUser_id)
        return render(request,'Executive/executive_navbar.html',{'ExUser':ExUser})
    else:
        return redirect('/as_Executive')

def executive_scanner(request):
    if 'ExUser_id' in request.session:
        if request.session.has_key('ExUser_id'):
            ExUser_id = request.session['ExUser_id']
        else:
            return redirect('/')
        ExUser = Executives.objects.filter(id=ExUser_id)
        return render(request,'Executive/executive_scanner.html',{'ExUser':ExUser})
    else:
        return redirect('/as_Executive')

def executive_dashboard(request):
    if 'ExUser_id' in request.session:
        if request.session.has_key('ExUser_id'):
            ExUser_id = request.session['ExUser_id']
        else:
            return redirect('/')
        ExUser = Executives.objects.filter(id=ExUser_id)
        atend = EntranceScan.objects.filter(Executive = ExUser_id)
        return render(request,'Executive/executive_dashboard.html',{'ExUser':ExUser,'atend':atend})
    else:
        return redirect('/as_Executive')


def entrance_qrscan(request):
    if request.method == 'POST':
        QrCode = request.POST.get('QrCode')
        exeid = request.POST.get('ExeID')
        exe = Executives.objects.get(id=exeid)
        details = Student_Registration.objects.get(booking_ID=QrCode)
        if Student_Registration.objects.filter(booking_ID=QrCode).exists():
            if EntranceScan.objects.filter(booking_ID=QrCode).filter(Executive=exeid).exists():
                response_data = {'status': 'exist'}
                return JsonResponse(response_data)
            else:
                if exe.event.id == details.event.id :
                    visitorname = details.fullname
                    bv = EntranceScan()
                    bv.Executive = exe
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


def executive_logout(request):
    if 'ExUser_id' in request.session:
        request.session.flush()
    return redirect('/as_Executive')