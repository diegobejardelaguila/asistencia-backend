from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    search_fields = ('first_name', 'last_name', 'email',)