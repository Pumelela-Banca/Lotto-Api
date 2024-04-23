"""
URL configuration for lotto_draws project.

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
from django.urls import path
from lotto_draws import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('daily/', views.daily_draws),
    path('daily/<int:year>-<int:month>-<int:day>/', views.daily_draws),
    path('powerball/', views.powerball_draws),
    path('powerball/<int:year>-<int:month>-<int:day>/', views.daily_draws),
    path('powerballplus/', views.powerball_plus_draws),
    path('powerballplus/<int:year>-<int:month>-<int:day>/', views.daily_draws),
    path('lotto/', views.lotto_draws),
    path('lotto/<int:year>-<int:month>-<int:day>/', views.daily_draws),
    path('lotto1/', views.lotto1_draws),
    path('lotto1/<int:year>-<int:month>-<int:day>/', views.daily_draws),
    path('lotto2/', views.lotto2_draws),
    path('lotto2/<int:year>-<int:month>-<int:day>/', views.daily_draws),
]
