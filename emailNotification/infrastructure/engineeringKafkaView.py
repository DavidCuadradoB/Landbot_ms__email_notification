from dependency_injector.wiring import inject, Provide
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from emailNotification import Container
from emailNotification.application.service.NotifyEngineeringUseCase import NotifyEngineeringUseCase
from emailNotification.infrastructure.engineeringConsumer import EngineeringConsumer


# TODO: This view should not exist. This should be a subscriber for the event type notification.
# Todo: The topic will be: Sales, Pricing or the type of event. If this team (sales, pricing...) want to be notified
# Todo: By mail, the only thing that they have to do is create a new subscriber here.
@inject
@csrf_exempt
def kafka_engineering_init(
        request: HttpRequest,
        notify_engineering_use_case: NotifyEngineeringUseCase = Provide[Container.notify_engineering_use_case],
        consumer: EngineeringConsumer = Provide[Container.engineering_consumer]
):
    print("starting kafka for engineering")
    consumer.consume()
    data = {
        'event': 'started'
    }
    return JsonResponse(data)
