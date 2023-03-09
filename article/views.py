from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
# Create your views here.

def index(request):

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    articles = Article.objects.filter(author = request.user) #tüm article'ları aldık ve yazar olarak açık hesabı seçerek dashboard'da kendi makalesini görsün diye
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

def Addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    context = {
        "form":form
    }
    
    if form.is_valid():
        article = form.save(commit = False) #objeye atıp commit false deme sebebimiz ismi almadığımız için direkt save yapamayız hata veriyor ondan dolayı böyle yapma durumundayız
        article.author = request.user #author bilgisi olarak user'dan gelen request ile atayabiliriz böylece ismi almış oluruz
        article.save() #şimdi artık save edebiliriz
        
        messages.success(request,"Article Successfully Created")
        return redirect("index")
    
    
    
    return render(request,"addarticle.html",context)
    

def detail(request,id): #dinamik url geldiği zaman id almamız gerekiyor ve id'yi içine ondan dolayı verdik
    #article = Article.objects.filter(id = id).first() #queryset hatası veriyor çünkü liste döndürüyor bizde dedik ki ilk gördüğünü al
    article = get_object_or_404(Article,id = id) #bunu bu şekilde yapma sebebimiz ise olmayan sayfaya gidince hata vermesi için
    context ={
        "article":article
    }
    return render(request,"detail.html",context)
