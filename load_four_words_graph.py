def load_words_from_file(file_name):
    words = open(file_name, 'r').read().split('\n')
    words.remove("")
    return words


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


def get_words_close(word, all_words):
    result = set()
    for test_word in all_words:
        if distance_of_one(zip(word, test_word)):
            result.add(test_word)
    return result


def build_word_graph(words):
    return {w: get_words_close(w, words) for w in words}


def load_graph():
    file_name = 'old_four.txt'
    print("Using the dictionary named " + file_name)
    words = load_words_from_file(file_name)
    graph = build_word_graph(words)
    return graph
