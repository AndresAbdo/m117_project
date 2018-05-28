"""StudyBuddyProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from studybuddy import views as sb_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # root StudyBuddy url is /sb/
    path('sb/', include('studybuddy.urls')),

    # Redirect root URL to URL 127.0.0.1:8000/sb/
    path('', RedirectView.as_view(url='/sb/')),


	path('login/', auth_views.login, name='login'),
	path('logout/', auth_views.logout, {'next_page':'login'}, name='logout'),
	path('signup/', sb_views.signup, name='signup'), 
]
