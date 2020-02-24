from django.urls import path
from adminBlog import views
urlpatterns=[
	path('users',views.users),
	path('user_add',views.user_add),
	path('user_delete/<id>',views.user_delete),
	path('user_edit/<id>',views.user_edit),
	path('forbidden',views.forbidden),
	path('forbidden_delete/<id>',views.forbidden_delete)
	





]
