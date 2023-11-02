from django import forms
from .models import Blog, Author, Word

class BlogFrom(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Blog
        fields =  ["title","topic","image","intro"]
        
        
class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ["word", "spelling", "definition", "mean", "example", "synonym", "level", "note"]