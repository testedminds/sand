from email.utils import formatdate
import subprocess


def seconds_since_epoch():
    p = subprocess.Popen(["date", "+%s"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out.decode('UTF-8').strip()


def now():
    # returns UTC in RFC 2822 format
    return formatdate()
