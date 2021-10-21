from django.contrib import admin

# Register your models here.


from .models import *



class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'photo', 'is_public', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'id')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name', 'id')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Human, HumanAdmin)