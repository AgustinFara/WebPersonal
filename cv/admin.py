from django.contrib import admin
from .models         import Work
from .models         import Client
from .models         import Technology

# Register your models here.

class WorkAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Work)

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Client)

class TechAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Technology)
