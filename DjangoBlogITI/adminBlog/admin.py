from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from adminBlog.models import forbidden_words,category,Post,Tags
# Register your models here.
UserAdmin.list_display += ('is_active','last_login')
UserAdmin.list_editable = ('is_active','is_staff')


# Register your models here.

admin.site.register(forbidden_words)
admin.site.register(category)
admin.site.register(Post)
admin.site.register(Tags)


