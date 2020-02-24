from django.shortcuts import render
from django.contrib.auth.models import User
from adminBlog.models import forbidden_words,category
#posts,
from django.http import HttpResponse,HttpResponseRedirect
from adminBlog.form import usr_form
from adminBlog.form import cat_form,word_form,usr_block,usr_promote
from django.contrib.auth.backends import BaseBackend


# Create your views here.
def users(request):
	all_users=User.objects.all()
	context={'all_users':all_users}
	return render(request,'users_tables.html',context)

def user_add(request):
	if request.method=='POST':
		user_form=usr_form(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect('/adminBlog/users')


	else:
		user_form=usr_form()
		context={'usr_form':user_form}
		return render(request,'user_form.html',context)	

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
	context={'categories':categories}
	return render(request,'side_bar.html',context)







