def Pre_Processing(string,arg1=100,arg2=1000):
    text = string
    max_length_tweet = arg1
    max_length_dict = arg2

    # remove urls and html tags
    import re
    from bs4 import BeautifulSoup
    text = BeautifulSoup(text).get_text() # remove html tags
    text = re.sub(r'RT','',text)
    text = re.sub(r"http\S+", "", text, flags=re.MULTILINE) # remove urls

    # tokenize
    from nltk.tokenize import TweetTokenizer
    ttk = TweetTokenizer(strip_handles=True, reduce_len=True)
    tweet_tokenize = ttk.tokenize(text)

    # # delete stopwords and numbers
    # from nltk.corpus import stopwords
    # lowercase_words = [word.lower() for word in tweet_tokenize
    #                       if word not in stopwords.words() and word.isalpha()] # delete stopwords and numbers
    # lowercase_words

    # # lemmatize, but nothing changed
    # from nltk.stem import WordNetLemmatizer

    # lemmatizer = WordNetLemmatizer()
    # lemma = [lemmatizer.lemmatize(word) for word in lowercase_words]
    # lemma

    # load embedding dict
    length = len(tweet_tokenize)
    token_index = np.zeros(length)
    i = 1
    embeddings_dict = {}
    with open("glove.twitter.27B.25d.txt", 'r', encoding="utf-8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            if word in tweet_tokenize:
                if len(embeddings_dict) <= max_length_dict:
                    embeddings_dict[word] = i
            i += 1

    # replace tokens with indexes
    for j in range(length):
        if tweet_tokenize[j] in embeddings_dict:
            token_index[j] = embeddings_dict[tweet_tokenize[j]]
    token_index = token_index[token_index != 0] # remove 0s

    token_index = token_index.astype("int").tolist()

    # padding
    if len(token_index) >= max_length_tweet:
        index = token_index[:max_length_tweet]
    else:
        index = [0]*max_length_tweet
        index[:len(token_index)] = token_index
    
    return index