import streamlit as st


def load_vocab(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab("vocab.txt")
# print(vocabs)


def levenshtein_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    levent = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m + 1):
        levent[i][0] = i

    for j in range(1, n + 1):
        levent[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j - 1]:
                levent[i][j] = levent[i-1][j-1]
            else:
                levent[i][j] = min(
                    levent[i-1][j-1], levent[i-1][j], levent[i][j-1]) + 1

    return levent[m][n]


# def main():
st.title("Word Correction using Levenshtein Distance")
word = st.text_input('Word:')

if st.button("Compute"):
    # compute levenshtein Distance
    leven_distances = dict()

    for vocab in vocabs:
        leven_distances[vocab] = levenshtein_distance(word, vocab)

    # sorted by distance
    sorted_distances = dict(
        sorted(leven_distances.items(), key=lambda item: item[1]))
    correct_word = list(sorted_distances.keys())[0]
    st.write('Correct Word: ', correct_word)

    # col1, col2 = st.columns(2)
    # col1.write('Vocabulary: ')
    # col1.write(vocabs)

    # col2.write('Distances: ')
    # col2.write(sorted_distances)
