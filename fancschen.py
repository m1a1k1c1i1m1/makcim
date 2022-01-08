from lxml import html
import requests
import os


HEDER = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 "
                  "Safari/537.36 "
}


def get_zapros(url):
    r = requests.get(url, headers=HEDER)
    return r


def seve(hash_lib, result):
    derektor = os.path.exists("cache")
    if derektor == False:
        os.mkdir("cache")
    with open(f'cache/{hash_lib}.txt', 'w') as file:
        file.write(result)


def schow(name):
    print("                                                ", name[0])
    print("_" * 170)
    list_cache = os.listdir("cache")
    for x in list_cache:
        print("|", x, " " + "|")
    print("_" * 170)


def parse1(hash_lib, req):
    tree = html.fromstring(req.content)
    name = tree.xpath('//div[@class="news-header__title"]/h1/text()')
    cont = tree.xpath('//div[@class="news-text"]/p/text()')
    res = ' '.join(cont)
    schow(name)
    seve(hash_lib, res)


def parse2(hash_lib, req):
    tree = html.fromstring(req.content)
    name = tree.xpath("//h1[@class='tm-article-snippet__title tm-article-snippet__title_h1']/span/text()")
    if tree.xpath("//*[@id='post-content-body']/div/p/text()"):
        cont = tree.xpath("//*[@id='post-content-body']/div/p/text()")
        res = ' '.join(cont)
        schow(name)
        seve(hash_lib, res)
    elif tree.xpath('//*[@id="post-content-body"]/div/text()'):
        cont = tree.xpath('//*[@id="post-content-body"]/div/text()')
        res = ' '.join(cont)
        schow(name)
        seve(hash_lib, res)


def check(name):
    check_file = os.path.isfile(f"cache/{name}.txt")
    return check_file
