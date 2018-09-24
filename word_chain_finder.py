from collections import deque


def find_word_chain(word1, word2, word_graph):
    word_queue = deque([word1])
    predecessors = {}

    while word_queue:
        word = word_queue.popleft()
        # check if word in graph
        for neighbor in word_graph[word]:
            # prevent taking previous words
            if neighbor not in predecessors:
                word_queue.append(neighbor)
                predecessors[neighbor] = word
                # finsihed?
                if neighbor == word2:
                    result = [word2]
                    while result[-1] != word1:
                        result.append(predecessors[result[-1]])
                    return list(reversed(result))
    return None
