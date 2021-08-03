from django.shortcuts import render

# Create your views here.
def community(request):
    return render(request,'community/cooktip.html')

def layout(request):
    return render(request,'community/layout.html')