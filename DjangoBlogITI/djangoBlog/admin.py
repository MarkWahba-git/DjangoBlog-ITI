from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from djangoBlog.models import forbidden_words,category,subscribe

# Register your models here.
admin.site.register(forbidden_words)
admin.site.register(category)
admin.site.register(subscribe)
