import struct 

def float_to_binary(number):
    [d] = struct.unpack(">Q", struct.pack(">d", number))
    return f'{d:064b}'

def integer_to_binary(number):
    binary = bin(number).replace("0b", "")
    return binary

if __name__ == "__main__":
    print(float_to_binary(3.14))
    print(integer_to_binary(45))