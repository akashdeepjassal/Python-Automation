# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:44:27 2017

@author: Akashdeep Jassal
"""

"""script to download all videos in a playlist"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from pytube import YouTube
import re
import argparse


def playlist(url):
    req = urlopen(url)
    res = req.read()
    soup = bs(res, 'html.parser')
    list = soup.find_all('a', {'class': 'pl-video-title-link'})
    files_in_pl = []
    for link in list:
        vid_id = link.get('href').split('&')[0]
        files_in_pl.append('https://www.youtube.com' + vid_id)

    for link in files_in_pl:
        print ('downloading ' + YouTube(link).title)
        YouTube(link).streams.first().download()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str,
                        help="youtuble playlist url")
    args = parser.parse_args()
    inurl = args.inp
    ret = re.search('com(.+?)\?', inurl)
    if(ret is not None):
        ret = ret.group(1)
    else:
        print ('wrong url')
        quit()
    if(ret != '/playlist'):
        print ('no url')
        quit()
    playlist(inurl)
