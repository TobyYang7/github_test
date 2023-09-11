import interpreter
import threading
import time
import os
os.environ['OPENAI_API_KEY'] = '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'
interpreter.model = "gpt-3.5-turbo"


def run_interpreter(messages):
    interpreter.chat(messages)


interpreter.reset()
while True:
    messages = input("Input your message: ")

    t = threading.Thread(target=run_interpreter, args=(messages,))
    t.start()

    while t.is_alive():
        time.sleep(0.1)
