import hystats_reader
import schedule
import time

def test():
    print('hi')


schedule.every().day.at("18:34").do(test)

while True:
    schedule.run_pending()
    time.sleep(60)
