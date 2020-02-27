from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from adminBlog.models import forbidden_words,category,Post
from django.http import HttpResponse,HttpResponseRedirect
from adminBlog.form import usr_form
from adminBlog.form import cat_form,word_form,usr_block,usr_promote
from django.contrib.auth.backends import BaseBackend
from .models import Post, Comment ,Tags ,reply,subscribe
from adminBlog.form import postform,commentform
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .form import UserRegisterationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
#from .forms import postform,commentform


# Create your views here.
def users(request):
	all_users=User.objects.all()
	context={'all_users':all_users}
	return render(request,'users_tables.html',context)

def user_add(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/adminBlog/users')
    else:
        form = UserRegisterationForm()
    return render(request, 'user_form.html',{'usr_form': form})

# def user_add(request):
# 	if request.method=='POST':
# 		user_form=usr_form(request.POST)
	
# 		if user_form.is_valid():
# 			user_form.save()
# 			return HttpResponseRedirect('/adminBlog/users')


# 	else:
# 		user_form=usr_form()
# 		context={'usr_form':user_form}
# 		return render(request,'user_form.html',context)	

def user_delete(request,id):
	usr=User.objects.get(id=id)
	usr.delete()
	return HttpResponseRedirect('/adminBlog/users')

def user_edit(request,id):
	usr=User.objects.get(id=id)
	if request.method=='POST':
		user_form=usr_form(request.POST,instance=usr)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect('/adminBlog/users')

	else:
		user_form=usr_form(instance=usr)	
		context={'usr_form':user_form}
		return render(request,'user_form.html',context)



def user_block(request,id):
	usr=User.objects.get(id=id)
	if request.method=='POST':
		user_bk=usr_block(request.POST,instance=usr)
		if user_bk.is_valid():
			user_bk.save()
			return HttpResponseRedirect('/adminBlog/users')

	else:
		user_bk=usr_block(instance=usr)
		context={'usr_bk':user_bk}
		return render(request,'block.html',context)

def user_promote(request,id):
	usr=User.objects.get(id=id)
	if request.method=='POST':
		user_pm=usr_promote(request.POST,instance=usr)
		if user_pm.is_valid():
			user_pm.save()
			return HttpResponseRedirect('/adminBlog/users')

	else:
		user_pm=usr_promote(instance=usr)
		context={'usr_pm':user_pm}
		return render(request,'promote.html',context)

####################################################################
def forbidden(request):
	all_forbidden=forbidden_words.objects.all()
	context={'all_forbidden':all_forbidden}
	return render(request,'forbiddenwords_tables.html',context)


def forbidden_delete(request,id):
	word=forbidden_words.objects.get(id=id)
	word.delete()
	return HttpResponseRedirect('/adminBlog/forbidden')


def forbidden_add(request):
	if request.method=='POST':
		words_form=word_form(request.POST)
		if words_form.is_valid():
			words_form.save()
			return HttpResponseRedirect('/adminBlog/forbidden')


	else:
		words_form=word_form()
		context={'word_form':words_form}
		return render(request,'newbadword.html',context)

def forbidden_edit(request,id):
	word=forbidden_words.objects.get(id=id)
	if request.method=='POST':
		words_form=word_form(request.POST,instance=word)
		if words_form.is_valid():
			words_form.save()
			return HttpResponseRedirect('/adminBlog/forbidden')

	else:
		words_form=word_form(instance=word)	
		context={'word_form':words_form}
		return render(request,'newbadword.html',context)
#####################################################################################
def categories(request):
	categories=category.objects.all()
	context={'categories':categories}
	return render(request,'categories.html',context)


def cat_delete(request,id):
	cat=category.objects.get(id=id)
	cat.delete()
	return HttpResponseRedirect('/adminBlog/categories')





def category_add(request):
	if request.method=='POST':
		category_form=cat_form(request.POST)
		if category_form.is_valid():
			category_form.save()
			return HttpResponseRedirect('/adminBlog/categories')


	else:
		category_form=cat_form()
		context={'category_form':category_form}
		return render(request,'newcategory.html',context)	



def category_edit(request,id):
	cat=category.objects.get(id=id)
	if request.method=='POST':
		category_form=cat_form(request.POST,instance=cat)
		if category_form.is_valid():
			category_form.save()
			return HttpResponseRedirect('/adminBlog/categories')

	else:
		category_form=cat_form(instance=cat)	
		context={'category_form':category_form}
		return render(request,'newcategory.html',context)
#################################################################################
def side_categories(request):
	categories=category.objects.all()
	subs = subscribe.objects.filter(user_id=request.user).values_list('category_id',flat=True) 
	lst= []
	for cat in categories:
		print(cat.id)
		print(subs)
		if cat.id in subs:
			check = cat.id
		else:
			check =-1
		lst.append(check)
	print(lst)
	context={'categories':categories, 'lst':lst}

	return render(request,'side_bar.html',context)

def select(request,name):
	catt=category.objects.filter(name=name)
	for cat in catt:
		post=Post.objects.filter(category_id=cat)
		context={'post':post}
		return render(request,'select.html',context)
#def subscribe_fun(request,name):

def subscribes(request, category_id):
	print("ok")	
	try:
		cat = category.objects.get(id = category_id)
		subscribe.objects.create(user_id = request.user, category_id = cat)
	finally:
		return HttpResponseRedirect('/adminBlog/side_categories')


def unsubscribe(request,category_id):
	try:
		cat = category.objects.get(id = category_id)
		sub = subscribe.objects.get(user_id = request.user, category_id = cat)
		sub.delete()
	finally:
		return HttpResponseRedirect('/adminBlog/side_categories')


####################################################################################3

def body(request):
	context={
	'title':'home page',
	'posts':Post.objects.all(),
	}

	return render(request,'index.html',context)

	return render(request,'body.html',context)


#def createpost (request):
	#return render(request ,'post/createpost.html')

def post_detail(request,postid):
	post=get_object_or_404(Post,pk=postid)
	coms=Comment.objects.filter(post_name_id=postid)
	context={
	'post':post,'comment':coms
	}
	return render(request,'showpostdetails.html',context)

def like_post(request):
	post=get_object_or_404(post,id=request.post.get('postid'))	
	post.likes.add(request,user)
	return HttpResponseRedirect(post.get.absolute_url())


def createpost(request):
	if request.method=="POST":
	    form = postform(request.POST,request.FILES)
	    if form.is_valid():
	    	form.save()

	    	return HttpResponseRedirect('/adminBlog/all_posts')

	    	return HttpResponseRedirect("/adminBlog/body")

	else:
	    form = postform()
	    return render(request,'post.html', {'form': form})


def addcomment(request,postid):
	if request.method=="POST":		
		post=get_object_or_404(Post,pk=postid)
		user=request.user
		con=request.POST.get('message')
		obj=Comment(post_name=post,user_id=user,comment_content=con)
		obj.save()
		return HttpResponseRedirect("/adminBlog/showpostdetails/"+str(postid))

def addreplay(request,commentid):
	if request.method=="POST":		
		comment=get_object_or_404(Post,pk=commentid)
		user=request.user
		con=request.POST.get('message')
		obj=Comment(post_name=post,user_id=user,comment_content=con)
		obj.save()
		return HttpResponseRedirect("/adminBlog/showpostdetails/"+str(postid))
	

	#def createpost(request):
	#form = postform(request.POST or None) 

	#if form.is_valid():
		#form.save()
	#else:
		#form= postform()

	#context={
		#'from':form,
	#}
	#return render(request,'post/createpost.html',context)




#############################################
def all_posts(request):
	all_posts=Post.objects.all()
	context={'all_posts':all_posts}
	return  render(request,'posts.html',context)


def post_delete(request,id):
	post=Post.objects.get(id=id)
	post.delete()
	return HttpResponseRedirect('/adminBlog/all_posts')

# def post_add(request):
# 	if request.method=='POST':
# 		posts_form=post_form(request.POST)
# 		if posts_form.is_valid():
# 			posts_form.save()
# 			return HttpResponseRedirect('/adminBlodg/all_posts')


# 	else:
# 		posts_form=post_form()
# 		context={'posts_form':post_form}
# 		return render(request,'adminBlog/post.html',context)	

def post_edit(request,id):
	post=Post.objects.get(id=id)
	if request.method=='POST':
		posts_form=postform(request.POST,instance=post)
		if posts_form.is_valid():
			posts_form.save()
			return HttpResponseRedirect('/adminBlog/all_posts')

	else:
		posts_form=postform(instance=post)	
		context={'form':posts_form}
		return render(request,'post.html',context)


