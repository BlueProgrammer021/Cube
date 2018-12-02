import random
B = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
R = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]
Y = ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9"]
G = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]
O = ["O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9"]
W = ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9"]
S = []
temp = ""
count = 0
r_choice = 0
default = []

# Up-Side
UpS1 = []
UpS2 = []
UpS3 = []
# Down-Side
DoS1 = []
DoS2 = []
DoS3 = []
# Right-Side
RiS1 = []
RiS2 = []
RiS3 = []
# Left-Side
LeS1 = []
LeS2 = []
LeS3 = []
# Front-Side
FrS1 = []
FrS2 = []
FrS3 = []
# Back-Side
BaS1 = []
BaS2 = []
BaS3 = []

# I make the cube with random 
rand_L = B + R + Y + G + O + W
#for i in range(0, 6):
for j in range(54):
    #L = random.choice(rand_L)
    while (rand_L != []):
        r_choice = random.choice(rand_L)
        for k in rand_L:
            if k == r_choice:
                rand_L.pop(count)
            count += 1
        count = 0
        default.append(r_choice)
        break

# Fill up the cube
rand_S = UpS1, UpS2, UpS3, DoS1, DoS2, DoS3, RiS1, RiS2, RiS3, LeS1, LeS2, LeS3, FrS1, FrS2, FrS3, BaS1, BaS2, BaS3
for b in range(18):
    S = rand_S[b]
    for c in range(3):
        temp = default[0]
        S.append(temp)
        default.pop(0)

print default
print "====================", FrS1
print "====================", FrS2
print "====================", FrS3
print ""
print "--------------------", UpS1
print "--------------------", UpS2
print "--------------------", UpS3
print LeS1, "-------------------------", RiS1
print LeS2, "-------------------------", RiS2
print LeS3, "-------------------------", RiS3
print "--------------------", DoS1
print "--------------------", DoS2
print "--------------------", DoS3
print ""
print "====================", BaS1
print "====================", BaS2
print "====================", BaS3
