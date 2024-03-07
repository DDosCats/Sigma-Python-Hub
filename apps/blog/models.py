import os
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.files import File

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


def generate_filename(instance, filename):

    ext = filename.split('.')[-1]

    filename = f'{uuid.uuid4()}.{ext}'
    return f'post_images/{filename}'



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='posts', null=True, default=None)
    
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(verbose_name='Малюнок', upload_to=generate_filename)
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(820, 440)],
                                      format='JPEG',
                                      options={'quality': 60})
    dislike = models.ManyToManyField(User, related_name='Diz_like_POST', blank=True)    
    is_published = models.BooleanField(verbose_name='Опубліковано', default=False, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    views = models.IntegerField(verbose_name='Перегляди', default=0, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    
    def __str__(self):
        return f'{self.title} - {self.created_at} - {self.is_published}'
    
    class Meta: # Це потрібно для відображення моделі в адмінці
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        ordering = ['-created_at']
        
        
          
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return 'https://via.placeholder.com/240x240.jpg'
    
  
    

        
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
