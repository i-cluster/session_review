from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article
from .forms import AForm

# Create your views here.

def main(request):
    art = Article.objects.all()
    return render(request, 'main.html', {'hey': art})

def detail(request, p):
    art = get_object_or_404(Article, pk=p)
    return render(request, 'detail.html', {'art': art})

def new(request):
    if request.method == "POST":
        artform = AForm(request.POST, request.FILES)
        if artform.is_valid():
            art = artform.save(commit=False)
            art.author = request.user
            art.pub_date = timezone.now()
            art.save()
            return redirect('main')
    else:
        aform = AForm()
        return render(request, 'new.html', {'art': aform})

def edit(request, a):
    ar = get_object_or_404(Article, pk=a)
    if request.method == "POST":
        artform = AForm(request.POST, request.FILES, instance=ar)
        if artform.is_valid():
            art = artform.save(commit=False)
            art.author = request.user
            art.pub_date = timezone.now()
            art.save()
            return redirect('/'+str(ar.id))
    else:
        aform = AForm(instance=ar)
        return render(request, 'edit.html', {'art': aform})

def delete(request, w):
    art = get_object_or_404(Article, pk=w)
    art.delete()
    return redirect('main')