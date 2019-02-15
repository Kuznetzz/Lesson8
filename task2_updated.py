# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
from collections import Counter


def huffman_compression(my_string):
    def combine_nodes(nodes, huf_tree=[], c_list=[], my_dict={}):
        huf_tree += [nodes]
        if len(nodes) > 1:
            nodes.sort(), nodes[0].append("0"), nodes[1].append("1")
            combine_nodes([[nodes[0][0] + nodes[1][0], nodes[0][1] + nodes[1][1]]] + nodes[2:], huf_tree)
        else:
            huf_tree.sort(reverse=True)
            for level in huf_tree:
                for node in level:
                    if node not in c_list: c_list.append(node)
            print(f"Binary dictionary for '{my_string}':")
            for l in let:
                my_dict[l] = ''.join([n[2] for n in c_list if len(n) > 2 and l in n[1]]) if len(let) > 1 else "0"
                print(f"{l}    |    {my_dict[l]}")
        return [my_dict, "".join(my_dict[char] for char in my_string)]

    temp = Counter(my_string)
    u = sorted([[temp[i], i] for i in temp])
    let = [i[1] for i in u]
    binary_dict, binary = combine_nodes(u)

    print(f"'{my_string}' in binary is:\n{binary}")
    print(f"Original string has {len(my_string) * 8} bites, compressed has {len(binary)} bites \n\
    You save {len(my_string) * 8 - len(binary)} bits with {round(len(my_string) * 8 / len(binary), 2)} compres ratio.")

    return [binary, binary_dict]


def huffman_decompression(binary, binary_dict):
    if binary:
        code = ''
        for digit in binary:
            code += digit
            for i in binary_dict:
                if code == binary_dict[i]:
                    return i + huffman_decompression(binary[len(code):], binary_dict)
    return ""


def testing(string_list):
    for my_string in string_list:
        binary, binary_dict = huffman_compression(my_string)
        uncom = huffman_decompression(binary, binary_dict)
        assert my_string == uncom, f"{my_string} != {uncom}"
        print(f"Uncompressed string is '{uncom}'")
        print()


strings = ["she sells sea shells", "i know what you think", "People everywhere", "ехал грека через реку", "a"]
testing(strings)
