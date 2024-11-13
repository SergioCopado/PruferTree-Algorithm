class Tree:

    def __init__(self, ele=None):
        self.__element = ele
        self.__parent = None
        self.__children = None
        self.__right_sibling = None

    def __str__(self):
        string = '<' + str(self.__element)
        aux = self.leftmost_child()
        while aux is not None:
            string += aux.__str__()
            aux = aux.right_sibling()
        string += '>'
        return string

    def element(self):
        return self.__element

    def parent(self):
        return self.__parent

    def size(self):
        if self.is_leaf():
            return 1
        aux_size = 1
        collector = self.__children
        while collector is not None:
            aux_size += collector.size()
            collector = collector.right_sibling()
        return aux_size

    def is_empty(self):
        return self.__element

    def is_root(self):
        return self.__parent is None

    def leftmost_child(self):
        return self.__children

    def right_sibling(self):
        return self.__right_sibling

    def is_leaf(self):
        return self.__children is None

    def remove_leaf(self):
        if self.is_leaf():
            parent = self.__parent
            sibl = self.__right_sibling
            if parent.leftmost_child() is self:
                parent.__children = sibl
            else:
                child = parent.leftmost_child()
                while child.right_sibling() != self:
                    child = child.right_sibling()
                child.__right_sibling = sibl

    def append_child(self, child):
        child.__parent = self
        if self.__children is None:
            self.__children = child
        else:
            temporal = self.__children
            while temporal.right_sibling() is not None:
                temporal = temporal.right_sibling()
            temporal.__right_sibling = child

    def minimum_label_leaf(self):
        if self.is_leaf():
            return self
        aux = self.leftmost_child()
        minimum = aux.minimum_label_leaf()
        aux = aux.right_sibling()
        while aux is not None:
            if minimum.element() > aux.minimum_label_leaf().element():
                minimum = aux.minimum_label_leaf
            aux = aux.right_sibling
        return minimum

    def preorder(self, order):
        order.append('<')
        order.append(self.__element)
        aux = self.__children
        while aux is not None:
            aux.preorder(order)
            aux = aux.right_sibling()
        order.append('>')
        return order

    def postorder(self, order):
        order.append('<')
        aux = self.__children
        while aux is not None:
            aux.postorder(order)
            aux = aux.right_sibling()
        order.append(self.__element)
        order.append('>')
        return order

    def inorder(self, order):
        if self.is_leave():
            order.append(self.__element)
        else:
            self.leftmost_child().inorder(order)
            order.append(self.__element)
            aux = self.__children.right_sibling()
            while aux is not None:
                aux.inorder(order)
                aux = aux.right_sibling()
        return order

    def __gt__(self, other):
        return self.__element > other.__element
