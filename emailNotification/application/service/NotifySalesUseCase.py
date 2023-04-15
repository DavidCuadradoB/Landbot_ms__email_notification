from emailNotification.application.command.NotifySalesCommand import NotifySalesCommand
from emailNotification.application.dto.EmailDTO import EmailDTO
from emailNotification.application.repository.EmailSender import EmailSender


class NotifySalesUseCase:

    def __init__(self, email_sender: EmailSender, sales_email):
        self.email_sender = email_sender
        self.sales_email = sales_email

    def execute(self, command: NotifySalesCommand):
        email_dto = EmailDTO(command.topic, command.description, self.sales_email)
        self.email_sender.send(email_dto)
