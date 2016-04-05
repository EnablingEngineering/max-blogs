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
            upload.upload_post(new)
        before = after


def get_files(path):
    return dict([(files, None) for files in os.listdir(path)])


main()
