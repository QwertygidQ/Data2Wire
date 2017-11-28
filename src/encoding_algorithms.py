import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def setup_plot():
    plt.margins(0.01)
    plt.gca().xaxis.grid(True, linestyle='dashed')
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))  # makes interval between ticks equal to 1
    plt.gca().set_xticklabels([])
    plt.xlabel('Time')
    plt.ylabel('Voltage')


def encoding_NRZ(data):
    data.append(data[-1])

    setup_plot()
    plt.plot(data, drawstyle='steps-post')
    plt.title('NRZ')
    plt.yticks([0, .5, 1], ['-U', '0V', '+U'])


def encoding_NRZI(data):
    level = False
    for bit in range(0, len(data)):
        if data[bit]:
            level = not level

        data[bit] = int(level)

    setup_plot()
    plt.plot(data, drawstyle='steps-post')
    plt.title('NRZI')
    plt.yticks([0, .5, 1], ['-U', '0V', '+U'])


def encoding_MANCH(data):
    formatted_data = [.5, .5]
    for bit in data:
        if bit:
            formatted_data.append(1)
            formatted_data.append(0)
        else:
            formatted_data.append(0)
            formatted_data.append(1)

    setup_plot()
    plt.plot(formatted_data, drawstyle='steps-pre')
    plt.title('Manchester')
    plt.yticks([0, .5, 1], ['-U', '0V', '+U'])


def encoding_DMANCH(data):
    formatted_data = [.5, .5, 1]
    for bit in data:
        last = formatted_data[-1]
        if bit:
            formatted_data.append(last)
            formatted_data.append(not last)
        else:
            formatted_data.append(not last)
            formatted_data.append(last)

    setup_plot()
    plt.plot(formatted_data, drawstyle='steps-pre')
    plt.title('Differential Manchester')
    plt.yticks([0, .5, 1], ['-U', '0V', '+U'])


def encoding_MLT3(data):
    formatted_data = [.5, .5]
    level = level_delta = .5
    for bit in data:
        if bit:
            level += level_delta
            if level > 1 or level < 0:
                level_delta = -level_delta
                level += 2 * level_delta

        formatted_data.append(level)

    setup_plot()
    plt.plot(formatted_data, drawstyle='steps-pre')
    plt.title('MLT-3')
    plt.yticks([0, .5, 1], ['-U', '0V', '+U'])


def encoding_2B1Q(data):
    if len(data) % 2 != 0:
        raise ValueError("Data stream length should be a multiple of 2 for 2B1Q encoding")

    formatted_data = []

    for pair in zip(data[0::2], data[1::2]):
        print(pair)
        if pair == (0, 0):
            formatted_data.append(0)
        elif pair == (0, 1):
            formatted_data.append(1)
        elif pair == (1, 1):
            formatted_data.append(2)
        else:
            formatted_data.append(3)

    setup_plot()
    plt.plot(formatted_data, drawstyle='steps-pre')
    plt.title('2B1Q')
    plt.yticks([0, 1, 2, 3], ['-3V', '-1V', '1V', '3V'])
