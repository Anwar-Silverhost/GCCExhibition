from django.urls import path
from exhibitor_app import views

urlpatterns = [
    path('exhibitor_navbar',views.exhibitor_navbar,name="exhibitor_navbar"),
    path('exhibitor_dashboard',views.exhibitor_dashboard,name="exhibitor_dashboard"),
    path('exhibitor_scanner',views.exhibitor_scanner,name="exhibitor_scanner"),
    path('boothvisitor_qrscan',views.boothvisitor_qrscan,name="boothvisitor_qrscan"),
    path('exhibitor_settings',views.exhibitor_settings,name="exhibitor_settings"),
    path('exhibitor_logout',views.exhibitor_logout,name="exhibitor_logout"),
]