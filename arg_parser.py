import argparse
from typing import *

def parse_args() -> Dict[str, Any]:
    parser = argparse.ArgumentParser(description='Pixiv crawler')
    parser.add_argument('-c', '--cookie', help='Cookie for Pixiv', type=str, default='./cookie.txt')
    parser.add_argument('-t', '--tags', help='Tags for Pixiv, in quotation marks, split by a space. eg: \'taga tagb\'', type=str, default='\'\'')
    parser.add_argument('-n', '--max_download_number', help='Max download number. -1 for unlimited', type=int, default=-1)
    parser.add_argument('-o', '--out_put_dir', help='Output directory', type=str, default='./downloads')
    parser.add_argument('-th', '--thread_number', help='Thread number. The number of threads to download images, default by 5', type=int, default=5)
    parser.add_argument('-pf', '--proxy-file', help='Path to file that store the information of proxy. The file\'s format should be a json, \
        such as "{\'http\':\'your.proxy.server:port\'}. Default ./proxy.json"', type=str, default='proxy.json')
    args = parser.parse_args()
    return vars(args)