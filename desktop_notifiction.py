from plyer import notification
import time

if __name__ == '__main__':

    while True:
        notification.notify(
            title = " Take rest. ",
            message = "Rest for heath",
            app_icon = "icon/path",
            timeout = 5

        )

        time.sleep(60*60)
