#!/usr/bin/env python3
import os
import urllib

import requests

import config


def dump_stories():
    new_stories = 0
    num_stories = 0
    r = requests.get(
        "https://i.instagram.com/api/v1/feed/reels_tray/",
        cookies=config.instagram_cookies, headers=config.instagram_headers).json()
    for user in r['tray']:
        user_dir = "./stories/{0!s}-{1!s}".format(user['user']['username'], user['id'])
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)

        print("[*] dumping " + user['user']['username'])
        user_stories = requests.get(
            "https://i.instagram.com/api/v1/feed/user/{0!s}/reel_media/".format(user['id']),
            cookies=config.instagram_cookies, headers=config.instagram_headers).json()

        for item in user_stories['items']:
            num_stories += 1
            if 'video_versions' in item:
                url = item['video_versions'][0]['url']
            else:
                url = item['image_versions2']['candidates'][0]['url']

            filename = url.split('/')[-1].split('?')[0]
            file_path = user_dir + '/' + filename
            if not os.path.isfile(file_path):
                new_stories += 1
                print(" +  " + filename)
                urllib.request.urlretrieve(url, file_path)
            else:
                print(" -  " + filename)

    return len(r['tray']), num_stories, new_stories


def send_notification(message):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={"token": config.pushover_app_token,
              "user": config.pushover_user_token,
              "title": "instadump",
              "message": message})


if __name__ == "__main__":
    num_users, num_stories, new_stories = dump_stories()
    message = "{0!s} stories ({1!s} new)\n{2!s} users".format(num_stories, new_stories, num_users)
    if config.pushover_app_token and config.pushover_user_token:
        send_notification(message)
    else:
        print(message)
