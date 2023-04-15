from django.apps import AppConfig

from emailNotification import container


class EmailNotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emailNotification'

    def ready(self):
        container.wire(modules=[".views"])
