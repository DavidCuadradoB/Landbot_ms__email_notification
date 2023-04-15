from django.urls import path

from emailNotification.infrastructure import views

urlpatterns = [
    path("", views.sales_email_notification, name="sales_email_notification"),
]