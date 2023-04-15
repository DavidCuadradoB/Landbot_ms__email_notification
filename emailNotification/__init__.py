from Landbot_ms__email_notification import settings
from emailNotification.infrastructure.containers import Container

container = Container()
container.config.from_dict(settings.__dict__)
