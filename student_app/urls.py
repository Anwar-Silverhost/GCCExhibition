from django.urls import path
from student_app import views

urlpatterns = [
   path('registration_save',views.registration_save,name='registration_save'),

]