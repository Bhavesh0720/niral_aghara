from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Cources(models.Model):
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    mode = models.CharField(max_length=50)
    video_url = models.TextField()
    playlist_url = models.TextField()

    def __str__(self):
        return self.title
    

class PlayLists(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.TextField()
    playlist_url = models.TextField()

    def __str__(self):
        return self.title
    

class MostPopular(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.TextField()

    def __str__(self):
        return self.title
