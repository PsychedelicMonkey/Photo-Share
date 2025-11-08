from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} by {self.user.username}'


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, related_name='photos', null=True, blank=True)
    image = models.ImageField(upload_to='gallery/')
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name if self.name else self.image.name

    def get_absolute_url(self):
        return reverse('photo-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        max_size = (1200, 800)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        img.save(self.image.path)

