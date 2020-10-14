import string
import random

def generate_sapid(length=10):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(length))


def generate_unique_sapid(instance, length=10):
    """ Create unique ext_id of alphanumeric characters """
    sap_id = generate_sapid(length)
    while not instance.check_unique(sap_id):
        sap_id = generate_sapid(length)

    return sap_id