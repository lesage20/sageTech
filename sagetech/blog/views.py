from django.shortcuts import render, redirect
from .models import *
from website.models import NewsLetter
from account.forms import NewsletterForm, CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect




def single(request, pk):
    article = Article.objects.get(id=pk)
    latest = Article.objects.filter().order_by('-id')[:4]
    trending = Article.objects.filter()[:7]
    slider = Article.objects.filter()[:1]
    videos = Video.objects.filter()[:3]
    auteur = article.auteur
    auteur_articles = Article.objects.filter(auteur=auteur)
    
    
    comment_form = CommentForm()
        
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.article = article
            comment_form.save()
            return HttpResponseRedirect(request.path_info)


    
    datas= {
        'article': article,
        'trending':trending,
        'latest':latest,
        'videos': videos,
        'auteur':auteur,
        'auteur_articles':auteur_articles,
        'comment_form': comment_form,
        
        
    }
    return render(request, 'single-post.html', datas)


def tech(request):
    latests = Article.objects.filter().order_by('-id')[:3]
    articles = Article.objects.filter()[:6]
    populars = Article.objects.order_by('nb_comment')[:3]
    most_reads = Article.objects.order_by('nb_vue')[:4]
    
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
        
        'populars': populars,
        'latests':latests,
        'articles':articles,
        'most_reads':most_reads,
        'form': form
        
    }
    return render(request, 'tech-category.html', datas)

