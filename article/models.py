from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

#burada author başka tabloyu işaret etmesi için foreign key oldu ve bu kişi silinince tüm her şeyi silinmesi için ise cascade kullanıldı    
class Article(models.Model):  #djangonun kendi tablosu olan auth user ı aldık
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE) 
    title = models.CharField(max_length = 50) 
    content = RichTextField()
    subtitle = models.CharField(max_length=180, null= True)
    created_date = models.DateField(auto_now_add = True)
    linkedin = models.URLField(null = False, blank = True, max_length=200)
    github = models.URLField(max_length = 200, null = False, blank = True)
    article_image = models.FileField(blank = True, null = True,verbose_name ="Add photo into article")
    
    
    def __str__(self):  #admin panalindeki articles object yerine direkt title kendi döncek
        return self.title
    