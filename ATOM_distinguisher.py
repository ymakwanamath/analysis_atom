
import matplotlib.pyplot as plt
import numpy as np
import secrets
import random
class ATOMCipher:
    def __init__(self, key, iv):
        self.key=[(key >> (127-i))&1 for i in range(128)]
        self.iv=[(iv >> (127-i)) & 1 for i in range(128)]
        #nfsr Initialization
        self.n=[(iv >> (89 - i)) & 1 for i in range(90)]
        #lfsr Initialization
        self.l=[(iv >> (127 - i)) & 1 for i in range(90, 128)]
        self.l += [1] * 22
        self.l += [0] * 9
        #print("The key is ")
        #print(self.key)
        #print("The iv is")
        #print(self.iv)
        #print("After key loading")
        #print("LFSR and NFSR are")
        #print(self.l) 
        #print(self.n)
         
    def h(self, x0, x1, x2, x3, x4, x5,x6,x7,x8):
        output= x0&x1&x2&x7&x8 ^ x0&x1&x2&x7 ^ x0&x1&x2&x8 ^ x0&x1&x2 ^ x0&x1&x3&x7&x8 ^ x0&x1&x3&x7 ^ x0&x1&x4&x7&x8^ x0&x1&x4&x7 ^ x0&x1&x4&x8^ x0&x1&x4^ x0&x1&x5&x7&x8 ^ x0&x1&x5&x7 ^ x0&x1&x6&x7&x8 ^ x0&x1&x6&x8 ^ x0&x1&x7&x8 ^ x0&x1&x8 ^ x0&x2&x3&x7&x8 ^ x0&x2&x3&x7 ^ x0&x2&x3&x8 ^ x0&x2&x3 ^ x0&x2&x4&x7&x8 ^ x0&x2&x4&x8 ^ x0&x2&x5&x7&x8 ^ x0&x2&x5&x7 ^ x0&x2&x5&x8 ^ x0&x2&x5^  x0&x2&x6&x7&x8^  x0&x2&x6&x8 ^ x0&x2&x7&x8 ^ x0&x2&x8 ^ x0&x3&x4&x7&x8 ^x0&x3&x4&x7 ^x0&x3&x5&x7&x8 ^x0&x3&x5&x7^ x0&x3&x6&x7&x8^ x0&x3&x6&x7^ x0&x3&x8^ x0&x3^ x0&x4&x5&x7&x8^ x0&x4&x5&x7^ x0&x4&x6&x7&x8^ x0&x4&x6&x8^ x0&x4&x7^ x0&x4^ x0&x5&x6&x7&x8^ x0&x5&x6&x7^ x0&x5&x7&x8^ x0&x5&x7^ x0&x6&x7^ x0&x6&x8^ x0&x7&x8^ x1&x2&x3&x7&x8^ x1&x2&x4&x7&x8^ x1&x2&x4&x8^ x1&x2&x5&x7&x8^ x1&x2&x6&x7&x8^ x1&x2&x6&x8^ x1&x2&x7^ x1&x2&x8^ x1&x2^ x1&x3&x4&x7&x8 ^x1&x3&x5&x7&x8^ x1&x3&x6&x7&x8^ x1&x3&x7^ x1&x4&x5&x7&x8 ^x1&x4&x5&x8^ x1&x4&x6&x7&x8 ^x1&x4&x7^ x1&x4 ^x1&x5&x6&x7&x8^ x1&x5&x6&x7^ x1&x5&x7&x8^ x1&x5&x7 ^x1&x5&x8^ x1&x6&x7 ^x1&x8 ^x1^ x2&x3&x4&x7&x8^ x2&x3&x5&x7&x8^ x2&x3&x6&x7&x8^ x2&x4&x5&x7&x8^ x2&x4&x5&x8 ^x2&x4&x6&x7&x8 ^x2&x4&x7&x8 ^x2&x4&x8^ x2&x5&x6&x7&x8^ x2&x5&x6&x8^ x2&x5&x8^ x2&x6&x7&x8^ x2&x6&x8^ x2&x7&x8^ x2^ x3&x4&x5&x7&x8^ x3&x4&x5&x7^ x3&x4&x6&x7&x8^ x3&x4&x6&x7^ x3&x5&x6&x7&x8^ x3&x5&x7&x8^ x3&x6&x7&x8^ x3&x6&x7^ x3&x7^ x3^ x4&x5&x6&x7&x8^ x4&x5&x6&x8^ x4&x6&x7&x8 ^x4&x6&x8^ x4&x7 ^ x5&x7&x8 ^x5 ^x6 ^x7&x8 ^x7 ^x8 ^1  
        return(output)
    
    def z(self):
        n=self.n
        l=self.l
        output=n[1] ^ n[5] ^n[11] ^ n[22] ^ n[36] ^ n[53] ^ n[72] ^ n[80] ^ n[84] ^ (l[5]&l[16]) ^ (l[13]&l[15]) ^ (l[30]&l[42]) ^ (l[22]&l[67])^self.h(l[7], l[33], l[38], l[50], l[59], l[62], n[85], n[41], n[9])
        return(output)
    
    def cnt(self):
        binary_string= ''.join(str(self.l[62+i]) for i in range(0,7))
        return(int(binary_string,2))
    
    def G(self):
        n=self.n
        output=n[0]^ n[24] ^ n[49] ^ n[79] ^ n[84] ^ (n[3]&n[59]) ^ n[10]&n[12] ^ n[15]&n[16] ^ n[25]&n[53] ^ n[35]&n[42] ^ n[55]&n[58] ^ n[60]&n[74] ^ n[20]&n[22]&n[23]^ n[62]&n[68]&n[72] ^ n[77]&n[80]&n[81]&n[83]
        return(output)

    def F(self):
        l=self.l
        output= l[0] ^ l[5] ^ l[12] ^ l[22] ^ l[28] ^ l[37] ^ l[45] ^ l[58]
        return(output)
    
    def binary_array_to_hex(self,binary_array):
        # Make sure the length is a multiple of 4 by padding with zeros if necessary
        while len(binary_array) % 4 != 0:
            binary_array.insert(0, 0)  # Pad with leading zeros

        hex_string = ''
        for i in range(0, len(binary_array), 4):
            nibble = binary_array[i:i+4]
            # Convert the nibble list to a string, then to an int, then to hex
            nibble_str = ''.join(str(bit) for bit in nibble)
            hex_digit = hex(int(nibble_str, 2))[2:]  # [2:] removes the '0x' prefix
            hex_string += hex_digit.upper()

        return hex_string





    def Initialization_Phase(self):
        rounds=127
        for __ in range(rounds):
            z=self.z()
            #print(z)
            cnt=self.cnt()
            #print(cnt)
            value_G=self.G()
            for i in range(89):
                self.n[i]=self.n[i+1]
            self.n[89]= value_G ^ self.l[0] ^ self.key[cnt] ^ z

            value_F=self.F()
            for i in range(59):
                self.l[i]=self.l[i+1]

            self.l[59]= value_F ^ z
            
            for i in range(9):
                self.l[60+i]= (__+1 >> (8-i)) &1
        #print("The LFSR is + \n")
        #print(self.l)
        #print("The NFSR is + \n")
        #print(self.n)

    def Run_Cipher(self, limit):
        output_stream=[]
        freq_cnt=[0]*128
        freq_key=[0,0]
        freq_nlfr=[0,0]
        freq_z=[0,0]
        freq_cnt_only=[0,0]
        #limit=511+limit
        
        for t in range(limit):
            
            
            z=self.z()
            if t==0:
                z1=z
            if t==1:
                z2=z
            freq_z[z]+=1
            cnt=self.cnt()
            freq_cnt[cnt]+=1
            value_G=self.G()
            for i in range(89):
                self.n[i]=self.n[i+1]
            #add self.key[cnt] in next command
            self.n[89]=value_G^self.l[0]^self.key[(t)%128]
            freq_cnt_only[self.G()^self.l[0]^self.key[cnt]]+=1
            freq_nlfr[self.n[89]]+=1
            freq_key[self.key[cnt]^self.key[(t)%128]]+=1
            value_F=self.F()
            for i in range(68):
                self.l[i]=self.l[i+1]
            self.l[68]=value_F
            output_stream.append(z)
        new=self.binary_array_to_hex(output_stream)
        print(new)
            #print("For t ="+str(t)+"\n")
            #print(z)
        #print(freq_key)
        #print(freq_nlfr)
        #print(freq_z)
        #print(freq_cnt_only)
        print("mean is")
        print(np.mean(freq_cnt))
        print("standard deviation")
        print(np.std(freq_cnt))
        
        #plt.figure(figsize=(12, 5))
        #plt.bar(range(128), freq_cnt, color='skyblue', edgecolor='black')
        #plt.title("Frequency of Values (0 to 127)")
        #plt.xlabel("Value")
        #plt.ylabel("Frequency")
        #plt.grid(axis='y', linestyle='--', alpha=0.7)
        #plt.tight_layout()
        #plt.show()
        return(z1,z2)
        
