from datetime import datetime
from time import sleep


def log(msg, when=datetime.now()):
    print('%s: %s' % (when, msg))


log('Hi')
sleep(0.1)
log("Hi Again")


def better_log(msg, when=None):
    when = datetime.now() if when is None else when
    print("%s: %s" % (when, msg))


better_log('Hi')
sleep(0.1)
better_log("Hi Again")
