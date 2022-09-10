from django.contrib import admin

# Register your models here.
from .models import Page, Revision

admin.site.register(Page)
admin.site.register(Revision)