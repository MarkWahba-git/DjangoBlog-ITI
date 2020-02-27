from django.shortcuts import render,get_object_or_404
from adminBlog.models import forbidden_words,category,Post
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .forms import UserRegisterationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from adminBlog.models import Post, Comment ,Tags ,reply,Likes
from djangoBlog.forms import postform,commentform
from adminBlog.models import Post, Comment ,Tags ,reply,subscribe

def signup(request):
    # if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/djangoBlog/indeex')
        else:
        # form = UserRegisterationForm()
            return render(request, 'signup.html',{'form': form})

def home(request): 
	return render(request, 'home.html')

def about(request): 
	return render(request, 'about.html')


def contact(request): 
	return render(request, 'contact.html')    


def login_view(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("/djangoBlog/indeex")
	
    else:
        form= AuthenticationForm()
    return render(request,'login_form.html',{'form':form})

def confirm_login_allowed(self, user):
        
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )


def body(request):

    
    categories=category.objects.all()
    
    # subs = subscribe.objects.filter(user_id=request.user).values_list('category_id',flat=True) 
    lst= []
    for cat in categories:
        print(cat.id)
        # print(subs)
        # if cat.id in subs:
            # check = cat.id
        # else:
            # check =-1
        # lst.append(check)
    # print(lst)
    context={
    # 'title':'home page',
    'posts':Post.objects.all(),
    'categories':categories, 'lst':lst
    }
    return render(request,'indeex.html',context)



def post_detail(request,postid):
    post=get_object_or_404(Post,pk=postid)
    coms=Comment.objects.filter(post_name_id=postid)


    likeCount = Likes.objects.filter(postID_id=postid, isLiked=False).count()
    if likeCount==10:
        Post.objects.get(id=postid).delete()
        return HttpResponseRedirect('/djangoBlog/indeex')

    context={
    'post':post,'comment':coms
    }
    return render(request,'showpost.html',context)

def like_post(request):
    post=get_object_or_404(post,id=request.post.get('postid'))  
    post.likes.add(request,user)
    return HttpResponseRedirect(post.get.absolute_url())


def addcomment(request,postid):
    if request.method=="POST":      
        post=get_object_or_404(Post,pk=postid)
        user=request.user
        con=request.POST.get('message')
        obj=Comment(post_name=post,user_id=user,comment_content=con)
        obj.save()
        return HttpResponseRedirect("/djangoBlog/showpost/"+str(postid))

def addreplay(request,commentid):
    if request.method=="POST":      
        comment=get_object_or_404(Post,pk=commentid)
        user=request.user
        con=request.POST.get('message')
        obj=Comment(post_name=post,user_id=user,comment_content=con)
        obj.save()

        return HttpResponseRedirect("/djangoBlog/showpost/"+str(postid))

        return HttpResponseRedirect("/adminBlog/showpostdetails/"+str(postid))
#############################################################################
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

	return render(request,'indeex.html',context)

def select(request,name):
	catt=category.objects.filter(name=name)
	for cat in catt:
		post=Post.objects.filter(category_id=cat)
		context={'post':post}
		return render(request,'indexcategory.html',context)
#def subscribe_fun(request,name):

def subscribes(request, category_id):
	print("ok")	
	try:
		cat = category.objects.get(id = category_id)
		subscribe.objects.create(user_id = request.user, category_id = cat)
	finally:
		return HttpResponseRedirect('/djangoBlog/indeex')


def unsubscribe(request,category_id):
	try:
		cat = category.objects.get(id = category_id)
		sub = subscribe.objects.get(user_id = request.user, category_id = cat)
		sub.delete()
	finally:
		return HttpResponseRedirect('/djangoBlog/indeex')

		return HttpResponseRedirect('/adminBlog/side_categories')

def liked(request,id):
    post = Post.objects.get(id=id)
    # print('idddddddddddddddd='+postID)
    # print('idddddddddddddddd='+postTitle)


    currentUser = request.user.id
    try:
        like, created = Likes.objects.get_or_create(
            postID_id=id, userID_id=currentUser, isLiked=True)
        Likes.objects.filter(
            postID_id=id, userID_id=currentUser, isLiked=False).delete()
            
        
    except Exception as e:
        pass
    finally:
        likesDic = {'post': post, 'user': currentUser}
        return HttpResponseRedirect('/djangoBlog/showpost/'+id)

        


def disliked(request,id):
    post = Post.objects.get(id=id)
    print('dislikeeeeeeeeed')
    currentUser = request.user.id
    try:
        dislike, created = Likes.objects.get_or_create(
            postID_id=id, userID_id=currentUser, isLiked=False)
        Likes.objects.filter(
            postID_id=id, userID_id=currentUser, isLiked=True).delete()

    except Exception as e:
        pass
    finally:
        likesDic = {'post': post, 'user': currentUser}
        return HttpResponseRedirect('/djangoBlog/showpost/'+id)



