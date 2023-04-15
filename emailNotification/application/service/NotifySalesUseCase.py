from emailNotification.application.command.NotifySalesCommand import NotifySalesCommand


class NotifySalesUseCase:

    def execute(self, command: NotifySalesCommand):
        print("I'm alive!!!")
