"""
URL configuration for temppro2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings          #This one and below one are belong to image
from django.conf.urls.static import static   # This is also belongs to image


from django.urls import path
from tempapp2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('home',views.homePage,name='home'),
    path('add',views.contactPage,name='add'),
    path('stu_login',views.studentsPage,name='stu_login'),
    # path('service',views.servicePage,name='service'),
    path('edits',views.editservice,name='edits'),       #update buttons in this html page
    path('upservice',views.Upservice,name='upservice'), #display page for updateservice
    path('update/<id>',views.updateserv,name='update'), #getting html page with id (main page of modifications)
    path('updating/<id>',views.updating_data,name='updating'), #post the the with updating data
    path('delete/<id>',views.deleting_data,name='delete'),
    path('stu_delete/<id>',views.stu_delete,name='stu_delete'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('boys',views.hostelform,name='boys'),
    path('hostel',views.hosteldata,name='hostel')
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
