from abc import ABC, abstractmethod

from emailNotification.application.dto.EmailDTO import EmailDTO


class EmailSender(ABC):
    @abstractmethod
    def send(self, email_dto: EmailDTO):
        pass
