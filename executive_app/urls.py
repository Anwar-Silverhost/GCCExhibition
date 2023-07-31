from django.urls import path
from executive_app import views

urlpatterns = [
    path('executive_navbar',views.executive_navbar,name="executive_navbar"),
    path('executive_dashboard',views.executive_dashboard,name="executive_dashboard"),
    path('executive_scanner',views.executive_scanner,name="executive_scanner"),
    path('entrance_qrscan',views.entrance_qrscan,name="entrance_qrscan"),
    path('executive_logout',views.executive_logout,name="executive_logout"),

]