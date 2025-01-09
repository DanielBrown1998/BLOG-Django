from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup

# Register your models here.
@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'url_or_path', 'new_tab')
    list_display_links = ('id', 'text')
    list_filter = ('new_tab',)
    search_fields = ('text', 'url_or_path')
    ordering = ('id',)

@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'show_header', 'show_search', 'show_menu', 'show_description', 'show_pagination', 'show_footer')
    list_display_links = ('id', 'title')
    list_filter = ('show_header', 'show_search', 'show_menu', 'show_description', 'show_pagination', 'show_footer')
    search_fields = ('title', 'description')
    ordering = ('id',)
    
