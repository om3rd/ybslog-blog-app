"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from article import views #article klasöründeki views dosyası içindeki index fonksiyonunu al dedik
                            #hatta direkt article klasöründen views dosyasını aldık böylece path kısmında
                            #views içinden gerekli şeyi alcaz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"), #boş bırakırsak localhost:8000'de bura çalışacak
    path('about/', views.about, name = "about"),
    #path('detail/<int:id>', views.detail, name = "detail"),
    path('articles/',include("article.urls")),  #articles/deneme10 , articles/makale3
    path('user/',include("user.urls")),  #user/register , user/login
    
]
