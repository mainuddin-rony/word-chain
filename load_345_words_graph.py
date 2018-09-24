def load_words_from_file(files):
    all_words = []
    for file in files:
        words = open(file, 'r').read().split('\n')
        words.remove("")
        all_words += words
    return all_words


def distance_of_one(test):
    distance = 0
    for a, b in test:
        if a != b:
            distance += 1
            if distance > 1:
                # break early
                return False

    # true if distance is 1
    return distance == 1


def check_is_shrunk_or_expanded(word1, word2, size_w1, size_w2):
    if size_w1 == 0: return True
    if size_w2 == 0: return False

    if word1[size_w1 - 1] == word2[size_w2 - 1]:
        return check_is_shrunk_or_expanded(word1, word2, size_w1 - 1, size_w2 - 1)
    return check_is_shrunk_or_expanded(word1, word2, size_w1, size_w2 - 1)


def is_expanded_or_shrunk(word, test_word):
    if (len(word) - len(test_word) == 2) or (len(word) - len(test_word) == -2):
        return False
    if len(word) - len(test_word) == 1:
        word1 = test_word
        word2 = word
        return check_is_shrunk_or_expanded(word1, word2, len(word1), len(word2))
    if len(word) - len(test_word) == -1:
        word1 = word
        word2 = test_word
        return check_is_shrunk_or_expanded(word1, word2, len(word1), len(word2))


def get_words_close(word, all_words):
    result = set()
    for test_word in all_words:
        if len(word) == len(test_word):
            if distance_of_one(zip(word, test_word)):
                result.add(test_word)
        else:
            if is_expanded_or_shrunk(word, test_word):
                result.add(test_word)
    return result


def build_word_graph(words):
    # return {'tree': get_words_close('tree', words)}
    return {w: get_words_close(w, words) for w in words}


def load_graph():
    files = ['three_lc.txt', 'four_lc.txt', 'five_lc.txt']
    print("Using the dictionaries named " + ", ".join(files))
    words = load_words_from_file(files)
    graph = build_word_graph(words)
    return graph
