# Pixiv Crawler

## Introduction

Use this project to download images from pixiv.

## Installation

### Clone the repository

> Make sure you have installed git
> You can install git from [here](https://git-scm.com/downloads)(for Linux) or [here](https://github.com/git-for-windows/git/releases/)(for Windows)

```bash
git clone https://github.com/ggqlq/pixiv-crawler.git
cd pixiv-crawler
```

or download the zip file from github and extract it.

After that, you will see a folder named `pixiv-crawler` in your current directory.
The structure of the folder is as follows:

```bash
.
├── app_config.py
├── app.py
├── arg_parser.py
├──  .gitignore
├── __init__.py
├── lib.py
├── LICENSE
├── proxy.json.example
├── __pycache__
│   ├── app_config.cpython-312.pyc
│   ├── arg_parser.cpython-312.pyc
│   └── lib.cpython-312.pyc
├── README.md
└── requirements.txt
```

### Install dependencies

Before any other operations, you need to install [python](https://www.python.org/downloads/), the recommended version is 3.12.3.

To install dependencies, run the following command:

```bash
pip install -r requirements.txt

```

## Usage

### 1. Get your pixiv cookie

Programs need your pixiv cookie to access assets. You need to open web browser and login to pixiv, then open the developer tools to get your cookie.

1. Open your browser and visit[pixiv](https://www.pixiv.net)
2. Open the developer tools in browser. For most browsers, you can press `F12` to open it.
3. Click the `Network` tab in the developer tools.
4. Press `F5` in the browser to refresh the page.
5. In the developer tools, you will see a list of requests. Find the request with the url `https://www.pixiv.net/`. Click it.
6. In the `Headers` tab, you will see a list of headers. Find the `Cookie` header. Copy the value of the header.
7. Create a file named `cookie.txt` in the root directory of the project. Paste the cookie you copied into the file.

### 2. Run the program

You can run the program in terminal with such command:

```bash
python app.py -t <tag> -n 5
```

> If you are using Ubuntu or Debian, you may need to run `python3` instead of `python`.

If there's no error, you will see the following message:

```bash
Downloading artwork 000000000...
Downloading artwork 000000001...
Downloading artwork 000000002...
Downloading artwork 000000003...
Downloading artwork 000000004...
Successfully downloaded 000000000.
Successfully downloaded 000000001.
Successfully downloaded 000000002.
Successfully downloaded 000000003.
Successfully downloaded 000000004.
Download completed.

```

The argument `-t` is the tag of the artwork you want to download. and `-n` tells the program how many artworks it should download. If you don't specify `-n`, the program will download all the artworks with the tag you specified.

You will also find a new folder named `downloads` in the root directory of the project. In the folder, you will find all the downloaded images.
The structure of the root directory is as follows:

```bash
.
├── app_config.py
├── app.py
├── arg_parser.py
├── cookie.cache
├── downloads
│   ├── 000000000
│   │   ├── 000000000_0.jpg
│   │   └── 000000000_info.txt
│   ├── 000000001
│   │   ├── 000000001_0.jpg
│   │   ├── 000000001_1.jpg
│   │   └── 000000001_info.txt
│   ├── 000000002
│   │   └── ...
│   ├── 000000003
│   │   └── ...
│   └── 000000004
│       └── ...
├──  .gitignore
├── __init__.py
├── lib.py
├── LICENSE
├── proxy.json.example
├── __pycache__
│   ├── app_config.cpython-312.pyc
│   ├── arg_parser.cpython-312.pyc
│   └── lib.cpython-312.pyc
├── README.md
└── requirements.txt
```

> 000000000, 000000001, ... will be replaced by the actual id of the artwork.

### 3. Use proxy (Optional)

If you want to use proxy to access pixiv, you can create a file named `proxy.json` in the root directory of the project. The file should be in the following format:

```json
{
    "http": "xxx://xxx.xxx.xxx:xx",
    "https": "xxx://xxx.xxx.xxx:xx"
}
```

### 4. Use multiple threads (Optional)

The program uses Five threads by default. If you want to use more threads, you can add the `-th` option.

```bash
python app.py -t <tag> -n 5 -th 10
```

This will use 10 threads to download the artworks.

## Arguments

Here's a list of all arguments:

| Argument | Description |
| -------- | ----------- |
| -t       | The tag of the artwork you want to download. |
| -n       | The number of artworks you want to download. |
| -th      | The number of threads you want to use. |
| -c       | A path to the file that store the cookie, default is `cookie.txt`. |
| -o       | The folder that store the downloaded images, default is `downloads`. |
| -pf      | The path to a file that store the proxy settings, default is `proxy.json`. |

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
