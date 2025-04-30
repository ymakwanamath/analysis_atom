import sympy
import random
from sympy import symbols

from sympy.logic.boolalg import And, Or,Xor, Not, Implies, Equivalent
from sympy.logic.boolalg import to_anf





class Alg_ATOM_cipher:
    def __init__(self,key,iv,state):
        self.key=key
        

        self.iv=[(iv >> (127-i)) & 1 for i in range(128)]
        self.n=[(iv >> (89 - i)) & 1 for i in range(90)]
        #lfsr Initialization
        self.l=[(iv >> (127 - i)) & 1 for i in range(90, 128)]
        self.l += [1] * 22
        self.l += [0] * 9
        self.s=state

    def h(self, x0, x1, x2, x3, x4, x5,x6,x7,x8):
        output= Xor(And(x0,x1,x2,x7,x8), And(x0,x1,x2,x7), And(x0,x1,x2,x8), And(x0,x1,x2) , And(x0,x1,x3,x7,x8) , And(x0,x1,x3,x7) , And(x0,x1,x4,x7,x8), And(x0,x1,x4,x7), And(x0,x1,x4,x8) , And(x0,x1,x4), And(x0,x1,x5,x7,x8), And(x0,x1,x5,x7), And(x0,x1,x6,x7,x8), And(x0,x1,x6,x8), And(x0,x1,x7,x8), And(x0,x1,x8), And(x0,x2,x3,x7,x8) , And(x0,x2,x3,x7), And(x0,x2,x3,x8), And(x0,x2,x3), And(x0,x2,x4,x7,x8), And(x0,x2,x4,x8), And(x0,x2,x5,x7,x8), And(x0,x2,x5,x7), And(x0,x2,x5,x8), And(x0,x2,x5), And(x0,x2,x6,x7,x8),  And(x0,x2,x6,x8),  And(x0,x2,x7,x8), And(x0,x2,x8), And(x0,x3,x4,x7,x8), And(x0,x3,x4,x7), And(x0,x3,x5,x7,x8), And(x0,x3,x5,x7), And(x0,x3,x6,x7,x8), And(x0,x3,x6,x7), And(x0,x3,x8), And(x0,x3),  And(x0,x4,x5,x7,x8),  And(x0,x4,x5,x7), And(x0,x4,x6,x7,x8), And(x0,x4,x6,x8), And(x0,x4,x7), And(x0,x4), And(x0,x5,x6,x7,x8), And(x0,x5,x6,x7), And(x0,x5,x7,x8), And(x0,x5,x7), And(x0,x6,x7), And(x0,x6,x8), And(x0,x7,x8), And(x1,x2,x3,x7,x8), And(x1,x2,x4,x7,x8), And(x1,x2,x4,x8), And(x1,x2,x5,x7,x8), And(x1,x2,x6,x7,x8), And(x1,x2,x6,x8), And(x1,x2,x7), And(x1,x2,x8), And(x1,x2), And(x1,x3,x4,x7,x8), And(x1,x3,x5,x7,x8), And(x1,x3,x6,x7,x8), And(x1,x3,x7), And(x1,x4,x5,x7,x8), And(x1,x4,x5,x8), And(x1,x4,x6,x7,x8), And(x1,x4,x7), And(x1,x4), And(x1,x5,x6,x7,x8), And(x1,x5,x6,x7), And(x1,x5,x7,x8), And(x1,x5,x7), And(x1,x5,x8), And(x1,x6,x7), And(x1,x8), And(x1,x2,x3,x4,x7,x8), And(x2,x3,x5,x7,x8), And(x2,x3,x6,x7,x8), And(x2,x4,x5,x7,x8), And(x2,x4,x5,x8), And(x2,x4,x6,x7,x8), And(x2,x4,x7,x8), And(x2,x4,x8), And(x2,x5,x6,x7,x8), And(x2,x5,x6,x8), And(x2,x5,x8), And(x2,x6,x7,x8),And(x2,x6,x8), And(x2,x7,x8),  x2, And(x3,x4,x5,x7,x8),  And(x3,x4,x5,x7), And(x3,x4,x6,x7,x8), And(x3,x4,x6,x7), And(x3,x5,x6,x7,x8), And(x3,x5,x7,x8), And(x3,x6,x7,x8), And(x3,x6,x7), And(x3,x7), x3, And(x4,x5,x6,x7,x8), And(x4,x5,x6,x8), And(x4,x6,x7,x8), And(x4,x6,x8), And(x4,x7), And(x5,x7,x8) ,x5 ,x6 , And(x7,x8),x7,x8,1)
        return(output)

    def z(self):
        n=self.n
        l=self.l
        output= Xor(n[1], n[5] ,n[11] , n[22] , n[36] , n[53] , n[72] , n[80] , n[84] , And(l[5],l[16]), And(l[13],l[15]), And(l[30],l[42]), And(l[22],l[67]), self.h(l[7], l[33], l[38], l[50], l[59], l[62], n[85], n[41], n[9]))
        return(output)

    def G(self):
        n=self.n
        output= Xor(n[0], n[24] , n[49] , n[79] , n[84] , And(n[3],n[59]),  And(n[10],n[12]), And(n[15],n[16]), And(n[25],n[53]), And(n[35],n[42]), And(n[55],n[58]), And(n[60],n[74]), And(n[20],n[22],n[23]), And(n[62],n[68],n[72]), And(n[77],n[80],n[81],n[83]))
        return(output)
    
    def cnt(self):
        binary_string= ''.join(str(self.l[62+i]) for i in range(0,7))
        return(int(binary_string,2))

    def F(self):
        l=self.l
        output= l[0]^ l[5]^ l[12]^ l[22] ^l[28] ^ l[37] ^ l[45] ^ l[58]
        return(output)
    
    def Initialization_Phase(self):
        rounds=511 
        for __ in range(rounds):
            print("Round No. is ")
            print(__)

            z=self.z()
            #print(z)
            value_G=self.G()
            value_F=self.F()
            for i in range(89):
                self.n[i]=self.n[i+1]
            
            self.n[89]= Xor(value_G, self.l[0], self.key[__], z)


            for i in range(59):
                self.l[i]=self.l[i+1]

            self.l[59]= Xor(value_F, z)
            
            for i in range(9):
                self.l[60+i]= (__ +1 >> (8-i)) &1
            #print("The LFSR is + \n")
            #print(self.l)
            #print("The NFSR is + \n")
            #print(self.n)
    def State_Initialization(self):
        self.l= [s[i] for i in range(69)]
        self.n= [s[i] for i in range(69,159)]

    def State_Initialization_lfsr_guessed(self):
        self.l=[1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        #self.l= [random.randint(0,1) for i in range(60)]
        #for i in range(30,60):
            #self.l.append(s[i]) 
        for i in range(60,69):
            {self.l.append(1)}
        self.n=[0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0]
        for i in range(149,159):
            self.n.append(s[i])
        #for i in range(10):
            #self.n.append(s[i])
        #for i in range(79,159):
            #self.n.append(random.randint(0,1))


    def Run_Cipher(self, limit):
        
        Z=[]
        
        for t in range(limit):
            print("The value of t is ")
            print(t)
            z=self.z()
            cnt=self.cnt()
            value_G=self.G()
            value_F=self.F()
            for i in range(89):
                self.n[i]=self.n[i+1]
            
            self.n[89]=Xor(value_G,self.l[0],self.key[(t-1)%128])
            for i in range(68):
                self.l[i]=self.l[i+1]
            self.l[68]=value_F
            print(self.l)
            print(self.n)
            print(z)
            Z.append(z.to_anf())
        print("Z is")
        print(Z)
        return(Z)
       
            

k0,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20, k21,k22,k23,k24,k25,k26,k27,k28,k29,k30,k31,k32,k33,k34,k35,k36, k37,k38,k39,k40,k41,k42,k43,k44,k45,k46,k47,k48,k49,k50 ,k51,k52,k53,k54,k55,k56,k57,k58,k59,k60,k61,k62,k63,k64,k65,k66,k67,k68,k69,k70,k71,k72,k73,k74,k75,k76,k77,k78,k79,k80, k81, k82, k83, k84, k85, k86, k87, k88, k89, k90, k91, k92, k93, k94, k95, k96, k97, k98, k99, k100, k101, k102, k103, k104, k105, k106, k107, k108, k109, k110, k111, k112, k113, k114, k115, k116, k117, k118, k119, k120, k121, k122, k123, k124, k125, k126, k127= symbols('k0 k1 k2 k3 k4 k5 k6 k7 k8 k9 k10 k11 k12 k13 k14 k15 k16 k17 k18 k19 k20  k21 k22 k23 k24 k25 k26 k27 k28 k29 k30 k31 k32 k33 k34 k35 k36 k37 k38 k39 k40 k41 k42 k43 k44 k45 k46 k47 k48 k49 k50 k51 k52 k53 k54 k55 k56 k57 k58 k59 k60 k61 k62 k63 k64 k65 k66 k67 k68 k69 k70 k71 k72 k73 k74 k75 k76 k77 k78 k79 k80 k81 k82 k83 k84 k85 k86 k87 k88 k89 k90 k91 k92 k93 k94 k95 k96 k97 k98 k99 k100 k101 k102 k103 k104 k105 k106 k107 k108 k109 k110 k111 k112 k113 114 k115 k116 k117 k118 k119 k120 k121 k122 k123 k124 k125 k126 k127')
key=[k0,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20, k21,k22,k23,k24,k25,k26,k27,k28,k29,k30,k31,k32,k33,k34,k35,k36, k37,k38,k39,k40,k41,k42,k43,k44,k45,k46,k47,k48,k49,k50 ,k51,k52,k53,k54,k55,k56,k57,k58,k59,k60,k61,k62,k63,k64,k65,k66,k67,k68,k69,k70,k71,k72,k73,k74,k75,k76,k77,k78,k79,k80, k81, k82, k83, k84, k85, k86, k87, k88, k89, k90, k91, k92, k93, k94, k95, k96, k97, k98, k99, k100, k101, k102, k103, k104, k105, k106, k107, k108, k109, k110, k111, k112, k113, k114, k115, k116, k117, k118, k119, k120, k121, k122, k123, k124, k125, k126, k127]

s = symbols('s0:159')

iv=0x00000000000000000000000000000000


cipher=Alg_ATOM_cipher(key, iv,s)
cipher.State_Initialization_lfsr_guessed()
cipher.Run_Cipher(10)


#cipher.Initialization_Phase()
#print(cipher.n)