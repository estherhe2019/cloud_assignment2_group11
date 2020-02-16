# tweets-pre-processing
This is a python library performing preprocessing for a sentiment analysis task with a CNN + Embedding model

## Installation
1. Use `pip install -r requirements.txt` to install the dependencies.
2. run `pip install .` to install the package. The program will automatically download [GloVe pre-trained word dict](http://nlp.stanford.edu/data/glove.6B.zip). You can download [GloVe pre-trained word dict](http://nlp.stanford.edu/data/glove.6B.zip) manually, unzip the file and place the `glove.6B.50d.txt` file under `/text_pre_processing/glove/glove.6B.50d.txt`. This my save the runtime of the install process.