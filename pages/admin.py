from django.contrib import admin
from pages.models import HomePage
# Register your models here.

class TinyMCEAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/media/js/tiny_mce/tiny_mce.js', '/static/media/js/tiny_mce/textareas.js')	

admin.site.register(HomePage, TinyMCEAdmin)
