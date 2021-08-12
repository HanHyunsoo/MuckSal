from django.shortcuts import get_object_or_404, render,redirect
from django.utils import timezone
from .models import Post
from .forms import CreateForm,CommentForm
from django.http import request
from django.core.paginator import Paginator
# Create your views here.

def community(request):
    posts = Post.objects.all().order_by('-pk')
    page = request.GET.get('page')
    paginator = Paginator(posts, 5)
    blogs = paginator.get_page(page)
    return render(request,'community/cooktip.html',{'posts':posts ,'blogs':blogs})


def new(request):
    return render(request, 'community/new.html')

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.created_at = timezone.now()
            form.save()
            return redirect('community:community')
    else:
        form = CreateForm()
        return render(request, 'community/new.html',{'form':form})

def detail(request, id):
    post = get_object_or_404 (Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('community:detail',id)
    else:
        form = CommentForm()
        return render(request, "community/detail.html", {'post':post, 'form':form})