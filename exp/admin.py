from django.contrib import admin

# Register your models here.
from .models import Acc, Details

admin.site.register(Acc)
admin.site.register(Details)