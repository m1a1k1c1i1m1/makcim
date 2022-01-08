import hashlib
import re
from fancschen import *


while True:
    url = input('Введите url:')
    hash_lib = hashlib.md5(url.encode()).hexdigest()
    chek = check(hash_lib)
    if chek == True:
        with open(f"cache/{hash_lib}.txt", "r") as file:
            print(file.read())
    else:
        if re.search(r'onliner', url):
            resault = get_zapros(url)
            if resault.status_code == 200:
                parse1(hash_lib, resault)
        else:
            if re.search(r'habr', url):
                resault = get_zapros(url)
                if resault.status_code == 200:
                    parse2(hash_lib, resault)
            if url == "exit":
                break
