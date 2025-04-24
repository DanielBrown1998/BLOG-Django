from django.db import models
from utils import rands
from django.contrib.auth.models import User

from utils.images import resize_image
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

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True, 
        default='',
        null = False,
        blank=True,
        max_length=255,
    )
    excerpt = models.CharField(max_length=255)
    is_published = models.BooleanField(
        default=False,
        help_text=(
            "Este campo precisara estar marcado "
            "para o post ser exibido publicamente"
        )
    )
    content = models.TextField()
    cover = models.ImageField(
        upload_to='posts/%Y/%m/',
        default='',
        blank=True,
    )
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text=(
            "Esta imagem sera exibida no conteudo do post "
            "caso esteja marcada"
        )
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=(
            "Esta data sera definida automaticamente "
            "quando o post for criado"
        )
    )
    #user.post_created_by.<QuerySet>[all, filter, get]
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
        related_name='post_created_by'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=(
            "Esta data sera definida automaticamente "
            "quando o post for atualizado"
        )
    )
    #user.post_updated_by.<QuerySet>[all, filter, get]
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
        related_name='post_updated_by'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        default=None,
        related_name='posts'
    )

    
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = rands.new_slugfy(self.title)
        current_name = self.cover.name # antes de ser salvo na base de dados
        save_super = super().save(*args, **kwargs) # salvando na base de dados
        # depois de ser salvo na base de dados
        name_changed = False
        if self.cover:
            name_changed = current_name != self.cover.name
        if name_changed:
            resize_image(self.cover, 900)
        return save_super
