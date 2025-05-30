from django.conf import settings

def vwo_account_id(request):
    return {
        "VWO_ACCOUNT_ID": getattr(settings, "VWO_ACCOUNT_ID", None),
        "VWO_USE_ASYNC": getattr(settings, "VWO_USE_ASYNC", False),
    }
