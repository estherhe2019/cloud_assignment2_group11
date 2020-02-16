#!/usr/bin/env python
"""This script performs preprocessing for a sentiment
analysis task with a CNN + Embedding model"""

import os
import re
import string
from nltk.tokenize import TweetTokenizer

class PreProcessor:
    """This is the main class for the PreProcessor"""
    def __init__(self, text, max_length_tweet, max_length_dictionary):
        """Constructor of the class. Init with the imput args"""
        if max_length_tweet < 0:
            raise ValueError("max_length_tweet can not be negative!")
        if max_length_dictionary < 0:
            raise ValueError("max_length_dictionary can not be negative!")
        self.text = text
        self.tokens = []
        self.pad = []
        self.max_length_tweet = max_length_tweet
        self.max_length_dictionary = max_length_dictionary
    def clean_text(self):
        """Clean the raw text to remove URLs and remove
        any other non-English chars, inplace"""
        #Cleaning the raw text to remove URLs
        self.text = re.sub(
            r"http\S+",
            "",
            self.text
        ).strip()
        #Removing any other non-English chars
        printable = set(string.printable)
        self.text = ''.join(
            filter(
                lambda x: x in printable,
                self.text
            )
        )
    def tokenize_text(self):
        """Convert a string into an array of tokens."""
        self.tokens = TweetTokenizer().tokenize(self.text)[:self.max_length_tweet]
    def replace_token_with_index(self):
        """replace each token in a list of tokens by their corresponding
        index in GloVe dictionary and producing a list of indexes
        -1 if word doesn't exists in the dictionary"""
        def load_dict():
            """This is a helper function to load the dictionary
            in the most memory efficient way"""
            dic = {}
            curr_dir = os.path.dirname(os.path.realpath(__file__))
            with open(
                    os.path.join(curr_dir, "glove/glove.6B.50d.txt"),
                    "r",
                    encoding="utf-8") as dict_file:
                idx = 1
                for line in dict_file:
                    if idx > self.max_length_dictionary:
                        return dic
                    dic[line.strip().split()[0]] = idx
                    idx += 1
            return dic
        dic = load_dict()
        self.pad = list(map(lambda x: dic[x] if x in dic else -1, self.tokens))
    def pad_sequence(self):
        """Padding a list of indices with 0 until a maximum length"""
        if len(self.pad) < self.max_length_tweet:
            self.pad = self.pad + [0] * (self.max_length_tweet - len(self.tokens))
