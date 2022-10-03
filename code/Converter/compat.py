
from numpy.compat import basestring, unicode

try:
    strtype = basestring
except NameError:
    strtype = str


def to_s(val):
    try:
        return unicode(val)
    except NameError:
        return str(val)
