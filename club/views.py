from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
from .models import *

def home(request):
    posts = FreePost.objects.all()
    return render(request,'index.html', {'posts': posts})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        userid = request.POST['username']
        userpw = request.POST['password']

        user = auth.authenticate(request, username=userid, password=userpw)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    else:
        userid = request.POST['username']
        userpw = request.POST['password']
        new_user = User.objects.create_user(username=userid, password=userpw)
        auth.login(request, new_user)
        return redirect('home')

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        post = FreePost()  
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.people = request.POST['people']
        post.save()
        return redirect('detail', post.id)

def detail(request, id):
    freepost = get_object_or_404(FreePost, pk = id)
    return render(request, 'detail.html', {'freepost': freepost})

def edit(request, id):
    edit_freepost = FreePost.objects.get(id=id)
    return render(request, 'edit.html', {'freepost':edit_freepost})

def update(request, id):
    update_freepost = FreePost.objects.get(id=id)
    update_freepost.title = request.POST['title']
    update_freepost.body = request.POST['body']
    update_freepost.people = request.POST['people']
    update_freepost.save()
    return redirect('detail', update_freepost.id)

def delete(request, id):
    delete_freepost = FreePost.objects.get(id = id)
    delete_freepost.delete()
    return redirect('home')
    
def comment(request, freepost_id):
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.post = get_object_or_404(FreePost, pk=freepost_id)
        new_comment.comment = request.POST['comment']
        new_comment.time = timezone.now()
        new_comment.save()
    return redirect('detail', freepost_id)