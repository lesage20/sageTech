from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from account.models import Profile
# Create your models here.


# category
# Tag

# video 
# auteur 
class Auteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='images/auteur-icon', null=True )

    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Auteur'
        verbose_name_plural = 'Auteurs'

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    nom = models.CharField(max_length=50, null=True)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nom




class Category(models.Model):
    nom = models.CharField(max_length=50, null=True)
    nombre_article = models.PositiveIntegerField(null=True)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom

class Article(models.Model):
    # article(image, titre, auteur, nb_com, nb_vue, date, description)
    titre = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/articles', null=True)
    image2 = models.ImageField(upload_to='images/single_example', null=True)
    image3 = models.ImageField(upload_to='images/single_example2', null=True)
    
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='auteur_article', null=True)
    tag = models.ManyToManyField(Tag, related_name='tag_aticle')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_article', null=True)
    description = models.TextField(null=True)
    nb_comment = models.PositiveIntegerField(null=True)
    nb_vue = models.PositiveIntegerField(null=True)
    date = models.DateField(null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        
        return reverse('single', kwargs={'pk': self.pk})
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')
    

class Video(models.Model):
    titre = models.CharField(max_length=200, null=True)
    lien = models.URLField(null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auteur_video', null=True)
    description = models.TextField(null=True)
    nb_comment = models.PositiveIntegerField(null=True)
    date = models.DateField(null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.titre


class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_comment', null=True)
    message = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', null=True)

    
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return self.user.username
    