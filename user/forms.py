from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "User Name")
    password = forms.CharField(min_length = 6, max_length = 20,label = "Password",widget = forms.PasswordInput)
    confirm = forms.CharField(min_length= 6,max_length = 20,label = "Confirm",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")  #burada şifrenin kontrolünü sağlayan bir yapı var
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        
        if password and confirm and password != confirm:
            raise forms.ValidationError("Password Doesn't Match!")
        
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('This Username Already Exist! Please Pick Another One')
        
        values = {  #if durumuna girmezse ve hepsini döndürmem lazım o zamanda sözlük ile döndürmek zorundayım
            "username" : username,
            "password" : password
        }
        return values
    
    
class LoginForm(forms.Form):
    username = forms.CharField(label = "User Name")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)
    
    