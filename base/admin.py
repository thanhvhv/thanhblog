from django.contrib import admin
from .models import Blog, Topic, Author, Word, Client, WordCollection, Comment
# Register your models here.

admin.site.register(Blog)
admin.site.register(Topic)
admin.site.register(Author)
admin.site.register(Word)
admin.site.register(Client)
admin.site.register(WordCollection)
admin.site.register(Comment)