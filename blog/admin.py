from django.contrib import admin
from .models import BlogEntry,UserInfo,Videos,FoodBlog,About

# Register your models here.


class BolEntryAdmin(admin.ModelAdmin):
    list_display=('title','isActive','isHome')
    list_editable=('isActive','isHome')
    search_fields=('title','description')


admin.site.register(BlogEntry)
admin.site.register(UserInfo)
admin.site.register(Videos)
admin.site.register(FoodBlog)
admin.site.register(About)
