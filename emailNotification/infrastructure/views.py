import json

from dependency_injector.wiring import inject, Provide
from django.http import HttpRequest, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from emailNotification import Container
from emailNotification.application.command.NotifySalesCommand import NotifySalesCommand
from emailNotification.application.service.NotifySalesUseCase import NotifySalesUseCase
from emailNotification.infrastructure.SalesConsumer import SalesConsumer


# TODO: This view should not exist. This should be a subscriber for the event type notification.
# Todo: The topic will be: Sales, Pricing or the type of event. If this team (sales, pricing...) want to be notified
# Todo: By mail, the only thing that they have to do is create a new subscriber here.
@inject
@csrf_exempt
def sales_email_notification(
        request: HttpRequest,
        notify_sales_use_case: NotifySalesUseCase = Provide[Container.notify_sales_use_case],
        consumer: SalesConsumer = Provide[Container.sales_consumer]
):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        try:
            command = NotifySalesCommand(body['topic'], body['description'])
        except KeyError as e:
            return HttpResponseBadRequest('The body should contain a topic and a description')

        notify_sales_use_case.execute(command)
        data = {
            'event': 'lala'
        }
        return JsonResponse(data)
