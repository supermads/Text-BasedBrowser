from collections import deque
import os
import requests
from bs4 import BeautifulSoup


def verify_url(url):
    if "." in url:
        if "http" not in url:
            url = "https://" + url
        r = requests.get(url)
        status = r.status_code
        if status == 200:
            return r.content
    return None


def process_url(url, dir):
    content = verify_url(url)
    if content:
        file_name = url.strip(".com")
        file_name = file_name.replace("https://", "")
        file_path = os.path.join(os.getcwd(), dir, file_name)
        soup = BeautifulSoup(content, 'html.parser')
        with open(file_path, "w") as f:
            f.write(soup.text)
        print(soup.text)
        return True
    return False


def main():
    history = deque()
    keep_going = True
    dir = os.sys.argv[1]
    if not os.path.exists(dir):
        os.mkdir(dir)
    while keep_going:
        url = input()
        if "exit" in url:
            keep_going = False
        elif url == "back":
            if len(history) > 1:
                history.pop()
                process_url(history.pop(), dir)
        elif process_url(url, dir):
            history.append(url)
        else:
            print("Error")


main()
