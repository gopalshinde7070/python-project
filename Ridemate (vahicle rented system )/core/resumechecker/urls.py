from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name='homepage'),
    path("ht/",views.ht,name='ht'),
    path("index/",views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_job/',views.admin_job,name='admin_job'),


    path("admin_job_list", views.admin_job_list, name="admin_job_list"),
    path("edit_job/<int:id>/", views.edit_job, name="edit_job"),
    path("delete_job/<int:id>/", views.delete_job, name="delete_job"),
    path("all_admin_side_matterial/", views.all_admin_side_matterial, name="all_admin_side_matterial"),
    path('logout/', views.user_logout, name='logout'),

]