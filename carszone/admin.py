from django.contrib import admin
from .models import Teams
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%">'.format(object.photo.url))
    
    thumbnail.short_description= 'Photo'
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_at')
    list_display_links = ('first_name','id', 'thumbnail')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)


admin.site.register(Teams, TeamAdmin)
