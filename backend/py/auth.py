import random
import secrets
import string

alphabet = string.ascii_letters + string.digits

def genarateSecrets():
    token = "".join(secrets.choice(alphabet) for c in range(16))
    return token