from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm   #burada forms.py de yaptığımız kontrolü ve formu buraya bağladık
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)  #post request gelmiyorsa none gelicek ve boş kalıcak içi böylyece get olcak
    if form.is_valid():  #bunu yaptığımızda clean metodunu alıyor django
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        linkedin = form.cleaned_data.get("linkedin")
        github = form.cleaned_data.get("github")
        newUser = User(username = username)  #user objemizi oluşturduk
        newUser.set_password(password)
        #newUser = User(linkedin = linkedin)
        #newUser = User(github = github)
        newUser.save()   #butona basıldığında da veritabanına kayıt edilcek
            
        login(request,newUser) #kullanıcı kayıt olduktan sonra login olması için
        messages.success(request,"Successfully Signed Up!")
        
        return redirect("index") #redirect yaparak login olan kullanıcı anasayfaya yönlendirilcek        
        
    context = {
        "form" : form #formu şimdi register.html'ye gönderdik
    }
    return render(request,"register.html",context)

     

def loginUser(request):
    form = LoginForm(request.POST or None) #yukardan boş dönünce buraya gelicek
    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username") #extra bir şey yapmadan clean methodu çalışıyor
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username, password = password) #değişkene atadık çünkü kontrol etmemizi sağlıyor
        
        if user is None:
            messages.info(request,"Username or Password Is Wrong!")
            return render(request,"login.html",context)
        messages.success(request,"Successfully Logged In!")
        login(request,user)
        return redirect("index")
    
    return render(request,"login.html",context) #get request veya post request de sıkıntı çıktıysa
    
    
def logoutUser(request):
    logout(request)
    messages.success(request,"Successfully Logged Out!")
    return redirect("index")
    




