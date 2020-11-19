from django.contrib import admin

# Register your models here.
from .models import Acc, Detail, Debit, Credit

admin.site.register(Acc)
admin.site.register(Detail)
admin.site.register(Debit)
admin.site.register(Credit)
