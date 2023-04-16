from unittest import TestCase

import mockito
from mockito import when

from emailNotification.application.command.NotifyEngineeringCommand import NotifyEngineeringCommand
from emailNotification.application.repository.EmailSender import EmailSender
from emailNotification.application.service.NotifyEngineeringUseCase import NotifyEngineeringUseCase


class NotifySalesUseCaseTest(TestCase):
    def test_execute_should_call_event_sender(self):
        a_topic = "A topic"
        a_description = "A description"
        email_sender_mock = mockito.mock(EmailSender)
        when(email_sender_mock).send(mockito.any()).thenReturn(mockito.any())
        notify_engineering_use_case = NotifyEngineeringUseCase(email_sender_mock, 'an email')
        notify_engineering_command = NotifyEngineeringCommand(a_topic, a_description)
        notify_engineering_use_case.execute(notify_engineering_command)
        mockito.verify(email_sender_mock).send(mockito.any())
