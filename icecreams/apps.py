from django.apps import AppConfig
from django.core.signals import setting_changed


class IcecreamsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'icecreams'

    def ready(self):
        from icecreams.signals import notify_admin_when_empty
        setting_changed.connect(notify_admin_when_empty)