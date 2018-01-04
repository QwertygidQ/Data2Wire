import encoding_algorithms
import matplotlib.pyplot as plt

enc_NRZ, enc_NRZI, enc_manch, enc_diff_manch, enc_MLT3, enc_2B1Q = \
    1, 2, 3, 4, 5, 6


def get_encoding_choice():
    print('1) NRZ')
    print('2) NRZI')
    print('3) Manchester')
    print('4) Differential Manchester')
    print('5) MLT3')
    print('6) 2B1Q\n')

    return int(input('Enter your choice: '))


def string_to_binary(string):
    return [int(bit) for bit in ''.join(format(ord(ch), 'b') for ch in string)]


def read_data():
    binary = (input('Is your data binary? (Y/n) ').lower() != 'n')
    data = input('Input data: ')

    if binary:
        for ch in data:
            if ch != '0' and ch != '1':
                raise ValueError('Data is not binary')

        return [int(bit) for bit in data]
    else:
        return string_to_binary(data)


def main():
    while True:
        print('Data2Wire by Qwertygid, 2017\n')
        encoding = get_encoding_choice()
        if encoding < enc_NRZ or encoding > enc_2B1Q:
            print("Invalid choice\n")
            continue

        try:
            data = read_data()
        except ValueError as err:
            print(err)
            print()
            continue

        if encoding == enc_NRZ:
            encoding_algorithms.encoding_NRZ(data)
        elif encoding == enc_NRZI:
            encoding_algorithms.encoding_NRZI(data)
        elif encoding == enc_manch:
            encoding_algorithms.encoding_MANCH(data)
        elif encoding == enc_diff_manch:
            encoding_algorithms.encoding_DMANCH(data)
        elif encoding == enc_MLT3:
            encoding_algorithms.encoding_MLT3(data)
        elif encoding == enc_2B1Q:
            try:
                encoding_algorithms.encoding_2B1Q(data)
            except ValueError as err:
                print(err)
                print()
        else:
            raise RuntimeError("You somehow got past the encoding check. Report this, please")

        plt.show()
        print()


if __name__ == '__main__':
    main()
