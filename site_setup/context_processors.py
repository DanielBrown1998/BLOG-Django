def general_setup(request):
    from site_setup.models import SiteSetup
    setup = SiteSetup.objects.all().first()
    return {
        'site_setup': setup,
    }