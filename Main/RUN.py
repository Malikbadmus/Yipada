import subprocess
import schedule
import time

def run_scripts():
    subprocess.run(['python', 'requests.py'])
    subprocess.run(['python', 'retrieve.py'])
    subprocess.run(['python', 'Update.py'])
    subprocess.run(['python', 'set.py'])

schedule.every(45).minutes.do(run_scripts)

while True:
    schedule.run_pending()
    time.sleep(1)
