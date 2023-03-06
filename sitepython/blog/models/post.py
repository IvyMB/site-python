from django.db import models
from django.contrib.auth.models import User

## Possíveis status dos posts do blog
STATUS = { (0, "Draft"), (1, "Publish")}
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices= STATUS, default= 0)

    ## Ordena os posts pela coluna 'created_on'
    class Meta:
      ordering = ['created_on']

    ## Representação em string da classe Post, retorna os titulos dos posts
    def __str__ (self):
      return self.title

