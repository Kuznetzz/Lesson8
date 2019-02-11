# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
from collections import Counter


def Huffman_compression(my_string):
    def freq_count(string):
        a = Counter(string)
        return sorted([[a[i], i] for i in a])

    def combine_nodes(nodes):
        if len(nodes) > 1:
            nodes.sort()
            nodes[0].append("0")
            nodes[1].append("1")
            nodes = [[nodes[0][0] + nodes[1][0], nodes[0][1] + nodes[1][1]]] + nodes[2:]
            huffman_tree.append(nodes)
            combine_nodes(nodes)
        return huffman_tree

    def sort_remove():
        huffman_tree.sort(reverse=True)
        checklist = []
        for level in huffman_tree:
            for node in level:
                if node not in checklist:
                    checklist.append(node)
                else:
                    level.remove(node)
        return checklist

    def binary_dict(my_dict={}):
        if len(only_letters) == 1:
            my_dict[only_letters[0]] = "0"
        else:
            for letter in only_letters:
                lettercode = ""
                for node in checklist:
                    if len(node) > 2 and letter in node[1]:
                        lettercode += node[2]
                my_dict[letter] = lettercode
        return my_dict

    len_my_string = len(my_string) * 8
    nodes = freq_count(my_string)
    huffman_tree = [nodes[:]]
    only_letters = [i[1] for i in nodes]
    combine_nodes(nodes)
    checklist = sort_remove()
    binary_dict = binary_dict()
    binary = "".join(binary_dict[character] for character in my_string)

    print(f"'{my_string}' in binary is:\n{binary}")
    print(f"Original string has {len_my_string} bites, compressed has {len(binary)} bites \n\
    You save {len_my_string - len(binary)} bits with {round(len_my_string / len(binary), 2)} compressing ratio.")
    print(f"Binary dictionary for '{my_string}':")
    for letter in binary_dict:
        print(f"{letter}    |    {binary_dict[letter]}")
    print()
    return [binary, binary_dict]


def Huffman_decompression(binary, binary_dict):
    if binary:
        code = ''
        for digit in binary:
            code += digit
            for i in binary_dict:
                if code == binary_dict[i]:
                    return i + Huffman_decompression(binary[len(code):], binary_dict)
    return ""


def testing(string_list):
    for my_string in string_list:
        binary, binary_dict = Huffman_compression(my_string)
        uncom = Huffman_decompression(binary, binary_dict)
        assert my_string == uncom, f"{my_string} != {uncom}"
        print(f"Uncompressed string is '{uncom}'")
        print()


strings = ["she sells sea shells", "i know what you think", "People everywhere", "ехал грека через реку", "a"]
testing(strings)
