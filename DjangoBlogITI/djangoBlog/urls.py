from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as authView
from .import views



urlpatterns = [
    # url('signup', views.signup, name='signup'),
    # # url('home/', views.home, name='home'),
    # url('signin/', views.confirm_login_allowed, name='confirm'),
    # url('signin/', views.login_view, name='signin'),
    # # path('post', views.createpost),
	path('indeex/',views.body,name="login"),
    path('signup/',views.signup),
    path('about/',views.about),
    path('contact/',views.contact),
    path("signin",views.login_view),

	path('showpost/<postid>/',views.post_detail),
	path('showpost/<postid>/addcomment',views.addcomment),
	path('showpost/<comid>/addreply',views.addreply),

	path('showpostdetails/<postid>/',views.post_detail),
	path('showpostdetails/<postid>/addcomment',views.addcomment),
    path('select/<name>/',views.select),
     path('indeex/',views.side_categories),
	path('sub/<category_id>', views.subscribes, name ='subscribes'),
    path('unsub/<category_id>', views.unsubscribe, name ='unsubscribe'),
    # path('logout/', authView.LogoutView.as_view(template_name='indeex.html'), name='logout'),
     path('logout/', authView.LogoutView.as_view(), name='logout'),


    path('like/<id>', views.liked),
    path("dislike/<id>", views.disliked)

    # url("like/<postID>", views.liked),
    # urL("unlike/<postID>", views.disliked)


]




