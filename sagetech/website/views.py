from django.shortcuts import render
from blog.models import Article
from account.forms import NewsletterForm
from .models import NewsLetter
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    articles = Article.objects.all()
    latests = Article.objects.order_by('-date')[:4]
    populars = Article.objects.order_by('nb_vue')[:3]
    one_article = Article.objects.filter()[:4]
    form = NewsletterForm()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        form = NewsletterForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

        else:
            messages.warning(request, 'veuillez entrer ue addresse email valide svp')
        
    
    datas= {
        'articles': articles,
        'latests': latests,
        'populars':populars,
        'one_article':one_article,
        'form': form

    }
    return render(request, 'index.html', datas)

def contact(request):
    articles = Article.objects.all()
    latests = Article.objects.order_by('-date')[:4]
    populars = Article.objects.order_by('nb_comment')[:3]
    
    form = NewsletterForm()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        form = NewsletterForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, 'veuillez entrer ue addresse email valide svp')
        
        
        
    
    datas= {
        'articles': articles,
        'latests': latests,
        'populars':populars,
        'form': form
    }
    return render(request, 'contact.html', datas)


