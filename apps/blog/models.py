from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name = 'Title',max_length=225)
    content = models.TextField(verbose_name = 'Content')
    image = models.ImageField(verbose_name = 'Image',upload_to='post_images/')
    is_published = models.BooleanField(verbose_name= 'Published', default=False)
    dislike = models.IntegerField(verbose_name='Diz_like', default=0, blank=True)
    likes = models.IntegerField(verbose_name='Вподобайки', default=0, blank=True)
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
    author = models.CharField(verbose_name='Author', max_length=50)
    content = models.TextField(verbose_name='Контент')
    dislike = models.IntegerField(verbose_name='Диз_Лайк', default=0, blank=True)
    likes = models.IntegerField(verbose_name='Вподобайки', default=0, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    
    def __str__(self):
        return f'{self.author} - {self.created_at}'
    
    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['created_at']