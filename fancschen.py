from lxml import html
import requests
import os

hider = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 "
                  "Safari/537.36 "
}


def get_zapros(url):
    r = requests.get(url, headers=hider)
    return r


def seve(hash_lib, result):
    derektor = os.path.exists("cache")
    if derektor == False:
        os.mkdir("cache")
    with open(f'cache/{hash_lib}.txt', 'w') as file:
        file.write(result)


def len_temp(ar):
    return len(' '.join(ar))


def Show(cach, name, res):
    max_len_aa = 35
    max_len_bb = 90
    list_cache = []
    max_len = 70
    words = res.split()
    arr_1 = []
    list_cache.append(cach)
    last_list = []
    print('                                    ', name[0])
    print('_' * 136)
    for word in words:
        buf = arr_1 + [word]
        if len_temp(buf) >= max_len:
            last_list.append(' '.join(buf))
            arr_1 = []
        else:
            arr_1.append(word)
    len_max = max([len(list_cache), len(last_list)])
    for i in range(0, len_max):
        if last_list[i] in last_list:
            aa = last_list[i]
        if i > len(list_cache):
            bb = ''
        else:
            bb = list_cache[i]
        print(f'| {bb}           | {aa}              |')
    # while len(list_cache) < len(last_list) or len(last_list) < len(list_cache):
    #     if len(list_cache) < len(last_list):
    #         list_cache.append('')
    #     else:
    #         last_list.append('')
    # # len_index = max([len(list_cache), len(last_list)])
    # for i in range(0, len_index):
    #     if list_cache[i] in list_cache and last_list[i] in last_list:
    #         aa = list_cache[i]
    #         bb = last_list[i]
    #         if aa == '' or bb == '':
    #             aa = ' ' * 36
    #         else:
    #             bb = ' ' * 36
    #         req_1 = max_len_aa - len(aa)
    #         req_2 = max_len_bb - len(bb)
    #         print(f'| {aa}           | {bb}              |')
    print('-' * 136)


def parse1(hash_lib, req):
    tree = html.fromstring(req.content)
    name = tree.xpath('//div[@class="news-header__title"]/h1/text()')
    cont = tree.xpath('//div[@class="news-text"]/p/text()')
    res = ' '.join(cont)
    seve(hash_lib, res)
    Show(hash_lib, name, res)


def parse2(hash_lib, req):
    tree = html.fromstring(req.content)
    name = tree.xpath("//h1[@class='tm-article-snippet__title tm-article-snippet__title_h1']/span/text()")
    if tree.xpath("//*[@id='post-content-body']/div[1]/div/div/text()"):
        cont = tree.xpath("//*[@id='post-content-body']/div[1]/div/div/text()")
        res = ' '.join(cont)
        seve(hash_lib, res)
        Show(hash_lib, name, res)
    elif tree.xpath("//*[@id='post-content-body']/div/div/div/p/text()"):
        cont = tree.xpath("//*[@id='post-content-body']/div/div/div/p/text()")
        res = ' '.join(cont)
        seve(hash_lib, res)
        Show(hash_lib, name, res)


def check(name):
    check_file = os.path.isfile(f"cache/{name}.txt")
    return check_file
