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

class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    inlines = MenuLinkInline,
    
    
    # Se o usuário já tiver criado um setup não poderá alterá-lo
    def has_add_permission(self, request):
        if not SiteSetup.objects.all().exists():        
            return True
        return False
    
