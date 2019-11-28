from django.db import models
from django import forms
from django.core import validators

class Posts(models.Model):
    title = models.CharField(#validators = [validators.validate_email],
        max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager

    def __str__(self):
        return self.title

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','content']
