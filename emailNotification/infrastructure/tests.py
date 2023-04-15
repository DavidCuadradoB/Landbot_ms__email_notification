import http
import mockito
from django.test import TestCase
from django.urls import reverse
from mockito import when

from emailNotification import container
from emailNotification.application.command.NotifySalesCommand import NotifySalesCommand
from emailNotification.application.service.NotifySalesUseCase import NotifySalesUseCase


# Create your tests here.
class SalesEmailNotificationViewTest(TestCase):
    def test_sales_email_notification_should_call_notify_sales_use_case(self):
        a_topic = "A topic"
        a_description = "A description"
        notify_sales_command = NotifySalesCommand("A topic", "A description")
        notify_sales_use_case_mock = mockito.mock(NotifySalesUseCase)
        when(notify_sales_use_case_mock).execute(mockito.any()).thenReturn(mockito.any())
        with container.notify_sales_use_case.override(notify_sales_use_case_mock):
            dummyBody = {
                "topic": a_topic,
                "description": a_description
            }
            response = self.client.post(reverse("sales_email_notification"),
                                        data=dummyBody,
                                        content_type='application/json')

            self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_post_given_an_body_without_topic_should_return_400(self):
        a_description = "A description"
        notify_sales_command = NotifySalesCommand("A topic", "A description")
        notify_sales_use_case_mock = mockito.mock(NotifySalesUseCase)
        when(notify_sales_use_case_mock).execute(mockito.any()).thenReturn(mockito.any())
        with container.notify_sales_use_case.override(notify_sales_use_case_mock):
            dummyBody = {
                "description": a_description
            }
            response = self.client.post(reverse("sales_email_notification"),
                                        data=dummyBody,
                                        content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)

    def test_post_given_an_body_without_description_should_return_400(self):
        a_topic = "A topic"
        notify_sales_command = NotifySalesCommand("A topic", "A description")
        notify_sales_use_case_mock = mockito.mock(NotifySalesUseCase)
        when(notify_sales_use_case_mock).execute(mockito.any()).thenReturn(mockito.any())
        with container.notify_sales_use_case.override(notify_sales_use_case_mock):
            dummyBody = {
                "topic": a_topic
            }
            response = self.client.post(reverse("sales_email_notification"),
                                        data=dummyBody,
                                        content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)