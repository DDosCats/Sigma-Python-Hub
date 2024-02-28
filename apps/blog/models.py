from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='posts', null=True, default=None)
    
    title = models.CharField(verbose_name = 'Title',max_length=225)
    content = models.TextField(verbose_name = 'Content')
    image = models.ImageField(verbose_name = 'Image',upload_to='post_images/')
    is_published = models.BooleanField(verbose_name= 'Published', default=False)
    dislike = models.ManyToManyField(User, related_name='Diz_like_POST', blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    views = models.IntegerField(verbose_name='Views', default=0)
    created_at = models.DateTimeField(verbose_name = 'When created',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name = 'When updated', auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} - {self.created_at} - {self.is_published}'
    
    class meta:
        verbose_name = 'Post'
        verbose_nam_plural = 'Posts'
        ordering = ['-created_at']
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='comments', null=True, default=None)
    content = models.TextField(verbose_name='Контент')
    dislike = models.ManyToManyField(User, related_name='Diz_like_COMMENT', blank=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    
    def __str__(self):
        return f'{self.author} - {self.created_at}'
    
    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['created_at']
