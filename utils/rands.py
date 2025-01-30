from random import SystemRandom
import string
from django.utils.text import slugify

def random_letters(k):
    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits, k=k
    ))


def new_slugfy(text, k=5):
    return slugify(text) + '-' + random_letters(k=k)


