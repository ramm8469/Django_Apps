"""HelpDesk_Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin

urlpatterns = [
    path('',include('ticket_system.urls')), # for CRUD and HomePage
    path('admin/', admin.site.urls),
    # path('admin/',admin.site.urls,name='Admin_login'), # For admin login
    path('accounts/',include('django.contrib.auth.urls')), # For Login
    path('signup/',include('accounts.urls')), # for signup
    # path('agents/',include('agents.urls')), # For Agents
    
    
]
