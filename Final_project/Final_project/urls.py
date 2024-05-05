"""
URL configuration for Final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('root.urls')),
    path('tutor/', include('tutor.urls')),
    path('customer/', include('customer.urls')),
    path('admin/', include('admin.urls')),
    path('order/', include('order.urls')),
    path('social-auth/',include('social_django.urls',namespace='social')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':    settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
    
    # path('admin/', include('admin.urls')),
    # path('login', views.login, name='login'),
    # path('reg_cus', views.reg_cus, name='reg_cus'),
    # path('add_tutor', views.add_tutor, name='add_course'),
    # path('admin/add_tutor', views.admin_add_tutor, name='add_tutor'),
    # path('admin/edit_tutor/<int:id>', views.edit_tutor, name='edit_tutor'),
    # path('admin/edit_tutor', views.tutor_edit, name='tutor_edit'),
    # path('admin', views.admin, name='admin'),
    # path('admin/customer', views.admin_cus, name='cus_admin'),
    # path('admin/admin_customer', views.admin_customer, name='admin_customer'),
    # path('admin/admin_tutor', views.admin_tutor, name='add_course_admin'),
    # path('admin/delete_tutor/<int:id>', views.delete_tutor, name='delete_tutor'),
    # path('admin/cus_edit/<int:id>', views.cus_edit, name='cus_edit'),
    # path('admin/edit_cust', views.edit_cust, name='edit_cust'),
    # path('admin/cus_delete/<int:id>', views.cus_delete, name='cus_delete'),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
