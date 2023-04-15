from django.conf import settings
from django.core.mail import get_connection, EmailMessage

from emailNotification.application.dto.EmailDTO import EmailDTO
from emailNotification.application.repository.EmailSender import EmailSender


class DjangoEmailSender(EmailSender):

    def send(self, email_dto: EmailDTO):
        # TODO: This could be injected? But then, the rest of the implementations should have this configuration.
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            subject = email_dto.topic
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_dto.recipient]
            message = email_dto.description
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
