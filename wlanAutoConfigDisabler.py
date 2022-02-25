# Justin Lu
# Feb. 25, 2022
# building: 
# cd wlanAutoconfig 
# pyinstaller --uac-admin -F wlanAutoConfigDisabler.py 

import os, sys
import tkinter as tk
from tkinter import ttk

# Create window
root = tk.Tk()

# Fix blurry text
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    # rest of code
    # initializing window
    root.title('wlanAutoConfigDisabler')
    root.geometry('600x200+0+0')
    root.resizable(False, False)
    os.system('cmd /c echo wlanAutoConfigDisabler')
    # adding label
    label = ttk.Label(root, 
                      text = """Welcome to Justin's wlanAutoConfigDisabler.""",
                      font = ("Arial", 14),
                      anchor = 'center',
                      relief = tk.GROOVE)
    label.pack(fill = 'both')
    label2 = ttk.Label(root, 
                      text = """\n
                                Click the disable button to turn off Windows' automatic WLAN 
                                detection. To re-enable, click the enable button.
                                The CMD window will show the status of the setting.
                                NOTE: You cannot connect to new networks while this is disabled.""",
                      font = ("Arial", 12),
                      anchor = 'nw')
    label2.pack(fill = 'both')
    # adding buttons
    
    enable_button = ttk.Button(root, 
                               text = 'Enable', 
                               command = lambda: os.system('cmd /c "netsh wlan set autoconfig enabled=yes interface="Wi-Fi""'))
    

    disable_button = ttk.Button(root, 
                                text = 'Disable', 
                                command = lambda: os.system('cmd /c "netsh wlan set autoconfig enabled=no interface="Wi-Fi""'))
    
    # packing
    enable_button.pack(padx = 150, side = tk.LEFT)
    disable_button.pack(side = tk.LEFT)

    # start main loop
    root.mainloop()
