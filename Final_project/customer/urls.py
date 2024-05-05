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
    path('register', v.register, name='register'),
    path('reg_cus', v.reg_cus, name='reg_cus'),
    path('user/email_verification/<str:id>',v.email_verify, name = 'email_verify'),
    path('reg_conf', v.reg_conf, name='reg_conf'),
    path('login', v.login, name='login'),
    path('login_cus', v.cus_login, name='login_cus'),
    path('logout', v.logout, name='logout_cus'),
    
]