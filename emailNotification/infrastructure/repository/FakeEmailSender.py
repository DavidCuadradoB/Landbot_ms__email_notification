from emailNotification.application.dto.EmailDTO import EmailDTO
from emailNotification.application.repository.EmailSender import EmailSender


class FakeEmailSender(EmailSender):

    def send(self, email_dto: EmailDTO):
        print("Sending event with topic %s and description %s...."
              % (email_dto.topic, email_dto.description))
        print("Email sent")
