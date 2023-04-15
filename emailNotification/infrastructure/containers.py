from dependency_injector import containers, providers

from emailNotification.application.service.NotifySalesUseCase import NotifySalesUseCase


class Container(containers.DeclarativeContainer):
    notify_sales_use_case = providers.Factory(
        NotifySalesUseCase
    )
