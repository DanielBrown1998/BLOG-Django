from django.db import models
from utils import rands
# Create your models here.
class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = rands.new_slugfy(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = rands.new_slugfy(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True, 
        default='',
        null = False,
        blank=True,
        max_length=255,
    )
    is_published= models.BooleanField(default=False)
    content = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = rands.new_slugfy(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
