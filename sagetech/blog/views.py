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
    auteur = article.auteur
    auteur_articles = Article.objects.filter(auteur=auteur)
    tags = Tag.objects.filter(tag_article=article)
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.article = article
            comment_form.save()
            return HttpResponseRedirect(request.path_info)
    
    user = request.user
    
    if request.method==  'POST':
        article_id = request.POST.get('article_id')
        article_obj = Article.objects.get(id=article_id)
    
        if user in article_obj.liked.all():
            article_obj.liked.remove(user)
        else:
            article_obj.liked.add(user)
        
        like, created = Like.objects.get_or_create(user=user, article_id=article_id)
        
        if not created:
            if like.value== 'Like':
                like.value='Unlike'
            else:
                like.value='Like'  
            
        
        like.save() 
        return redirect(request.path_info)


    
    datas= {
        'article': article,
        'trending':trending,
        'latest':latest,
        
        'auteur':auteur,
        'auteur_articles':auteur_articles,
        'comment_form': comment_form,
        'tags': tags
        
        
    }
    return render(request, 'single-post.html', datas)

# def like_view(request):
         
    

#     return render(request, 'single-post.html')

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
            return redirect(request.path_info)

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

