class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            prev_node = self.head
            for elem in nodes:
                node.next = Node(elem)
                node = node.next
                node.previous = prev_node
                prev_node = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, node):
        self.head.previous = node
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        node.previous = current_node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty!")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next.previous = new_node
                node.next = new_node
                new_node.previous = node
                return

        raise Exception("Node with data %s not found!" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty!")

        if self.head.data == target_node_data:
            self.add_first(new_node)
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.previous = prev_node
                node.previous = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data %s not found!" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty!")

        if self.head == target_node_data:
            self.head = self.head.next
            self.head.previous = None
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                node.next.previous = prev_node
                return
            prev_node = node

        raise Exception("Node with data %s not found!" % target_node_data)


llist = LinkedList(["a", "b", "c"])

llist.add_first(Node("1"))
llist.add_first(Node("2"))

llist.add_last(Node("e"))
llist.add_last(Node("f"))

llist.add_after("2", Node("1.4"))

llist.add_before("e", Node("d"))
llist.remove_node("a")

for node in llist:
    print("prev: {}, current: {}, next: {}".format(
        "None" if not node.previous else node.previous.data, node.data, "None" if not node.next else node.next.data))
