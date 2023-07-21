from django.contrib import admin
from app.models import Pelucia
# Register your models here.

class PeluciaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pelucia, PeluciaAdmin)