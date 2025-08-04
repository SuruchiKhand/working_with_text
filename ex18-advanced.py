import numpy as np
import math

text = """Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again"""


def main(text):
    # Splits text into lines, converts to lowercase, and split into words
    docs = [line.lower().split() for line in text.split("\n")]

    # Create a vocabulary of unique words across all documents
    vocabulary = list(set(word for doc in docs for word in doc))

    N = len(docs)  # Number of documents

    # For each word and document, calculate term frequency
    tf = {}
    df = {}

    # Calculate TF for each document
    for word in vocabulary:
        tf[word] = []
        for doc in docs:
            word_count = doc.count(word)
            doc_length = len(doc)
            tf[word].append(word_count / doc_length if doc_length > 0 else 0)

        # Calculate DF -counts how many document contain each word
        documents_containing_word = sum(1 for doc in docs if word in doc)
        df[word] = documents_containing_word

    # Calculate TF-IDF representation for each line
    tfidf_vectors = []

    for doc_index in range(N):
        tfidf_vector = []
        for word in vocabulary:
            if df[word] > 0:
                idf = math.log(N / df[word], 10)
            else:
                idf = 0

            # Calculate TF - IDF
            tfidf_value = tf[word][doc_index] * idf
            tfidf_vector.append(tfidf_value)

        tfidf_vectors.append(tfidf_vector)

    # Calculate distance between each pair of lines to find the closest
    dist = np.empty((N, N), dtype=float)

    for i in range(N):
        for j in range(N):
            if i == j:
                # Set diagonal to infinity to avoid self-comparison
                dist[i, j] = np.inf
            else:
                # Calculate Manhattan distance between TF-IDF vectors
                distance = sum(
                    abs(tfidf_vectors[i][k] - tfidf_vectors[j][k])
                    for k in range(len(vocabulary))
                )
                dist[i, j] = distance

    # Find the minimum distance pair
    min_indices = np.unravel_index(np.argmin(dist), dist.shape)
    print(min_indices)


main(text)
