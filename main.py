from time import sleep
from pathlib import Path
import subprocess
import atexit
import keyboard

proc: subprocess.Popen = subprocess.Popen("echo")


def cleanup_process():
    global proc
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(5)

        except subprocess.TimeoutExpired:
            proc.kill()


atexit.register(cleanup_process)


# example env
# ~/bob/Dev/.venv
# ~/bob/Dev/American_Sign_language_Detection/app.py
paths = Path(".env").read_text().split("\n")
proc = subprocess.Popen([paths[0], paths[1]], cwd=paths[1].removesuffix("/app.py"))


lastLetter = ""

while True:
    letter = Path("letter").read_text().lower()
    keyboard.write(letter) if lastLetter != letter else None
    lastLetter = Path("letter").read_text().lower()
