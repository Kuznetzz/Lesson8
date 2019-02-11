# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
# только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

from struct import *
import hashlib


def sha1(data):
    # based on https://codereview.stackexchange.com/questions/37648/python-implementation-of-sha1

    hex_repr = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
    k_hex = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6]
    sha_functions = [lambda a: (a[1] & a[2]) | ((~a[1]) & a[3]),
                     lambda a: a[1] ^ a[2] ^ a[3],
                     lambda a: (a[1] & a[2]) | (a[1] & a[3]) | (a[2] & a[3]),
                     lambda a: a[1] ^ a[2] ^ a[3]]

    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    message = bytearray(data, 'utf8')
    message.append(0x80)
    message.extend([0] * (63 - (len(message) + 7) % 64))
    message.extend(pack('>Q', len(data) * 8))

    for chunk in range(0, len(message), 64):
        w = list(unpack('>16L', message[chunk: chunk + 64]))
        for i in range(16, 80):
            w.append(rol((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1))

    a = hex_repr[:]

    for i in range(4):
        for j in range(20):
            a = [rol(a[0], 5) + sha_functions[i](a) + a[4] + k_hex[i] + w[
                i * 20 + j] & 0xffffffff, a[0], rol(a[1], 30), a[2], a[3]]
    for i in range(5):
        hex_repr[i] += a[i] & 0xffffffff
    return "".join(list(hex(i)[-8:] for i in hex_repr))


def count_all_substring(string):
    b = []
    c = []  # for testing
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            h = sha1(string[i:j])
            if h not in b:
                b.append(h)
                c.append(string[i:j])  # for testing
    assert len(c) == len(b) == len(set(b)) == len(set(c))  # for testing
    # print(c)
    return (f"'{string}' has {len(b)} substrings\n")


print(count_all_substring("abracadabra"))
print(count_all_substring("alice in wonderland"))
print(count_all_substring(" 1 2 3"))

print("testing sha1 function:\n")
string = "I want to know "
qqq = string.encode('utf8')
print(sha1(string))
print(hashlib.sha1(qqq).hexdigest())
print("Short  string is ok , but long string is wrong , i dont understand why: ")
string = "For when you know you are reinventing the wheel, but are doing it \
         anyways. Questions with this tag involve code that is already fully \
         implemented (such as from a library)"
qqq = string.encode('utf8')
print(sha1(string))
print(hashlib.sha1(qqq).hexdigest())
