from django.contrib import admin
from news.models import News, Category, Tags


admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)
# Register your models here.