#key=0x8F3A1C9B72D45EF0A6BC198E34F0A1C7  
#iv=0x4E72AB90C1D83F6E2BD5A4C83E9F129B

#key=0x00000000000000000000000000000000
#iv=0x00000000000000000000000000000000
#key=0xffffffffffffffffffffffffffffffff
#iv=0xffffffffffffffffffffffffffffffff
#key=0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#iv=0x55555555555555555555555555555555

#key=0xbcd60b1e3af4a91d5d52834218e89d7f
#iv=0x00000000000000000000000000000000

key=0xcd718f56a392674767587feb4906a5d4
iv=0xba3c55a8d8e27e977534b17d7bf540c5

cipher=ATOMCipher(key, iv)
cipher.Initialization_Phase()
#print("LFSR after initialization is")
#print(cipher.l)
#print("NFSR after initialization is")
#print(cipher.n)
#print("cnt is")
#print(cipher.cnt())
#cipher.Run_Cipher(50000)
freq_first_bits=[0,0,0,0]
for i in range(5000):
    key_b = secrets.token_bytes(16)  # 16 bytes = 128 bits
    iv_b  = secrets.token_bytes(16)
    
    # Convert the bytes to integers
    key= int.from_bytes(key_b, 'big')  # Convert to integer using big-endian byte order
    iv = int.from_bytes(iv_b, 'big')

    cipher=ATOMCipher(key,iv)
    cipher.Initialization_Phase()
    (first_bit,second_bit)=cipher.Run_Cipher(2)
    freq_first_bits[first_bit+2*second_bit]+=1

print(freq_first_bits)