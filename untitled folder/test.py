import resend
from typing import List

try:
    resend.api_key = "re_123456789"

    params: List[resend.Emails.SendParams] = [
    {
        "from": "onboarding@resend.dev",
        "to": ["vnaveen894@gmail.com"],
        "subject": "hello world",
        "html": "<h1>it works!</h1>",
    },
    {
        "from": "onboarding@resend.dev",
        "to": ["vnaveen894@gmail.com"],
        "subject": "world hello",
        "html": "<p>it works!</p>",
    }
    ]
    resend.Batch.send(params)
except Exception as e:
    print(e)