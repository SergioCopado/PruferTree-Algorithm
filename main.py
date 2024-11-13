import Tree as Tree
import Heap as Heap

def prufer_to_tree(prufer_code):
    pair_of_nodes = []
    T = [i for i in range(0, len(prufer_code)+2)]

    deg = [1] * len(T)
    for i in prufer_code:
        deg[i-1] += 1

    for i in prufer_code:
        for j in T:
            if deg[j] == 1:
                pair_of_nodes.append((i,j + 1))
                deg[i-1] -= 1
                deg[j] -= 1
                break
    last = [i for i in T if deg[i] == 1]
    pair_of_nodes.append((last[0] + 1, last[1] + 1))
    return pair_of_nodes


def create_tree(list_edges):
    list_vertex = []

    for element in list_edges:
        if element[0] not in list_vertex:
            list_vertex.append(element[0])
        if element[1] not in list_vertex:
            list_vertex.append(element[1])

    nodes_in_tree = [None] * (len(list_edges) + 1)
    for ele in list_edges:
        parent, child = ele
        if nodes_in_tree[parent-1] is None:
            nodes_in_tree[parent-1] = Tree.Tree(parent)

        if nodes_in_tree[child-1] is None:
            nodes_in_tree[child-1] = Tree.Tree(child)

        nodes_in_tree[parent-1].append_child(nodes_in_tree[child-1])
    i = 0

    while not nodes_in_tree[i].is_root():
        i += 1
    return nodes_in_tree


def tree_to_prufer(nodes_in_tree):
    list_aux = []
    my_heap = Heap.Heap()
    prufer_code = []

    for i in nodes_in_tree:
        if i.is_leaf():
            list_aux.append(i)
    my_heap.build_heap(list_aux)

    for i in range(len(nodes_in_tree) - 2):
        min_leaf = my_heap.delete()
        parent = min_leaf.parent()
        prufer_code.append(parent.element())
        min_leaf.remove_leaf()
        if parent.is_leaf():
            my_heap.insert(parent)
    return prufer_code


def create_a_tree(list_edges):
    list_vertex = []

    for element in list_edges:
        if element[0] not in list_vertex:
            list_vertex.append(element[0])
        if element[1] not in list_vertex:
            list_vertex.append(element[1])

    nodes_in_tree = [None] * (len(list_edges) + 1)
    for ele in list_edges:
        parent, child = ele
        if nodes_in_tree[parent-1] is None:
            nodes_in_tree[parent-1] = Tree.Tree(parent)

        if nodes_in_tree[child-1] is None:
            nodes_in_tree[child-1] = Tree.Tree(child)

        nodes_in_tree[parent-1].append_child(nodes_in_tree[child-1])
    i = 0

    while not nodes_in_tree[i].is_root():
        i += 1
    return nodes_in_tree[i]


def read_trees():
    tree = []
    print('Reading the tree')
    print('=====================')
    number_of_edges = int(input('Please, enter the number of edges of the tree: '))
    for i in range(0, number_of_edges):
        print('\t Reading the vertex {}'.format(i))
        parent = int(input('\t\t Please enter the father vertex: '))
        son = int(input('\t\t Please enter the child vertex: '))
        tree.append((parent, son))
    return tree


if "name == __main__":
    print("\t\t PRüFER CODE PROGRAM")
    print('\t\t ===================')
    print('Options:')
    print('\t 1. Generate the Prüfer code for a given labeled tree')
    print('\t 2. Generate the tree associated to a given Prüfer code')
    print('\t 3. Exit the program')
    options = int(input('Please chose one option between 1 and 3: '))


    while not 1 <= options <= 3:
        options = int(input('Please chose one option between 1 and 3: '))
    if options == 1:
        print('GENERATING THE PRUFER CODE FOR A GIVEN TREE')
        list_of_edges = read_trees()
        the_tree = create_tree(list_of_edges)
        print('\n\t The generated tree is: ')
        print(create_a_tree(list_of_edges))
        prufer_code = tree_to_prufer(the_tree)
        string = ''
        for ele in prufer_code:
            string += str(ele)

        print('\t The prüfer code associated to tree is: ', string, '\n')


    elif options == 2:
        print('\n GENERATING THE TREE FROM A PRÜFER CODE')
        print('=======================================')
        string = input('Please enter a sequence of integer numbers without spaces: ')
        print('The entered Prüfer code is: ', string)
        prufer_code = []
        for a in string:
            prufer_code.append(int(a))
        tree_edges = prufer_to_tree(prufer_code)
        tree = create_a_tree(tree_edges)
        print('The generated tree in preorder is: ', tree, '\n')

