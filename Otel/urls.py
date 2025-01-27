"""
URL configuration for Otel project.

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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include, re_path, include

from OtelIcerik.views import *
from OtelRestApiBlokaj.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Anasayfa Login Sayfası
    path('', anasayfa, name="anasayfa"),

    # Api'leri includes et
    path('api/v1/', send_routes, name="apitest"),
    path('api/v1/checkstatus', checkstatus, name="checkstatus" ),

    # Otel Oda DashBoard
    path('dashboard', dashboard, name="dashboard"),

    # Misafir Detay Sayfası
    path('misafirdetay/<misafirID>', misafirdetay, name="misafirdetay"),

    # Misafir Ekle
    path('misafirekle/<odaID>', misafirekle, name="misafirekle"),
    
    # Blokaj Sayfası
    path('blokaj', blokaj, name="blokaj"),

    # Muhasebe Sayfası
    path('muhasebe', muhasebe, name="muhasebe"),
    
    # Oda Detay
    path('odadetay/<odaID>', odadetay, name="odadetay"),

    # Oda Sil
    path('odasil/<odaID>', odasil, name="odasil"),

    # Oda Ekle
    path('odaekle', odaEkle, name="odaekle"),
    # Logout
    path('logout', cikisYap, name="logout"),
    # 404 Sayfası
    re_path(r'^.*/$', hatasayfasi, name="404"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
