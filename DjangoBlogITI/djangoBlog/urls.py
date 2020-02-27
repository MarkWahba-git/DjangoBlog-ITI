from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from .import views


urlpatterns = [
    # url('signup', views.signup, name='signup'),
    # # url('home/', views.home, name='home'),
    # url('signin/', views.confirm_login_allowed, name='confirm'),
    # url('signin/', views.login_view, name='signin'),
    # # path('post', views.createpost),
	path('indeex/',views.body),
	path('showpost/<postid>/',views.post_detail),
	path('showpost/<postid>/addcomment',views.addcomment),
    
]




