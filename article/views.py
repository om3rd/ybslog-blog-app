from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


@login_required(login_url= "user:login") #user app altındaki url dosyasında yer alan login uzantımızı verdik
def dashboard(request):
    articles = Article.objects.filter(author = request.user) #tüm article'ları aldık ve yazar olarak açık hesabı seçerek dashboard'da kendi makalesini görsün diye
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)


@login_required(login_url= "user:login")
def Addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None) #files kısmını ekleme sebebimiz görsel içerik veya harici dosya ekleyebilmek için
    context = {
        "form":form
    }
    
    if form.is_valid():
        article = form.save(commit = False) #objeye atıp commit false deme sebebimiz ismi almadığımız için direkt save yapamayız hata veriyor ondan dolayı böyle yapmak durumundayız
        article.author = request.user #author bilgisi olarak user'dan gelen request ile atayabiliriz böylece ismi almış oluruz
        article.save() #şimdi artık save edebiliriz
        
        messages.success(request,"Article Successfully Created")
        return redirect("articles:dashboard")
        
    return render(request,"addarticle.html",context)
    

def detail(request,id): #dinamik url geldiği zaman id almamız gerekiyor ve id'yi içine ondan dolayı verdik
    #article = Article.objects.filter(id = id).first() #queryset hatası veriyor çünkü liste döndürüyor bizde dedik ki ilk gördüğünü al
    article = get_object_or_404(Article,id = id) #bunu bu şekilde yapma sebebimiz ise olmayan sayfaya gidince hata vermesi için
    context ={
        "article":article
    }
    return render(request,"detail.html",context)


@login_required(login_url= "user:login")
def update(request,id):
    article = get_object_or_404(Article,id = id)            #instance eski verileri alıyor ve aşağıda eski verileri değiştiriyoruz.
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if article.author == request.user:
        if form.is_valid():
            article = form.save(commit = False)
            article.author = request.user
            article.save()
            messages.success(request,"Article Successfully Updated!")
            return redirect("articles:dashboard")
    else:
        messages.info(request, "You Can't Update Other User's Article!")
        return redirect("article:dashboard")

    #is valid değil ve get request ise
    context = {
        "form":form
    }
    return render(request,"update.html",context)


@login_required(login_url= "user:login")
def delete(request,id):
    article = get_object_or_404(Article,id = id)
    if article.author == request.user:
        article.delete()
        messages.success(request,"Article Successfully Deleted!")
        return redirect("articles:dashboard") #article altındaki dashboard'a git dedik url ismine göre
    else:
        messages.info(request, "You Can't Delete Other User's Article!")
        return redirect("article:dashboard")