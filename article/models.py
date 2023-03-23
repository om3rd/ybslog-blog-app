from django.db import models
from ckeditor.fields import RichTextField
from django.core import validators
from django.forms.fields import URLField as FormURLField

# Create your models here.

#burada author başka tabloyu işaret etmesi için foreign key oldu ve bu kişi silinince tüm her şeyi silinmesi için ise cascade kullanıldı    
class Article(models.Model):  #djangonun kendi tablosu olan auth user ı aldık
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE) 
    title = models.CharField(max_length = 50) 
    content = RichTextField()
    subtitle = models.TextField(max_length=80, null= True)
    created_date = models.DateField(auto_now_add = True)
    article_image = models.FileField(blank = True, null = True,verbose_name ="Add photo into article")
    
    
    def __str__(self):  #admin panalindeki articles object yerine direkt title kendi döncek
        return self.title

"""class URL(models.URLField):
    default_validators = [validators.URLValidator()]
    linkedin = models.URLField(null = False, blank = True, max_length=200)
    github = models.URLField(max_length = 200, null = False, blank = True)"""
    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Article",related_name="comments") #yukardaki article classı ile bağladık
    comment_author = models.CharField(max_length=50,verbose_name="Name")
    comment_content = models.CharField(max_length=250,verbose_name="Content")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    #daha sonra bunları admin panaline kayıt ettirmek için admin paneline de eklememiz gerekiyor
    