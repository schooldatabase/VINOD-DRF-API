from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
# Create your models here.
from django.utils.text import slugify
import uuid
import datetime

# class BaseModel(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

# class Post(BaseModel):
#     name = models.CharField(max_length=100,blank=True, null=True)
#     slug = models.SlugField(blank=True, null=True)
    
class Artist(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

class Album(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    artists = models.ManyToManyField(Artist, related_name='albums')

class Song(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    artists = models.ManyToManyField(Artist, related_name='songs')
    albums = models.ManyToManyField(Album, related_name='songs')














# class Song(models.Model):
#     title = models.CharField(max_length=100)
#     artist = models.CharField(max_length=100)
#     duration = models.DurationField()
#     # audio_file = models.FileField(upload_to='audio/', validators=[validate_audio_extension, validate_audio_size])
#     # Additional fields for the Music app
#     album = models.CharField(max_length=100)
#     genre = models.CharField(max_length=50)
#     release_date = models.DateField()

#     def __str__(self):
#         return self.title
    
# # Library 
# class LikedSong(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     song = models.ForeignKey(Song, on_delete=models.CASCADE)

    
# class Album(models.Model):
#     title = models.CharField(max_length=100)
#     artist = models.CharField(max_length=100)
#     cover_image = models.ImageField(upload_to='album_covers/')
#     release_date = models.DateField()
#     genre = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title