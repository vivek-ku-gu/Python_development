import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Drink water reminder",
            message="Your target 4 lit water",
            app_icon="C://Users//GIGABYTE\Desktop//python coding//water notification//icon.ico",
            timeout=8   
        )
        time.sleep(60*60*2)
        # if you want to run the program in the background then type pythonw /main.py