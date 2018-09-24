import load_four_words_graph as four_words
import load_345_words_graph as words_345
import word_chain_finder as finder


def main():
    graph_4_words = four_words.load_graph()
    graph_345_words = words_345.load_graph()
    while True:
        chain_opt = raw_input("Enter 1 for 4-words chain or 2 for 345-words chain: \n")
        if chain_opt == '1':
            word1 = raw_input("Enter Start Word: \n")
            word2 = raw_input("Enter End Word: \n")
            if word1 == word2:
                print("Words are same. Chain length is 0\n")
                continue
            if len(word1) != len(word2):
                print("Words must be of same length. Chain length is 0\n")
                continue
            print('Shortest path between "%s" and "%s" using 4-words graph is:' % (word1, word2))
            chain = finder.find_word_chain(word1, word2, graph_4_words)
            if not None:
                print(" -> ".join(chain))
                print("Chain length is " + str(len(chain)-1))
        elif chain_opt == '2':
            word1 = raw_input("Enter Start Word: \n")
            word2 = raw_input("Enter End Word: \n")
            if word1 == word2:
                print("Words are same. Chain length is 0\n")
                continue
            if len(word1) != len(word2):
                print("Words must be of same length. Chain length is 0\n")
                continue
            print('Shortest path between "%s" and "%s" using 4-words graph is:' % (word1, word2))
            chain = finder.find_word_chain(word1, word2, graph_345_words)
            if not None:
                print(" -> ".join(chain))
                print("Chain length is " + str(len(chain) - 1))
        else:
            print("Please enter a valid input (1 or 2).\n")


if __name__ == '__main__':
    main()