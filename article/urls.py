from django.contrib import admin
from django.urls import path
from article import views


app_name = "articles"

urlpatterns = [
    path('create/',views.index, name = "index"),
    path('dashboard/',views.dashboard, name = "dashboard"),
    path('addarticle/',views.Addarticle, name = "addarticle"),
    path('article/<int:id>',views.detail, name = "detail"), #dinamik url ile makalemizin id'si neyse ona yönlendirmesini sağlayacak dasboard'da zaten belirtmiştik burda da gidecek yer verdik
    
]