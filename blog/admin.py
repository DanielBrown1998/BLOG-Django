from django.contrib import admin

from blog.models import Tag, Category, Page, Post

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fileds = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name',),
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fileds = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name',),
    }
    

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published',
    list_display_links = 'title',
    search_fileds = 'id', 'title', 'slug', 'content',
    list_per_page = 50
    list_filter = 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',),
    }
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published', 
    list_display_links = 'title',
    search_fileds = 'id', 'title', 'slug', 'content', 'excerpt',
    list_per_page = 50
    list_filter = 'is_published',  'category',
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = 'created_at', 'updated_at', 'updated_by', 'created_by',
    prepopulated_fields = {
        "slug": ('title',),
    }

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        obj.save()
    
