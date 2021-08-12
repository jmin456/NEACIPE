from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from itertools import combinations

# Create your views here.

def result(request):
    checks=request.POST.getlist('checks[]')
    blogs=Blog.objects.all()
    results = []
    for blog in blogs:
        blog.checks=blog.checks.replace(" ",'').split(',')
        counter = 0
        for i in blog.checks:
            if i in checks:
                counter += 1
                if counter == len(blog.checks):
                    results.append(blog.title)
    length = len(results)
    checks = str(checks).rstrip(']').lstrip('[').replace("'",'')
    for blog in blogs:
        blog.checks = str(blog.checks).rstrip(']').lstrip('[').replace("'",'')
    return render(request, "result.html",{'blogs':blogs,'checks':checks,'results':results,'length':length})

def list(request):
    blogs = Blog.objects.all()
    return render(request, 'list.html', {'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    # form = BlogForm()
    return render(request, 'new.html')


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.image = request.FILES['image']
    new_blog.checks = str(request.POST.getlist('checks[]')).lstrip('[').rstrip(']').replace("'","")
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('list')