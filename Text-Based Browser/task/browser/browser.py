
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
from collections import deque
import os
import requests


def process_url(url, dir):
    if "http" not in url:
        url = "https://" + url
    r = requests.get(url)
    file_name = url.strip(".com")
    file_name = file_name.replace("https://", "")
    file_path = os.path.join(os.getcwd(), dir, file_name)
    with open(file_path, "w") as f:
        f.write(r.text)
    print(r.text)


def main():
    history = deque()
    keep_going = True
    dir = os.sys.argv[1]
    if not os.path.exists(dir):
        os.mkdir(dir)
    while keep_going:
        url = input()
        if url == "exit":
            keep_going = False
        elif url == "back":
            if len(history) > 1:
                history.pop()
                process_url(history.pop(), dir)
        elif "." in url:
            process_url(url, dir)
            history.append(url)
        else:
            print("Error")


main()
