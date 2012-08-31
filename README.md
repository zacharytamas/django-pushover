# django-pushover

Easily send push notifications using Pushover.net from your Django project.

*Note:* Currently `django-pushover` is simply a `LogHandler` to push Pushover notifications to admins based on logged events. More generic functionality may come later.

## Usage

Usage is simple. First, create an application for your webapp on the Pushover.net website and take note of your keys. You'll need them next.

Put `pushover_handler.py` somewhere inside your project and set the keys as noted in the file:

    PUSHOVER_APPLICATION_TOKEN = "YOUR_TOKEN_HERE"
    PUSHOVER_LOG_USER_TOKENS = [
        "USER_TOKEN_HERE",  # Joe the admin
    ]

`PUSHOVER_LOG_USER_TOKENS` is a `list` of token strings which will be iterated over when sending push notifications.

With that configured, set the log handlers as you'd like in your `settings.py`:

    LOGGING['handlers']['pushover']: {
        'level': 'INFO',
        'class': 'my_project.utils.pushover_handler.PushoverHandler'
    }
            
    LOGGING['loggers']['my_project'] = {
        'handlers': ['pushover'],
        'level': 'INFO'
    }

Then in your project you can import it and create a push notification wherever you choose, like this:

    import logging
    logger = logging.getLogger(__name__)

    logger.info("A new user account was created: %s" % user.username)
    