from django import template 
from adminBlog.models import Post


register=template.library()
@register.inclusion_tag('djangoBlog'/latest_posts.html)


def latest_posts():
	context={
	'l_posts':post.objects.all()[0:3]
	}
	return context