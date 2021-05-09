from django.contrib import admin
from .models import NEWS,Comment

@admin.register(NEWS)
class Cat(admin.ModelAdmin):
    list_display=('name','date')
    list_filter=('name','date')
    search_fields = ("name", )

class Cat1(admin.ModelAdmin):
    fields = ('name',)


admin.site.register(Comment)

