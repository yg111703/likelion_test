from django.db import models

# Create your models here.

class FreePost(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=100)
    people = models.IntegerField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(FreePost, on_delete=models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment