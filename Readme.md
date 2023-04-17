# Description

This microservice is a django service and is responsible for sending emails. It is listening to a kafka broker and,
based on the topic, sends an email to one team or another.

## Run it:

### Using Docker (Recommended)

In the root folder just run:

`docker-compose up`

This service has a real implementation, there are some environment variables that need to be added:

create a .env file in the Landbot_ms__email_notification folder

```
cd Landbot_ms__email_notification
touch .env
```
Add the following variables in this file:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=originMail
EMAIL_HOST_PASSWORD='password'
```

## Test it

This service will only listen messages, in theory, this shouldn't have any endpoint. BUT:

In this point I found a problem. As django is set up only to get endpoints, it is necessary to make a workaround to have a subscriber always listening to a topic. The solution I came up with was to call an endpoint to start the kafka subscribers. You only need to call these once, and you don't need to wait for the response. There is one endpoint per subscriber. In the test, there are two subscribers (sales and engineering) so two endpoints need to be called.

I'm sure there must be another way to do this. Maybe django is not needed in this microservice because there is no endpoint to expose. But since all the configuration, mainly control inversion and dependency injection, was done in django in the other microservice, I decided to go with it.

The endpoints that has to be called are:

* For the sales consumer:
  * `[GET] http://127.0.0.1:8001/notification/sales/kafka/`
* For the engineering consumer:
  * `[GET] http://127.0.0.1:8001/notification/engineering/kafka/`

Once the Kafka is initialised, it will listen to the configured topic. For example, the SalesConsumer will listen to the Sales topic and the EngineeringConsumer will listen to the Engineering topic. Both will run
use case and the implementation can be different.

The microservice also provides a way to send an email in the DjangoEmailSender. This email is independent of the use
case, it just needs to get the recipient's email.

This destination email is injected into the use case from the properties. So each use case will have its own email.

I thought about moving the configuration of the DjangoEmailSender to another class and injecting it into the DjangoEmailSender,
but I think that might couple the EmailSender interface to a particular Django implementation. Maybe a different
implementation might not need all these configurations, or might need more.

If another team needs to be notified by email, all we need to do is create a new consumer that listens to a new topic.
to a new issue. This architecture helps with the escalation of the system.