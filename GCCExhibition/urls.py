from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('as_admin', views.admin_login, name='admin_login'),
    path('register',views.register,name="register"),
    path('student_app/', include('student_app.urls')),
    path('admin_user/',include('admin_user.urls')),
    path('AppStore/',views.appstore,name="appstore"),
    path('as_Exhibitor', views.exhibitor_login, name='exhibitor_login'),
    path('exhibitor_app/',include('exhibitor_app.urls')),
    path('as_Executive', views.executive_login, name='executive_login'),
    path('executive_app/',include('executive_app.urls')),





]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 