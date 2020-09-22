IP = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
# 2) Permute 8 bits by removing the 1st 2 bits from 10 bits
Perm10_8 =[6, 3, 7, 4, 8, 5, 10, 9]
# 3) Permute 8 bits
P8 = [2, 6, 3, 1, 4, 8, 5, 7]
# 4) IP inverse
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
# 5) Expansion Table
EP = [4, 1, 2, 3, 2, 3, 4, 1]
# 6) Permute 4 bits
P4 =[2, 4, 3, 1]
# Sbox 1
s1 =[[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3],
     [0, 2, 1, 3], [3, 1, 3, 2]]
# SBox 2
s2 =[[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0],
     [2, 1, 0, 3]]

# 16 Keys are stored in this table
KEYS = []
# Get binary string of x of length n
get_bin = lambda x, n: format(x, 'b').zfill(n)


def permute(key, perm):
    p = ""
    for i in perm:
        p +=key[i-1]
    return p


def round_shift(key_left, key_right):
    rotate_left = key_left[1:]
    rotate_left += key_left[:1]

    rotate_right = key_right[1:]
    rotate_right += key_right[:1]
    return rotate_left, rotate_right


def xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b [i]:
            result += "0"
        else:
            result +="1"
    return result


def look_up_stable(bits, table):
    r = int(bits[0]+bits[3], 2)
    c = int(bits[1]+bits[2], 2)
    return get_bin(table[r][c], 2)


def generateKeys(key):
    key_string = get_bin(key, 10)
    p = permute(key_string, IP)
    key_left = p[0:5]
    key_right = p[-5:]
    rKey_left, rKey_right = round_shift(key_left, key_right)
    keyOne = permute(rKey_left+rKey_right, Perm10_8)

    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    keyTwo = permute(rKey_left+rKey_right, Perm10_8)

    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    keyThree = permute(rKey_left+rKey_right, Perm10_8)

    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    keyFour = permute(rKey_left+rKey_right, Perm10_8)

    KEYS = [keyOne, keyTwo, keyThree, keyFour]
    return KEYS


def encrypt_des(plain_text, KEYS):
    pt_bits = get_bin(plain_text, 8)
    perm_bits = permute(pt_bits, P8)
    left = perm_bits[:4]
    right = perm_bits[-4:]
    st1L, st1R = feistal(left, right, KEYS[0])
    st2L, st2R = feistal(st1L, st1R, KEYS[1])
    st3L, st3R = feistal(st2L, st2R, KEYS[2])
    st4L, st4R = feistal(st3L, st3R, KEYS[3])
    cipher = permute(st4R+st4L, IP_inv)
    return int(cipher, 2)


def decrypt_des(cipher, KEYS):
    pt_bits = get_bin(cipher, 8)
    perm_bits = permute(pt_bits, P8)
    left = perm_bits[:4]
    right = perm_bits[-4:]
    st1L, st1R = feistal(left, right, KEYS[3])
    st2L, st2R = feistal(st1L, st1R, KEYS[2])
    st3L, st3R = feistal(st2L, st2R, KEYS[1])
    st4L, st4R = feistal(st3L, st3R, KEYS[0])
    plainText = permute(st4R + st4L, IP_inv)
    return int(plainText,2)

def expand_perm(r, k):
    expand_r = permute(r, EP)
    expand_r_xor_k = xor(expand_r, k)
    e_l = expand_r_xor_k[:4]
    e_r = expand_r_xor_k[-4:]

    sleft = look_up_stable(e_l, s1)
    sright = look_up_stable(e_r, s2)
    perm4 = permute(sleft + sright, P4)
    return perm4


def feistal(left, right, k):
    l_xor_perm = xor(left, expand_perm(right, k))
    # print("Left XOR Exp_Perm(right, key): ", l_xor_perm)
    return right, l_xor_perm


def encryptText(t, key):
    t = t.lower()
    cipher = ""
    Keys = generateKeys(key)
    for p in t:
        i = encrypt_des(ord(p), Keys)
        cipher += chr(i)
    return cipher


def decryptText(c, key):
    pt=""
    Keys = generateKeys(key)
    for t in c:
        i = decrypt_des(ord(t), Keys)
        pt += chr(i)
    return pt


def get_round_14(bits, key):
    left = bits[:4]
    right = bits[-4:]
    KEYS = generateKeys(key)
    st2L, st2R = feistal(left, right, KEYS[1])
    st3L, st3R = feistal(st2L, st2R, KEYS[2])
    st4L, st4R = feistal(st3L, st3R, KEYS[3])

    return left, right, st4L, st4R


def differential_cryptanalysis(str, str_star, key):
    l1, r1, l4, r4 = get_round_14(str, key)
    l1_s, r1_s, l4_s, r4_s = get_round_14(str_star, key)
    print(r4, r4_s)
    l1_diff = xor(l1, l1_s)
    r1_diff = xor(r1, r1_s)
    l4_diff = xor(l4, l4_s)
    r4_diff = xor(r4, r4_s)
    # r4' xor l1'
    r4l1d = xor(r4_diff, l1_diff)
    # E(l4')
    el4d = permute(l4_diff, EP)
    # Sbox 1 input
    s1_input = el4d[:4]
    # Sbox 1 output
    s1_output = r4l1d[:3]
    # Sbox 2 input
    s2_input = el4d[-4:]
    # Sbox 2 output
    s2_output = r4l1d[-3:]
    # contain possible K4L
    pairs_s1 =[]
    # find pairs s1
    for i in range(0, 16):
        for j in range(0, 16):
            x = get_bin(i, 4)
            y = get_bin(j, 4)
            if xor(x, y) == s1_input:
                s1_x = look_up_stable(x, s1)
                s1_y = look_up_stable(y, s1)
                if xor(s1_x, s1_y) == s1_output:
                    pairs_s1.append(xor(x, el4_left))

    # contain possible K4R
    pairs_s2 = []
    # find pairs s2
    for i in range(0, 16):
        for j in range(0, 16):
            x = get_bin(i, 4)
            y = get_bin(j, 4)
            if xor(x, y) == s2_input:
                s2_x = look_up_stable(x, s2)
                s2_y = look_up_stable(y, s2)
                if xor(s2_x, s2_y) == s2_output:
                    pairs_s2.append(xor(y, el4_right))

    # needs to be completed...

def main():
    key = 1010
    message = 243
    print("Key: ", key)
    print("Message: ", message)
    KEYS = generateKeys(key)
    print("Generated Keys: ", KEYS[0:2])
    print("Encrypting...")
    cipher = encrypt_des(message, KEYS)
    print("Cipher: ",cipher)
    print()
    print("Decrypting...")
    decryptedM = decrypt_des(cipher, KEYS)
    print("Decrypted Message: ", decryptedM)
    #first = "11001011"
    #first_star = "10101011"
    #differential_cryptanalysis(first, first_star, key)
if __name__== "__main__":
  main()
