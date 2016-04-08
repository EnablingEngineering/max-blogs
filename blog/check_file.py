# -*- coding: utf-8 -*-

import os
import time
import upload


def main():
    path_to_watch = "."
    before = get_files(path_to_watch)
    while 1:
        time.sleep(5)
        after = get_files(path_to_watch)
        new = [f for f in after if f not in before]
        if new:
            parse_files(new)
        before = after


def get_files(path):
    return dict([(files, None) for files in os.listdir(path)])


def parse_files(files):
    for f in files:
        with open(f, 'r') as myfile:
            data = "<div>"
            data += myfile.read() + "</div>"
            upload.upload_post(data)

main()
