from Word import *


class Node:
    # to complete
    def __init__(self, word, index=0):
        self.word = word
        self.left = None
        self.right = None
        # self.index = index


class DictionaryBST:
    # to complete
    def __init__(self):
        self.root = None
        self.node_count = 0
        self.max_level = 0

    def load(self, filename):
        file_path = filename+'.txt'
        with open(file_path, 'r') as file:
            for line in file:
                word = line.strip().split('\n')[0]
                word_obj = Word(word, filename)
                self.insert(word_obj)

    def insert(self, word_obj):
        if self.root is None:
            self.root = Node(word_obj, 0)
            self.node_count += 1
        else:
            self._rec_insert(self.root, word_obj, 0, 0)

    def _rec_insert(self, node, word_obj, current_level, index):
        if word_obj.getWord() < node.word.getWord():
            if node.left is None:
                node.left = Node(word_obj, 2 * index + 1)
                self.node_count += 1
                self.max_level = max(self.max_level, current_level + 1)
            else:
                self._rec_insert(node.left, word_obj, current_level + 1, 2 * index + 1)
        else:
            if node.right is None:
                node.right = Node(word_obj, 2 * index + 2)
                self.node_count += 1
                self.max_level = max(self.max_level, current_level + 1)
            else:
                self._rec_insert(node.right, word_obj, current_level + 1, 2 * index + 2)

    def getSize(self):
        return self.node_count

    def getMaxLevel(self):
        return self.max_level

    def extractInOrder(self):
        result = []
        self._inOrder(self.root, result)
        return result

    def _inOrder(self, node, result):
        if node is None:
            return

        self._inOrder(node.left, result)
        result.append(node.word)
        self._inOrder(node.right, result)

    def show(self, node=None, level=0, option='word'):
        if node is None:
            node = self.root

        else:
            self.show(node.right, level + 1, option)
            print(' ' * (level * 4) + str(getattr(node.word, option)))
            self.show(node.left, level + 1, option)

    def search(self, word):
        return self._search_iterative(self.root, word)

    def _search_iterative(self, node, word):
        stack = []
        while node or stack:
            while node:
                if node.word.word == word:
                    return node.word
                elif word < node.word.word:
                    stack.append(node)
                    node = node.left
                else:
                    node = node.right
            if stack:
                node = stack.pop()
        return None
