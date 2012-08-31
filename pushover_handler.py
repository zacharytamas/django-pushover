import logging
import httplib
import urllib

PUSHOVER_APPLICATION_TOKEN = "YOUR_TOKEN_HERE"
PUSHOVER_LOG_USER_TOKENS = [
    "USER_TOKEN_HERE",  # Joe the admin
]

class PushoverHandler(logging.Handler):
    """A logging handler which pushes notifications
    to site admins via Pushover.net"""

    def emit(self, record):

        for user_token in PUSHOVER_LOG_USER_TOKENS:
            conn = httplib.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages",
                urllib.urlencode({
                    "token": PUSHOVER_APPLICATION_TOKEN,
                    "user": user_token,
                    "message": record.getMessage(),
                }), 
            { "Content-type": "application/x-www-form-urlencoded" })
