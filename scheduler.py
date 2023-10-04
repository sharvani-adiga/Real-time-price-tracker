import schedule
import time
import subprocess

def run():
    subprocess.run(['python','scrape.py'])

schedule.every(30).minutes.do(run)  #frequency can be set as per preference

while True:
    schedule.run_pending()
    time.sleep(1)
