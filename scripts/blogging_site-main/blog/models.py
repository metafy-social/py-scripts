from django.db import models
from django.template.response import ContentNotRenderedError
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    header_image=models.ImageField(null=True,blank=True,upload_to="database_image")
    content=RichTextField(blank=True,null=True)
    # content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='blog_posts')


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.post.pk)])
        
