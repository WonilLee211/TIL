from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

# 어드민 사이트에 등록한다.
admin.site.register(User, UserAdmin)
