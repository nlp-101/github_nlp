#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:38:21 2019

@author: ericescalante
"""

import os
import json
from typing import Dict, List
import requests

# TODO: make a github personal access token
# TODO: replace YOUR_GITHUB_USERNAME with your github username

# Go here and generate a personal access token
# https://github.com/settings/tokens
# save it in your env.py file
from env import github_token

DATA_DIR = 'data'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

headers = {
    'Authorization': f'token {github_token}',
    'User-Agent': 'escalante-eric'
}

def github_api_request(url: str) -> requests.Response:
    return requests.get(url, headers=headers)

def get_repo_language(repo: str) -> str:
    url = f'https://api.github.com/repos/{repo}'
    return github_api_request(url).json()['language']
    
def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f'https://api.github.com/repos/{repo}/contents/'
    return github_api_request(url).json()

def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    '''
    Takes in a response from the github api that lists
    the files in a repo and returns the url that can be
    used to download the repo's README file.
    '''
    for file in files:
        if file['name'].lower().startswith('readme'):
            return file['download_url']

def process_repo(repo: str) -> Dict[str, str]:
    '''
    Takes a repo name like "gocodeup/codeup-setup-script" and returns
    a dictionary with the language of the repo and the readme contents.
    '''
    contents = get_repo_contents(repo)
    return {
        'repo': repo,
        'language': get_repo_language(repo),
        'readme_contents': requests.get(get_readme_download_url(contents)).text
    }

# TODO: put a lot of repos here (or generate the list progromatically)
repos = [
    'twbs/bootstrap',
    'facebook/react',
    'EbookFoundation/free-programming-books',
    'sindresorhus/awesome',
    'kamranahmedse/developer-roadmap',
    'jwasham/coding-interview-university',
    'electron/electron',
    'facebook/create-react-app',
    'vinta/awesome-python',
    'donnemartin/system-design-primer',
    'electron/electron',
    'facebook/create-react-app',
    'vinta/awesome-python',
    'donnemartin/system-design-primer',
    'nodejs/node',
    'FortAwesome/Font-Awesome',
    'daneden/animate.css',
    'golang/go',
    'toddmotto/public-apis',
    'vinta/awesome-python',
    'flutter/flutter',
    'donnemartin/system-design-primer',
    'nodejs/node',
    'FortAwesome/Font-Awesome',
    'angular/angular.js',
    'daneden/animate.css',
    'axios/axios',
    'golang/go',
    'toddmotto/public-apis',
    'moby/moby',
    'tensorflow/models',
    'kubernetes/kubernetes',
    'laravel/laravel',
    'jquery/jquery',
    'mrdoob/three.js',
    'ytdl-org/youtube-dl',
    'GoogleChrome/puppeteer',
    'apple/swift',
    'iluwatar/java-design-patterns',
    'mui-org/material-ui',
    'socketio/socket.io',
    'ant-design/ant-design',
    'hakimel/reveal.js',
    'vuejs/awesome-vue',
    'danistefanovic/build-your-own-x',
    '30-seconds/30-seconds-of-code',
    'pallets/flask',
    '30-seconds/30-seconds-of-code',
    'pallets/flask',
    'expressjs/express',
    'nvbn/thefuck',
    'avelino/awesome-go',
    'chartjs/Chart.js',
    'rails/rails',
    'h5bp/html5-boilerplate',
    'django/django',
    'jakubroztocil/httpie',
    'chartjs/Chart.js',
    'rails/rails',
    'h5bp/html5-boilerplate',
    'django/django',
    'jakubroztocil/httpie',
    'moment/moment',
    'meteor/meteor',
    'keras-team/keras',
    'elastic/elasticsearch',
    'prettier/prettier',
    'Kickball/awesome-selfhosted',
    'google/material-design-lite',
    'juliangarnier/anime',
    'Alamofire/Alamofire',
    'gogs/gogs',
    'storybooks/storybook',
    'zeit/next.js',
    'ansible/ansible',
    'shadowsocks/shadowsocks-windows',
    'antirez/redis',
    'rust-lang/rust',
    'Dogfalo/materialize',
    'yarnpkg/yarn',
    'google/guava',
    'parcel-bundler/parcel',
    'aymericdamien/TensorFlow-Examples',
    'Kickball/awesome-selfhosted',
    'google/material-design-lite',
    'juliangarnier/anime',
    'Alamofire/Alamofire',
    'chrislgarry/Apollo-11',
    'gogs/gogs',
    'thedaviddias/Front-End-Checklist',
    'protocolbuffers/protobuf',
    'apache/incubator-echarts',
    'x64dbg/x64dbg',
    'babel/babel',
    'scrapy/scrapy',
    'apache/incubator-echarts',
    'x64dbg/x64dbg',
    'FreeCodeCampChina/freecodecamp.cn',
    'babel/babel',
    'scrapy/scrapy',
    'minimaxir/big-list-of-naughty-strings',
    'square/retrofit',
    'square/okhttp',
    'prettier/prettier',
    'google/guava',
    'parcel-bundler/parcel',
    'aymericdamien/TensorFlow-Examples',
    'Kickball/awesome-selfhosted'
]

def scrape_github_data():
    data = [process_repo(repo) for repo in repos]
    json.dump(data, open('data.json', 'w'))
    
if __name__ == '__main__':
    scrape_github_data()