from sys import argv
from math import ceil


def main():
    file_path = argv[1]
    file = open(file_path, 'r')

    output_file_path = argv[1].replace('.txt', '_out.txt')
    output_file = open(output_file_path, 'w')

    sequence_number = int(file.readline().rstrip())

    # Jump empty line
    file.readline()

    for i in range(sequence_number):
        tree = MaxesTree()
        sequence_values = []
        data_number = int(file.readline().rstrip())
        number_of_lines = ceil(data_number / 10.0)

        for j in range(number_of_lines):
            line = file.readline().rstrip()
            sequence_values.extend(map(int, line.split()))
        # Jump empty line
        file.readline()

        # Build tree
        tree.build_tree(sequence_values)

        # Write header in file
        output_file.write(f'Sequence {i + 1}\n')

        # Traverse tree pre order
        pre_order_result = tree.traverse_tree_pre_order()
        output_file.write(f'Pre Order\n')
        for num in pre_order_result:
            output_file.write(f'{num} ')
        output_file.write('\n')

        # Traverse tree in order
        in_order_result = tree.traverse_tree_in_order()
        output_file.write(f'In Order\n')
        for num in in_order_result:
            output_file.write(f'{num} ')
        output_file.write('\n')

        # Traverse tree post order
        post_order_result = tree.traverse_tree_post_order()
        output_file.write(f'Post Order\n')
        for num in post_order_result:
            output_file.write(f'{num} ')
        output_file.write('\n')

        # empty line to separate sequences
        output_file.write('\n')

    file.close()
    output_file.close()


class MaxesTree():
    def __init__(self):
        self.root = None

    def build_tree(self, array):
        if len(array) <= 0:
            return None
        max_value = max(array)
        max_index = array.index(max_value)

        # set entire tree root (only done the first time)
        if self.root == None:
            self.root = Node(max_value, None, None)

        left_sublist = array[:max_index]
        left_root = self.build_tree(left_sublist)

        right_sublist = array[max_index + 1:]
        right_root = self.build_tree(right_sublist)

        if self.root.value == max_value:
            self.root = Node(max_value, left_root, right_root)
        else:
            return Node(max_value, left_root, right_root)

    def traverse_tree_in_order(self):
        result = []
        self.root.traverse_in_order(result)
        return result

    def traverse_tree_pre_order(self):
        result = []
        self.root.traverse_pre_order(result)
        return result

    def traverse_tree_post_order(self):
        result = []
        self.root.traverse_post_order(result)
        return result


class Node():
    def __init__(self, value, left_child, right_child):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def traverse_in_order(self, result):
        if self.left_child != None:
            self.left_child.traverse_in_order(result)

        result.append(self.value)

        if self.right_child != None:
            self.right_child.traverse_in_order(result)

    def traverse_pre_order(self, result):
        result.append(self.value)

        if self.left_child != None:
            self.left_child.traverse_pre_order(result)

        if self.right_child != None:
            self.right_child.traverse_pre_order(result)

    def traverse_post_order(self, result):
        if self.left_child != None:
            self.left_child.traverse_post_order(result)

        if self.right_child != None:
            self.right_child.traverse_post_order(result)

        result.append(self.value)


main()
