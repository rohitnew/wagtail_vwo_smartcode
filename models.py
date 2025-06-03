from django.db import models
from django.core.validators import MinValueValidator
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, HelpPanel

@register_setting
class VWOSettings(BaseSiteSetting):
    LOADING_CHOICES = [
        ('async', 'Asynchronous'),
        ('sync', 'Synchronous'),
    ]

    vwo_account_id = models.IntegerField(
        verbose_name="VWO Account ID",
        help_text='You can find this in your VWO dashboard under Account Settings',
        null=False,
        blank=False,
        default=1,
        validators=[MinValueValidator(1)]
    )
    
    async_load = models.CharField(
        verbose_name="SmartCode Loading Type",
        max_length=5,
        choices=LOADING_CHOICES,
        default='async',
        help_text='Choose how the VWO tracking script loads on your site. Asynchronous is recommended for faster page loads.'
    )

    settings_tolerance = models.IntegerField(
        verbose_name="Settings Tolerance (ms)",
        default=2500,
        validators=[MinValueValidator(2500)],
        help_text='Maximum wait time for VWO settings to be applied. Must be 2500ms or higher.'
    )

    class Meta:
        verbose_name = 'VWO Settings'

    panels = [
        HelpPanel(
                template='wagtail_vwo_smartcode/help_panel.html',
                classname="vwo-help-panel"
            ),
        MultiFieldPanel(
            [   
                FieldPanel('vwo_account_id'),
                FieldPanel('async_load'),
                FieldPanel('settings_tolerance'),
            ],
            heading="VWO Configuration",
            classname="collapsible"
        ),
        HelpPanel(
                    template='wagtail_vwo_smartcode/help_panel_report.html',
                    classname="vwo-help-panel"
        ),
    ] 
