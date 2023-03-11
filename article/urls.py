from django.contrib import admin
from django.urls import path
from article import views


app_name = "articles"

urlpatterns = [
    path('dashboard/',views.dashboard, name = "dashboard"),
    path('addarticle/',views.Addarticle, name = "addarticle"),
    path('article/<int:id>',views.detail, name = "detail"), #dinamik url ile makalemizin id'si neyse ona yönlendirmesini sağlayacak dasboard'da zaten belirtmiştik burda da gidecek yer verdik
    path('update/<int:id>',views.update, name = "update"),
    path('delete/<int:id>',views.delete, name = "delete"),
    path('',views.articles, name = "articles"), #boş bıraktık çünkü blog altındaki URL'de articles/ include yapmıştık böylece boş bırakırsak makaleler çıkacak 
]