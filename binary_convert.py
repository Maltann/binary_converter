def binary_to_decimal(number_binary):
    str_bin = str(number_binary)
    decimal = 0
    bits_number = len(str_bin)
    reverse_bin = ''.join(reversed(str_bin))
    for i in range(bits_number):
        if reverse_bin[i] == '1':
            decimal += 2 ** i
    return decimal

def decimal_to_binary(number_decimal):
    binary_number = ''
    while number_decimal != 0:
        remaider = str(number_decimal % 2)
        number_decimal = number_decimal // 2
        binary_number = binary_number + remaider
    binary_number = ''.join(reversed(binary_number))
    return binary_number

replay = "yes"

while replay == 'yes':
    what_todo = int(input("Choose what todo : \n1 for binary -> decimal \n2 for decimal -> binary\n"))
    if what_todo == 1:
        number = int(input("Enter number in binary"))
        print(binary_to_decimal(number))
    elif what_todo == 2:
        number = int(input("Enter number in decimal"))
        print(decimal_to_binary(number))
    else:
        print("IDIOT")
        break
    replay = input("Do you want to make another conversion ? (yes or no)")
exit()
