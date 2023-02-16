from django.contrib import admin
from .models import User
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ("is_superuser",)
    

admin.site.register(User,PostAdmin)