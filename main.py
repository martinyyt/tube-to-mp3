from pytube import YouTube
from joblib import Parallel, delayed
import csv
import time
import os


def download(url: str):
    yt = YouTube(url)
    title = ''
    try:
        title = yt.title
    except KeyError:
        title = yt.author

    print(f'downloading: {title}')
    # print(yt.streams.filter(only_audio=True, abr='128kbps'))

    yt.streams.filter(only_audio=True, abr='128kbps').first().download(
        filename=f'{title}.mp4')


if __name__ == "__main__":
    start = time.time()

    url_list = list()

    with open('url-list.csv', newline='') as f:
        reader = csv.reader(f)

        for row in reader:
            if row[0].startswith('//') or row[0].startswith('#'):
                print(f'skipping url {row[0]}')
            else:
                url_list.append(row[0])

    try:
        os.chdir('downloads')
    except:
        print(f'downloads folder does not exist, creating...')
        os.mkdir('downloads')
        os.chdir('downloads')

    Parallel(n_jobs=-1)(delayed(download)(url) for url in url_list)

    end = time.time()
    print(f'completed in {end - start:.2f} seconds')
