from django import forms
from django.contrib.auth.models import User
from urllib.parse import urlparse


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "User Name")
    password = forms.CharField(min_length = 6, max_length = 20,label = "Password",widget = forms.PasswordInput)
    confirm = forms.CharField(min_length= 6,max_length = 20,label = "Confirm",widget = forms.PasswordInput)
    github = forms.URLField(required = True)
    linkedin = forms.URLField(required= True)
    
    def clean(self):
        username = self.cleaned_data.get("username")  #burada şifrenin kontrolünü sağlayan bir yapı var
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        github = self.cleaned_data.get("github")
        linkedin = self.cleaned_data.get("linkedin")
        
        if password and confirm and password != confirm:
            raise forms.ValidationError("Password Doesn't Match!")
        
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('This Username Already Exist! Please Pick Another One')
        
        values = {  #if durumuna girmezse ve hepsini döndürmem lazım o zamanda sözlük ile döndürmek zorundayım
            "username" : username,
            "password" : password,
            "github" : github,
            "linkedin" : linkedin
        }
        return values
    
    def validate_url(value):
        if not value:
            return  # Required error is done the field
        obj = urlparse(value)
        if not obj.hostname in ('github.com', 'linkedin.com'):
            raise ValidationError('Only urls from GitHub or Linkedln allowed')

    
class LoginForm(forms.Form):
    username = forms.CharField(label = "User Name")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)
    
    