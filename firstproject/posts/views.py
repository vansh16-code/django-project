from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from. import forms
from django.contrib import messages
# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html', {'posts':posts})


def post_page(request, slug):
     post = Post.objects.get (slug=slug)
     return render(request,'posts/post_page.html', {'post':post})


@login_required(login_url="/users/login/")
def post_new(request):
     if request.method == 'POST':
          form = forms.CreatePost(request.POST,request.FILES)
          if form.is_valid():
               newpost = form.save(commit=False)
               newpost.author = request.user
               newpost.save()
               return redirect('posts:list')
     else:
          form = forms.CreatePost()
     return render(request, 'posts/post_new.html',{'form':form})
 