from django.http import HttpRequest, JsonResponse
from django.shortcuts import render


# TODO: This view should not exist. This should be a subscriber for the event type notification.
# Todo: The topic will be: Sales, Pricing or the type of event. If this team (sales, pricing...) want to be notified
# Todo: By mail, the only thing that they have to do is create a new subscriber here.
def sales_email_notification(
        request: HttpRequest
):
    data = {
        'event': 'lala'
    }
    return JsonResponse(data)
