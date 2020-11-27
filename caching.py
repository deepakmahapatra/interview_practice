import collections


class Node:
    def __init__(self, key, value, count):
        self.key = key
        self.value = value
        self.count = count


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}
        self.count_to_node = collections.defaultdict(collections.OrderedDict)
        self.min_count = None

    def get(self, key):
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        del self.count_to_node[node][key]

        if not self.count_to_node[node.count]:
            del self.count_to_node[node.count]
            if node.count == self.min_count:
                self.min_count += 1
        node.count += 1
        self.key_to_node[key] = node
        self.count_to_node[node.count][key] = node
        return node.value

    def put(self, key, value):
        if not self.capacity:
            return
        if key in self.key_to_node:
            self.key_to_node[key].value = value
            self.get(key)
            return
        if len(self.key_to_node) == self.capacity:
            k,v = self.count_to_node[self.min_count].popitem(last=False)
            del self.key_to_node[k]
        self.min_count = 1
        self.count_to_node[1][key] = Node(key, value, 1)
        self.key_to_node[key] = Node(key, value, 1)
        return


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = collections.OrderedDict()

    def get(self, key):
        if key not in self.key_to_node:
            return None
        self.key_to_node.move_to_end(key)
        return self.key_to_node[key]

    def put(self, key, value):
        if self.capacity == len(self.key_to_node):
            return
        if key in self.key_to_node:
            self.key_to_node[key] = value
            self.get(key)
            return
        if len(self.key_to_node) == self.capacity:
            self.key_to_node.popitem(last=False)
        self.key_to_node[key] = value
        return



