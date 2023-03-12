from django import forms
from .models import Article



class ArticleForm(forms.ModelForm):  #formun modeli olduğu için direkt model formdan kullanmak daha kolay
    class Meta:  #burada yapılanlar tamamiyle django gereği yapılıyor model = Article dokümanda yer alıyor
        model = Article #formumuz ile modelimiz artık bağl
        fields = ["title","subtitle","content","article_image"]  #input alanı tanımlamadan direkt model üstünden django kendi yaptı
        
        
