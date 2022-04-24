from plyer import notification


class Notification:
    def __init__(self):
        pass

    def send_notification(self, setup_name, stock_name):
        notification.notify(
            title='Notification',
            message=f'Setup {setup_name} {stock_name}',
            app_icon=None,
            timeout=10,
        )
