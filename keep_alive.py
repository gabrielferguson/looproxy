# keep_alive.py
import time
import httpx
import os
import threading

def function_to_run():
    count = 0
    url = f"https://{os.environ.get('PROJECT_DOMAIN')}/health"
    while True:
        if count > 30:
            break
        try:
            httpx.get(url).close()
            print("Keeping alive...")
        except:
            print("Failed to keep alive")
            count += 1
        time.sleep(5 * 60)  # 每5分钟请求一次

thread = threading.Thread(target=function_to_run)
thread.start()
# thread.join()
