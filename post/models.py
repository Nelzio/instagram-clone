from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    foto = models.ImageField(null=True, blank=True)
    legenda = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True)
    utilizador = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.legenda
    

class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    