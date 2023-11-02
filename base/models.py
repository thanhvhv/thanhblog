from django.db import models
from datetime import datetime   
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/', default=None)
    dob = models.DateField(default=None)
    follower = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    join_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/', default=None)
    dob = models.DateField(default=None)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/')
    intro = models.CharField(max_length=500)
    content = models.TextField()
    appraisal = models.FloatField(default=0)
    views = models.IntegerField(default=0)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    created = models.DateField(auto_now_add=True)
    
class Word(models.Model):
    blog = models.ManyToManyField(Blog, related_name="words")
    word = models.CharField(max_length=50, blank=True)
    spelling = models.CharField(max_length=50, blank=True)
    definition = models.TextField(blank=True)
    mean = models.TextField(blank=True)
    example = models.TextField(blank=True)
    synonym = models.CharField(max_length=100, blank=True)
    LEVEL_CHOICES = (
        ("A1", "A1"),
        ("A2", "A2"),
        ("B1", "B1"),
        ("B2", "B2"),
        ("C1", "C1"),
        ("C2", "C2"),
    )
    level = models.CharField(max_length=5, choices=LEVEL_CHOICES, default=None)
    note = models.TextField(blank=True, default=None)
    
    def __str__(self):
        return self.word
    
class WordCollection(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    LEVEL_CHOICES = (
        ("Easy","Easy"),
        ("Medium","Medium"),
        ("Hard","Hard")
    )
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default="Medium")
    
    
    
    
        