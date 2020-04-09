import win32gui
import win32con
import pyautogui
import pyperclip
import time

WM_SETTEXT = win32con.WM_SETTEXT
WM_KEYDOWN = win32con.WM_KEYDOWN
VK_RETURN = win32con.VK_RETURN

def Send_msg(Chat_Name, msg):
    hwnd = win32gui.FindWindow(None, Chat_Name)
    txt = win32gui.FindWindowEx(hwnd, None, "RichEdit20W", None)
    win32gui.SendMessage(txt, WM_SETTEXT, 0, str(msg))
    win32gui.PostMessage(txt, WM_KEYDOWN, VK_RETURN, 0)

def Send_msgs(Chat_Name, msgs):
    hwnd = win32gui.FindWindow(None, Chat_Name)
    txt = win32gui.FindWindowEx(hwnd, None, "RichEdit20W", None)
    for msg in msgs:
        win32gui.SendMessage(txt, WM_SETTEXT, 0, str(msg))
        win32gui.PostMessage(txt, WM_KEYDOWN, VK_RETURN, 0)
        time.sleep(0.5)

def Find_User(name):
    a = win32gui.FindWindow(None, "카카오톡")
    win32gui.BringWindowToTop(a)
    win32gui.SetForegroundWindow(a)
    pyautogui.hotkey('ctrl','f')
    pyperclip.copy(name)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press("down")
    pyautogui.press("enter")

if __name__=="__main__":
    Find_User("")
    Send_msg("","")
