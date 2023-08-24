import pyperclip

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_mode():
    while True:
        response = input('Do you want to (e)ncrypt or (d)ecrypt?\n> ').lower()
        if response.startswith('e'):
            return 'encrypt'
        elif response.startswith('d'):
            return 'decrypt'
        print('Please enter the letter e or d.')


def get_key():
    max_key = len(SYMBOLS) - 1
    while True:
        response = input(f'Please enter the key (0 to {max_key}) to use.\n> ')
        if response.isdigit():
            key = int(response)
            if 0 <= key < len(SYMBOLS):
                return key
        print('Invalid key. Please enter a valid key.')


def process_message(mode, message, key):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            if mode == 'encrypt':
                num = (num + key) % len(SYMBOLS)
            elif mode == 'decrypt':
                num = (num - key) % len(SYMBOLS)
            translated += SYMBOLS[num]
        else:
            translated += symbol
    return translated


def main():
    print('The Caesar cipher encrypts letters by shifting them over by a')
    print('key number. For example, a key of 2 means the letter A is')
    print('encrypted into C, the letter B encrypted into D, and so on.\n')

    mode = get_mode()
    key = get_key()

    message = input(f'Enter the message to {mode}.\n> ').upper()

    translated = process_message(mode, message, key)

    print(translated)

    try:
        pyperclip.copy(translated)
        print(f'Full {mode}ed text copied to clipboard.')
    except ImportError:
        pass  # Do nothing if pyperclip wasn't installed.


if __name__ == '__main__':
    main()
