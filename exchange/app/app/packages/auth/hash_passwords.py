from passlib.hash import pbkdf2_sha256


def make_hash(password):
    """make hash"""
    if not isinstance(password, str):
        password = str(password)

    return pbkdf2_sha256.hash(password)

def check_hash(password,hash_):
    if not isinstance(password, str):
        password = str(password)

    return pbkdf2_sha256.verify(password, hash_)