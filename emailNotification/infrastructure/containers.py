from dependency_injector import containers, providers

from emailNotification.application.service.NotifySalesUseCase import NotifySalesUseCase
from emailNotification.infrastructure.Salesconsumer import Salesconsumer
from emailNotification.infrastructure.repository.DjangoEmailSender import DjangoEmailSender


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    email_sender = providers.Factory(
        DjangoEmailSender
    )

    notify_sales_use_case = providers.Factory(
        NotifySalesUseCase,
        email_sender,
        config.SALES_EMAIL
    )

    consumer = providers.Factory(
        Salesconsumer,
        notify_sales_use_case
    )
