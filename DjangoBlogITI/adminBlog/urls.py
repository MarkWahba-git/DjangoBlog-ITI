from django.urls import path
from adminBlog import views
urlpatterns=[
	path('users',views.users),
	path('user_add',views.user_add),
	path('user_delete/<id>',views.user_delete)





]
