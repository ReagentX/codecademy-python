'''
Convert from HEX to RGB and back again
Written in Python 3, this will not work on CodeCademy
CodeCademy used Python 2.7 when I wrote this
'''


def rgb_hex():
    red = validate_rgb('red')
    green = validate_rgb('green')
    blue = validate_rgb('blue')
    val = hex((red << 0b10000) + (green << 0b1000) + blue)
    print(val[2:])


def hex_rgb():
    hex_val = int(validate_hex(), 16)
    two_hex = 2 ** 8
    blue = hex_val % two_hex
    hex_val = hex_val >> 0b1000
    green = hex_val % two_hex
    hex_val = hex_val >> 0b1000
    red = hex_val % two_hex
    print(f'{red}, {green}, {blue}')


def validate_hex():
    invalid_msg = 'Not valid hex!'
    hex_val = input('Enter a hex: ')
    while len(hex_val) != 6:
        print(invalid_msg)
        hex_val = input('Enter a hex: ')
    return hex_val


def validate_rgb(color: str):
    invalid_msg = 'Not valid RGB!'
    n = int(input(f'Enter a value for {color}: '))
    check = False if n <= 255 and n >= 0 else True
    while check:
        print(invalid_msg)
        n = int(input(f'Enter a value for {color}: '))
        check = False if n <= 255 and n >= 0 else True
    return n


def convert():
    while True:
        option = input('Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ')
        if option == 'X':
            break
        elif option == '1':
            rgb_hex()
        elif option == '2':
            hex_rgb()
        else:
            print('Error')


convert()
