from audioop import reverse
from distutils.command.upload import upload
from tabnanny import verbose
from django import views
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Cotegory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('cotegory', kwargs={"slug":self.slug})

    def save(self,*args, **kwargs):
        self.slug = self.title
        super().save(*args, *kwargs)

class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('tag', kwargs={"slug":self.slug})

    def save(self,*args, **kwargs):
        self.slug = self.title
        super().save(*args, *kwargs)

def upload_post(filename):
    return f'photo/%y/%m/%d {filename}'

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    content = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='upload_post', blank=True, null=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self) -> str:
        return reverse('post', kwargs={"slug":self.slug})

    def save(self,*args, **kwargs):
        self.slug = self.title
        super().save(*args, *kwargs)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'