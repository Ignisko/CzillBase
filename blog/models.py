from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Fixed: Use DateTimeField
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # Fixed: Use Post (singular)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
