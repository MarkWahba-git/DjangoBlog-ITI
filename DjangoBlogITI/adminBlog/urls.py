from django.urls import path
from adminBlog import views
urlpatterns=[
	path('users',views.users),
	path('user_add',views.user_add),
	path('user_delete/<id>',views.user_delete),
	path('user_edit/<id>',views.user_edit),
	path('user_block/<id>',views.user_block),
	path('user_promote/<id>',views.user_promote),
	path('forbidden',views.forbidden),
	path('forbidden_delete/<id>',views.forbidden_delete),
	path('forbidden_add',views.forbidden_add),
	path('forbidden_edit/<id>',views.forbidden_edit),
	path('categories',views.categories),
	path('cat_delete/<id>',views.cat_delete),
	path('category_add',views.category_add),
	path('category_edit/<id>',views.category_edit),
	path('side_categories',views.side_categories),

############################################### my pages
	path('post', views.createpost),
	path('index',views.index),
	path('showpostdetails/<postid>/',views.post_detail),
	path('showpostdetails/<postid>/addcomment',views.addcomment),

	path('all_posts',views.all_posts),
	path('post_delete/<id>',views.post_delete),
	path('select/<name>',views.select)



	


    ]  
	
	
	
	
