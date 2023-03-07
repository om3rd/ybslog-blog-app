from django.contrib import admin
from .models import Article

# Register your models here.

@admin.register(Article) #models kısmında yaptığımız modeli adminde göstermek için önce import sonra da bu şekilde gösterttik
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author","created_date")
    list_display_links = ("title","created_date")
    search_fields = ["title"]
    ordering = ["created_date"]
    list_filter = ["created_date"]
    
    class Meta:
        model = Article  #class da decorative kullanmak için ve article ları bağlamak için django bunu öneriyor
        
        