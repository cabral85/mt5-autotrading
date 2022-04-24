from plyer import notification


def send_notification(setup_name, stock_name):
    notification.notify(
        title='Notification',
        message=f'Setup {setup_name} {stock_name}',
        app_icon=None,
        timeout=10,
    )
