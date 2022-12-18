from django.db import models
from django.utils.text import slugify


class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs')
    description = models.TextField()
    entry = models.TextField()
    video = models.URLField(null=True)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)
    isActive = models.BooleanField()
    isHome = models.BooleanField()

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class FoodBlog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs')
    description = models.TextField()
    entry = models.TextField()
    video = models.URLField(null=True)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)
    isActive = models.BooleanField()
    isHome = models.BooleanField()

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class UserInfo(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.TextField()
    isActive = models.BooleanField()


class Videos(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    url = models.TextField()
    imageUrl = models.TextField()
    description = models.TextField()
    isActive = models.BooleanField()


class About(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
