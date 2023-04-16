from dependency_injector.wiring import inject, Provide
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from emailNotification import Container
from emailNotification.application.service.NotifySalesUseCase import NotifySalesUseCase
from emailNotification.infrastructure.SalesConsumer import SalesConsumer


@inject
@csrf_exempt
def kafka_sales_init(
        request: HttpRequest,
        notify_sales_use_case: NotifySalesUseCase = Provide[Container.notify_sales_use_case],
        consumer: SalesConsumer = Provide[Container.sales_consumer]
):
    print("starting kafka for sales")
    consumer.consume()
    data = {
        'event': 'started'
    }
    return JsonResponse(data)
