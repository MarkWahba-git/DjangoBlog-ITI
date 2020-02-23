"""DjangoBlogITI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin

# from DjangoBlogITI import views
# from djangoBlog.views import *
# from adminBlog.views import *
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.views import logout


urlpatterns = [
    path('admin/', admin.site.urls),
]
# urlpatterns = [
#     url(r'^login_form$', login_form),
#     url(r'^logged_in_only$', logged_in_only),
#     url(r'^signup/$', signup),
#     url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
#     url(r'^allCats/$', all_categories),
#     url(r'^home/$', home),
#     url(r'^likes/(?P<post_id>[0-9]+)/$', show_likes),
#     url(r'^dislikes/(?P<post_id>[0-9]+)/$', show_dislikes),
#     url(r'^addlike/(?P<post_id>[0-9]+)/$', add_like),
#     url(r'^adddislike/(?P<post_id>[0-9]+)/$', add_dislike),
#     url(r'^search/(?P<term>[A-Za-z0-9]+)/$', search),
#     url(r'^addcomment/(?P<text>[a-zA-Z0-9_ ]+)/(?P<post>[0-9]+)/$', add_comment),
#     url(r'^reply/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)/$', show_reply),
#     url(r'^addreply/(?P<text>[a-zA-Z0-9_ ]+)/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)$', add_reply),
#     url(r'^unsup/(?P<cat_id>[0-9]+)/', un_sup),
#     url(r'^sup/(?P<cat_id>[0-9]+)/', sup),
#     url(r'^allCats/(?P<name>[a-z]+)/$', post_by_category),
#     url(r'^allPosts$', all_posts),
#     url(r'^category/(?P<cat_id>[0-9]+)/$', get_category),
#     url(r'^user/(?P<user_id>[0-9]+)/$', get_user),
#     url(r'^posts/(?P<post_id>[0-9]+)/$', show_post),
#     url(r'^comments/(?P<post_id>[0-9]+)/$', show_comments),
#     url(r'^allusers/', allUsers),
#     url(r'^block/(?P<usr_id>[0-9]+)/$', user_block),
#     url(r'^unblock/(?P<usr_id>[0-9]+)$', user_unblock),
#     url(r'^promote/(?P<usr_id>[0-9]+)$', user_promote),
#     url(r'^(?P<usr_id>[0-9]+)/delete', user_delete),
#     url(r'^(?P<usr_id>[0-9]+)/update', user_update),
#     url(r'^user/new', user_new),
#     url(r'^allcategories/$', allCategories),
#     url(r'^alltags/$', allTags),
#     url(r'^alltags/new', tag_new),
#     url(r'^allcategories/new/$', category_new),
#     url(r'^allcategories/(?P<cat_id>[0-9]+)/update', category_update),
#     url(r'^allcategories/(?P<cat_id>[0-9]+)/delete', category_delete),
#     url(r'^allbadwords/$', allBadwords),
#     url(r'^allbadwords/new/$', badword_new),
#     url(r'^allbadwords/(?P<word_id>[0-9]+)/update', badword_update),
#     url(r'^allbadwords/(?P<word_id>[0-9]+)/delete', badword_delete),
#     url(r'^allposts/', allPosts),
#     url(r'^post/new', post_new),
#     url(r'^post/(?P<post_id>[0-9]+)/edit', Posts_edit),
#     url(r'^post/(?P<post_id>[0-9]+)/del', Post_delete),
#     url(r'^index', admin),
#     url(r'base', base_dir),
#     url(r'^post/(?P<post_id>[0-9]+)',getPost),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)