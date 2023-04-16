from dependency_injector import containers, providers

from emailNotification.application.service.NotifyEngineeringUseCase import NotifyEngineeringUseCase
from emailNotification.application.service.NotifySalesUseCase import NotifySalesUseCase
from emailNotification.infrastructure.SalesConsumer import SalesConsumer
from emailNotification.infrastructure.engineeringConsumer import EngineeringConsumer
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

    notify_engineering_use_case = providers.Factory(
        NotifyEngineeringUseCase,
        email_sender,
        config.ENGINEERING_EMAIL
    )

    sales_consumer = providers.Factory(
        SalesConsumer,
        notify_sales_use_case
    )

    engineering_consumer = providers.Factory(
        EngineeringConsumer,
        notify_engineering_use_case
    )
