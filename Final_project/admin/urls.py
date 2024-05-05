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
from . import views as v

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', v.index, name='admin'),
    path('customer', v.admin_cus, name='cus_admin'),
    path('admin/admin_tutor', v.admin_tutor, name='add_course_admin'),
    path('admin/admin_customer', v.admin_customer, name='admin_customer'),
    path('login', v.login, name='admin_login'),
    path('admin/cus_edit/<int:id>', v.cus_edit, name='cus_edit'),
    path('admin/edit_cust', v.edit_cust, name='edit_cust'),
    path('admin/cus_delete/<int:id>', v.cus_delete, name='cus_delete'),
    path('login_admin', v.login_admin, name='login_admin'),
    path('logout', v.logout, name='logout'),
    path('order', v.order_index, name='admin_order')
    

]