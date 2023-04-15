from dependency_injector import containers, providers

from emailNotification.application.service.NotifySalesUseCase import NotifySalesUseCase
from emailNotification.infrastructure.repository.FakeEmailSender import FakeEmailSender


class Container(containers.DeclarativeContainer):
    email_sender = providers.Factory(
        FakeEmailSender
    )

    notify_sales_use_case = providers.Factory(
        NotifySalesUseCase,
        email_sender
    )
