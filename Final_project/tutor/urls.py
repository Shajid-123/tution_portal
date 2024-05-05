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
    path('', v.add_tutor, name='add_course'),
    path('add_tutor_admin', v.admin_add_tutor, name='add_tutor'),
    path('edit_tutor/<int:id>', v.edit_tutor, name='edit_tutor'),
    path('edit_tutor', v.tutor_edit, name='tutor_edit'),
    path('delete_tutor/<int:id>', v.delete_tutor, name='delete_tutor'),
    # path('reg_cus', v.reg_cus, name='reg_cus'),
    path('user/email_verification/<str:id>',v.email_verify, name = 'ef'),
    path('reg_conf', v.reg_conf, name='reg_conf_tutor'),
    path('details/<int:id>', v.details, name='view_details'),
    path('search', v.search, name='search'),
    # path('csv_upload', v.csv, name='add_tutor_csv')
]
