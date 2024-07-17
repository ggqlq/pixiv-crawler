import webbrowser
import lib
import os
from typing import *
from concurrent.futures import ThreadPoolExecutor, as_completed
from app_config import Config

def main():
    config = Config()
    if config.cookie is None or config.cookie == '':
        if (os.path.isfile('cookie.cache')):
            f = open('cookie.cache', 'r')
            cookie_t = f.read()
            config.cookie = cookie_t.encode('utf-8')
            f.close()
        else:
            print('Cookie is empty, please input the cookie.')
            config.cookie = input('Cookie: ')
    with open('cookie.cache', 'w') as f:
        f.write(str(config.cookie))
    
    cookie = config.cookie
    tag = config.tags[0]
    max_download_number = config.max_download_number
    out_put_dir = config.out_put_dir
    max_workers = config.thread_number
    artworks = lib.searchByTag(tag, cookie, total=max_download_number, proxies=config.proxy)
    futures = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for artwork in artworks:
            try:
                #lib.downloadImagesByID(artwork, cookie, out_put_dir=os.path.join(out_put_dir, str(artwork)))
                futures.append(executor.submit(download_task, artwork, cookie, os.path.join(out_put_dir, str(artwork)), config.proxy))
            except Exception as e:
                print(f'Failed: {e}')
            #print(f'Successfully downloaded.')
        #for future in as_completed(futures):
        #    try:
        #        print(f'Successfully downloaded {future.result()}.')
        #    except Exception as e:
        #        print(f'Error occurred: {e}')
    print('Download completed.')

def download_task(id, cookie, out_put_path, proxy):
    print(f'Downloading artwork {id}...')
    try:
        lib.downloadImagesByID(id, cookie, out_put_path, proxy)
        print(f'Successfully downloaded {id}.')
    except Exception as e:
        print(f'Error occurred when downloaded {id}: {e}')

if __name__ == '__main__':
    main()