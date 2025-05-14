from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Avval ro'yxatdan chiqaramiz (agar kerak bo‘lsa)
admin.site.unregister(User)

# Keyin yana ro'yxatdan o'tkazamiz
admin.site.register(User, UserAdmin)
