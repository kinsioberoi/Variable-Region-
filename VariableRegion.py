
Anchor1 = 'ATTTTTGGGGGGG'
Anchor2 = 'GTTTTTAGGGGG'
seq = "ATTTTTGGGGGGGATATATATATATGTTTTTAGGGGG"
print ("Variable Region =" ,(seq.split(Anchor1))[1].split(Anchor2)[0])

