from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):

    #author = models.ForeignKey(user,related_name='author', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title