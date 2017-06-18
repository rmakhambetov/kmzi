
def p_and_q(n):
    data = []
    for i in range(2, n):
        if n % i == 0:
            data.append(i)
    return tuple(data)


def euler(p, q):
    return (p - 1) * (q - 1)


def private_index(e, euler_v):
    for i in range(2, euler_v):
        if i * e % euler_v == 1:
            return i


def decipher(d, n, c):
    return c ** d % n


def main():
    LETTERS = """абвгдежзийклмнопрстуфхцчшщъыьэюя""".upper()
    dict = {LETTERS.index(i)+(128):i for i in LETTERS}
    C = 3519671666
    K = (3574122301, 3967)
    binary = bin(C)[2:]
    symbols = tuple(int('0b'+binary[0+i:i+8], 2) for i in range(len(binary)) if i%8==0)
    # word = ''.join([dict[i] for i in symbols])
    # print(binary,symbols)
    e = 3967
    n = 3574122301
    for i in symbols:
        c = i

        p_and_q_v = p_and_q(n)
        # print("[p_and_q]: ", p_and_q_v)

        euler_v = euler(p_and_q_v[0], p_and_q_v[1])
        # print("[euler]: ", euler_v)

        d = private_index(e, euler_v)
        # print("d: ", d)

        # print("private key: ", (d, n))

        plain = decipher(d, n, c)
        print("plain: ", plain)


if __name__ == "__main__":
    main()