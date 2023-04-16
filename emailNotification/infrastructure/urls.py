from django.urls import path

from emailNotification.infrastructure import views, salesKafkaView, engineeringKafkaView

urlpatterns = [
    path("sales/", views.sales_email_notification, name="sales_email_notification"),
    path("sales/kafka/", salesKafkaView.kafka_sales_init, name="kafka_sales_init"),
    path("engineering/kafka/", engineeringKafkaView.kafka_engineering_init, name="kafka_engineering_init"),
]
