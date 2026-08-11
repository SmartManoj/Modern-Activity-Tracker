from pymsgbox import alert
from time import sleep
from datetime import datetime
def notify_after_eat():
    # sleep(60*60)
    alert(f'Take Tablet at {datetime.now().strftime("%H:%M")}')
