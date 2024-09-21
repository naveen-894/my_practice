import resend
from typing import List

def send_email():
    try:
        resend.api_key = "re_fPyT58ye_MowMXWgfEdYiBfZr3AsCVYqC"

        params: List[resend.Emails.SendParams] = [
        {
            "from": "no-reply@rawnn.com",
            "to": ["raghavendrabc.02@gmail.com"],
            "subject": "hello world",
            "html": "<h1>it works!</h1>",
        },
        {
            "from": "no-reply@rawnn.com",
            "to": ["raghuchandrashekar259@gmail.com"],
            "subject": "world hello",
            "html": "<p>it works!</p>",
        },
        {
            "from": "no-reply@rawnn.com",
            "to": ["rawnnfashions@gmail.com"],
            "subject": "world hello",
            "html": "<p>it works!</p>",
        }
        ]
        resend.Batch.send(params)
    except Exception as e:
        print(e)