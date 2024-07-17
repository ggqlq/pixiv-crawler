from arg_parser import parse_args
import json
import os


class Config():
    def __init__(self):
        self.cookie = None
        self.tags = ['']
        self.max_download_number = -1
        self.out_put_dir = './downloads'
        self.thread_number = 5
        self.proxy = {}
        args = parse_args()
        if 'cookie' in args:
            if args['cookie'] is not None and os.path.isfile(args['cookie']):
                with open(args['cookie'], 'r') as f:
                    self.cookie = f.read().encode('utf-8')
        if 'tags' in args:
            tags_str = args['tags']
            if tags_str.startswith('\'') and tags_str.endswith('\''):
                tags_str = tags_str[1:-1]
            self.tags = tags_str.split(' ')
        if 'max_download_number' in args:
            self.max_download_number = args['max_download_number']
        if 'out_put_dir' in args:
            self.out_put_dir = args['out_put_dir']
        if 'thread_number' in args:
            self.thread_number = int(args['thread_number'])
        if 'proxy_file' in args:
            file = args['proxy_file']
            if os.path.isfile(file):
                with open(file, 'r') as f:
                    self.proxy = json.load(f)