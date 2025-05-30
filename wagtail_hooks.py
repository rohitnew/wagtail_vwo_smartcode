from wagtail import hooks
from wagtail.models import Site
from django.conf import settings
from django.utils.html import format_html
from django.template.loader import render_to_string
from .models import VWOSettings

@hooks.register('before_serve_page')
def inject_vwo_smartcode(page, request, serve_args, serve_kwargs):
    """Inject VWO SmartCode into the page."""
    try:
        # First try to get settings from admin
        site = Site.find_for_request(request)
        vwo_settings = VWOSettings.for_site(site)
        
        if vwo_settings and vwo_settings.vwo_account_id:
            account_id = vwo_settings.vwo_account_id
            async_load = vwo_settings.async_load
        else:
            # Fall back to Django settings
            account_id = getattr(settings, 'VWO_ACCOUNT_ID', None)
            async_load = getattr(settings, 'VWO_ASYNC_LOAD', True)
        
        if account_id:
            html = render_to_string('wagtail_vwo_smartcode/smartcode.html', {
                'vwo_account_id': account_id,
                'async_load': async_load,
            })
            return format_html(html)
    except Exception:
        return None 
