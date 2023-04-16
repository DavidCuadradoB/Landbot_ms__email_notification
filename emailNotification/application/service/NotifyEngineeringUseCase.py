from emailNotification.application.command.NotifyEngineeringCommand import NotifyEngineeringCommand
from emailNotification.application.dto.EmailDTO import EmailDTO
from emailNotification.application.repository.EmailSender import EmailSender


class NotifyEngineeringUseCase:

    def __init__(self, email_sender: EmailSender, sales_email):
        self.email_sender = email_sender
        self.sales_email = sales_email

    def execute(self, command: NotifyEngineeringCommand):
        email_dto = EmailDTO(command.topic, command.description, self.sales_email)
        self.email_sender.send(email_dto)
