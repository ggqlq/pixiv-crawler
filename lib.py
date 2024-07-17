import requests
import os
import urllib.parse
from typing import *
import json
import app_config

class AlwaysGreater:
    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

def getArtworkInfoByID(id: int, Cookie: str, proxies:Dict[str, str] = {}) -> str:
    url = f'https://www.pixiv.net/ajax/illust/{id}'
    params = {'lang': 'zh'}
    headers = {'Cookie': Cookie, 'Referer': f'https://www.pixiv.net/artworks/{id}', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    r = requests.get(url, params=params, headers=headers, proxies=proxies)
    r.raise_for_status()
    body =  r.json()['body']
    artwork = {'id': int(body['id']), 'title': body['title'], 'commit': body['description'], 'tags': [taginfo['tag'] for taginfo in body['tags']['tags']], 'userId': int(body['userId']), 'userName': body['userName']}
    return artwork

def downloadImagesByID(id: int, Cookie: str, out_put_dir: dir = './', proxies:Dict[str, str] = {}) -> None:
    pages_url = f'https://www.pixiv.net/ajax/illust/{id}/pages'
    pages_params = {'lang': 'zh'}
    pages_headers = {'Cookie': Cookie, 'Referer': f'https://www.pixiv.net/artworks/{id}', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    pages =  requests.get(pages_url, params=pages_params, headers=pages_headers, proxies=proxies).json()['body']
    image_urls = [page['urls']['original'] for page in pages]
    if not os.path.exists(out_put_dir):
        os.makedirs(out_put_dir)
    for i, image_url in enumerate(image_urls):
        image = requests.get(image_url, headers={'Referer': f'https://www.pixiv.net/', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}, proxies=proxies)
        with open(os.path.join(f'{out_put_dir}', f'{id}_{i}.jpg'), 'wb') as f:
            f.write(image.content)
    info = getArtworkInfoByID(id, Cookie, proxies=proxies)
    with open(os.path.join(out_put_dir, f'{id}_info.txt'), mode='w', encoding='utf-8') as f:
        f.write(json.dumps(info, indent=4, ensure_ascii=False))
        #print(json.dumps(info, indent=4))


def searchByTag(tag: str, Cookie: str, order='date_d', total: int = -1, proxies:Dict[str, str] = {}) -> Generator[int, None, None]:
    url = f'https://www.pixiv.net/ajax/search/artworks/{urllib.parse.quote(tag)}'
    Referer = f'https://www.pixiv.net/tags/{urllib.parse.quote(tag)}/artworks'
    params = {'word': tag, 'order': order, 'mode': 'all', 'p': 1, 'csw': 0, 'type': 'all', 's_mode':'s_tag_full'}
    headers = {'Cookie': Cookie, 'Referer': Referer, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    now = 0
    if total == -1:
        total = AlwaysGreater()
    while now < total:
        r = requests.get(url, params=params, headers=headers, proxies=proxies)
        r.raise_for_status()
        body = r.json()['body']['illustManga']
        if 'data' not in body:
            break
        datas = body['data']
        if len(datas) == 0:
            break
        for data in datas:
            if 'id' not in data:
                continue
            now += 1
            yield int(data['id'])
            if now >= total:
                break
        params['p'] += 1