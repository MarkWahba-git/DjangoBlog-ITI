from django.urls import path
from adminBlog import views
urlpatterns=[
	path('users',views.users),
	path('user_add',views.user_add),
	path('user_delete/<id>',views.user_delete),
	path('user_edit/<id>',views.user_edit),
	path('forbidden',views.forbidden),
	path('forbidden_delete/<id>',views.forbidden_delete),
	path('forbidden_add',views.forbidden_add),
	path('forbidden_edit/<id>',views.forbidden_edit),
	path('categories',views.categories),
	path('cat_delete/<id>',views.cat_delete),
	path('category_add',views.category_add),
	path('category_edit/<id>',views.category_edit)
	
	
	
	
	
	
	





]
