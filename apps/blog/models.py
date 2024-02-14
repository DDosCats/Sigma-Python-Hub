from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name = 'Title',max_length=225)
    content = models.TextField(verbose_name = 'Content')
    image = models.ImageField(verbose_name = 'Image',upload_to='post_images/')
    is_published = models.BooleanField(verbose_name= 'Published', default=False)
    likes = models.IntegerField(verbose_name= 'Likes',default=0)
    views = models.IntegerField(verbose_name='Views', default=0)
    created_at = models.DateTimeField(verbose_name = 'When created',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name = 'When updated', auto_now_add=True)
    
    class meta:
        verbose_name = 'Post'
        verbose_nam_plural = 'Posts'
        ordering = ['-created_at']
