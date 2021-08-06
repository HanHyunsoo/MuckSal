from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
from .forms import CreateForm
# Create your views here.

def community(request):
    posts = Post.objects.all()
    return render(request,'community/cooktip.html',{'posts':posts})

def detail(request):
    posts = Post.objects.all()
    return render(request, 'community/detail.html')

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
