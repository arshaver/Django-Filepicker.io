from django.conf import settings

def settings_context_processor(request):
    settings_dict = {
        'FILEPICKER_API_KEY': settings.FILEPICKER_API_KEY,
    }
    return settings_dict