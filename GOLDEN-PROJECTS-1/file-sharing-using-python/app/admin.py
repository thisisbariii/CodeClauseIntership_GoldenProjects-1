from django.contrib import admin
from .models import myfile
# Register your models here.
@admin.register(myfile)
class fileadmin(admin.ModelAdmin):
    list_display=['id' ,'file']