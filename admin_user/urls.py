from django.urls import path
from admin_user import views

urlpatterns = [
    path('admin_navbar',views.admin_navbar,name="admin_navbar"),
    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('admin_register_view',views.admin_register_view,name="admin_register_view"),
    path('remove_regs/<int:id>',views.remove_regs,name="remove_regs"),
    path('admin_events',views.admin_events,name="admin_events"),
    path('edit_event/<int:id>',views.edit_event,name="edit_event"),
    path('delete_event/<int:id>',views.delete_event,name="delete_event"),
    path('admin_exhibitors',views.admin_exhibitors,name="admin_exhibitors"),
    path('admin_view_exhibitors/<int:id>',views.admin_view_exhibitors,name="admin_view_exhibitors"),
    path('Update_admin_exhibitors/<int:id>',views.Update_admin_exhibitors,name="Update_admin_exhibitors"),
    path('delete_Exhibitors/<int:id>',views.delete_Exhibitors,name="delete_Exhibitors"),
    path('admin_executives',views.admin_executives,name="admin_executives"),
    path('saveExecutive',views.saveExecutive,name="saveExecutive"),
    path('deleteExecutive/<int:id>',views.deleteExecutive,name="deleteExecutive"),

]