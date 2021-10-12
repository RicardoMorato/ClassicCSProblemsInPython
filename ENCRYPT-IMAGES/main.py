from secrets import token_bytes
from typing import Tuple
from base64 import b64encode, b64decode

def random_key_generator(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, 'big')

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original
    dummy: int = random_key_generator(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, 'big')
    encrypted: int = original_key ^ dummy
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return temp.decode()


if __name__ == "__main__":
    with open('github-profile-pic.png', 'rb') as image:
        image_str: bytes = b64encode(image.read())
        key1, key2 = encrypt(image_str)
        result: str = decrypt(key1, key2)

        print(f'The decrypted is equal to the original: {image_str.decode() == result}')
