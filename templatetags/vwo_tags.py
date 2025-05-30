from django import template
from django.template.loader import render_to_string
from wagtail.models import Site
from ..models import VWOSettings

register = template.Library()

@register.simple_tag(takes_context=True)
def vwo_smartcode(context):
    """
    Template tag to insert VWO SmartCode in the header.
    Usage: {% load vwo_tags %}{% vwo_smartcode %}
    """
    try:
        request = context.get('request')
        if request:
            site = Site.find_for_request(request)
            vwo_settings = VWOSettings.for_site(site)
            
            if vwo_settings and vwo_settings.vwo_account_id:
                return render_to_string('wagtail_vwo_smartcode/smartcode.html', {
                    'vwo_account_id': vwo_settings.vwo_account_id,
                    'async_load': vwo_settings.async_load,
                    'settings_tolerance': vwo_settings.settings_tolerance,
                })
    except Exception:
        return ''
    return '' 
