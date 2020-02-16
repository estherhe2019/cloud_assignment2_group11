import os
from setuptools import setup
import pip

if not os.path.exists("./text_pre_processing/glove/glove.6B.50d.txt"):
    import urllib
    import urllib.request
    import progressbar
    import zipfile

    class MyProgressBar():
        def __init__(self):
            self.pbar = None

        def __call__(self, block_num, block_size, total_size):
            if not self.pbar:
                self.pbar=progressbar.ProgressBar(maxval=total_size)
                self.pbar.start()

            downloaded = block_num * block_size
            if downloaded < total_size:
                self.pbar.update(downloaded)
            else:
                self.pbar.finish()
    
    print("Downloading glove.6B.zip ...")
    urllib.request.urlretrieve(
        "http://nlp.stanford.edu/data/glove.6B.zip",
        "./text_pre_processing/glove/glove.6B.zip",
        MyProgressBar())

    print("Unzipping files...")
    with zipfile.ZipFile('./text_pre_processing/glove/glove.6B.zip', 'r') as zip_ref:
        zip_ref.extractall('./text_pre_processing/glove/')
    for remove in [
        './text_pre_processing/glove/glove.6B.zip',
        './text_pre_processing/glove/glove.6B.100d.txt',
        './text_pre_processing/glove/glove.6B.200d.txt',
        './text_pre_processing/glove/glove.6B.300d.txt']:
        os.remove(remove)

    

setup(
    name = 'text_pre_processing',
    version = '1.0',
    description = 'This package performs preprocessing for a sentiment analysis task with a CNN + Embedding model',
    url = '#',
    author = 'Freya',
    author_email = '',
    license = 'MIT',
    packages = [
        'text_pre_processing'
    ],
    install_requires = [
        'nltk',
        'pytest'
    ],
    zip_safe = False)