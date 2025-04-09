from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User
import math
import re
from django.utils.html import strip_tags
# Create your models here.
class BlogCategory(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Blog(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    content = CKEditor5Field(config_name='extends')
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, related_name='blogs', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_read_time(self):
        text = strip_tags(self.content)  # Removes HTML tags
        words = re.findall(r'\w+', text)  # Find all words
        word_count = len(words)
        read_time_minutes = math.ceil(word_count / 200)  # Assuming 200 WPM
        return read_time_minutes
    
    @property
    def read_time(self):
        return self.calculate_read_time()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title