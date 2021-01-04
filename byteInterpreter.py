import binascii

#EXTERNAL : Boiler plate code
def textToBits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def textToByteTable(text, split=32):
    bits = textToBits(text)
    table = []
    for i in range(len(bits)//split):
        table.append(bits[i*split:split*(i+1)])
    return table

def textFromBits(bits, encoding='utf-8', errors='surrogatepass'):
    string = ""
    for i in range(len(bits)//8):
        try:
            string = string + getChar(bits[i*8:(i+1)*8], encoding, errors)
        except Exception as e:
            print(e)
            string = string + "-"
    return string


def getChar(byte, encoding, errors):
    n = int(byte,2)
    return n.to_bytes((n.bit_length()+7) // 8, 'big').decode(encoding, errors) or '\0'
