from django.shortcuts import render
from django.contrib.auth.models import User
from adminBlog.models import forbidden_words,category
#posts,
from django.http import HttpResponse,HttpResponseRedirect
from adminBlog.form import usr_form
from adminBlog.form import cat_form,word_form,usr_block
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





















