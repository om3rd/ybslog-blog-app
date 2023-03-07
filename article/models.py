from django.db import models

# Create your models here.

#burada author başka tabloyu işaret etmesi için foreign key oldu ve bu kişi silinince tüm her şeyi silinmesi için ise cascade kullanıldı    
class Article(models.Model):  #djangonun kendi tablosu olan auth user ı aldık
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE) 
    title = models.CharField(max_length = 50) 
    content = models.TextField()
    created_date = models.DateField(auto_now_add = True)
    
    def __str__(self):  #admin panalindeki articles object yerine direkt title kendi döncek
        return self.title
    