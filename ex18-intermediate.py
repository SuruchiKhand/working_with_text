# DATA BLOCK

text = """he really really loves coffee
my sister dislikes coffee
my sister loves tea"""

import math


def main(text):
    # split the text first into lines and then into list of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'[0] contains the term frequence of the word 'he' in the first document
        tf[word] = [doc.count(word) / len(doc) for doc in docs]

        # df:number of documents containing word w
        df[word] = sum([word in doc for doc in docs]) / N

        # loop through documents to calculate tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # TF-IDF = TF * IDF, where IDF = log10(N / DF)
            # Note: df[word] is already DF/N, so we need to multiply by N to get back DF
            idf = math.log(1 / df[word], 10)
            tfidf_value = tf[word][doc_index] * idf
            tfidf.append(tfidf_value)
        print(tfidf)


main(text)
