from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    
class Song(models.Model):
  title = models.CharField(max_length=100)
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  file = models.FileField(upload_to='songs/')