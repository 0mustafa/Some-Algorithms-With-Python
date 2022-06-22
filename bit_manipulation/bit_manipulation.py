vars = [4,4,3,3,1,6,6,8,8]
zero = 0

for i in vars:
    ###### XOR ######
    # A | B | A XOR B
    # 0 | 0 |    0
    # 0 | 1 |    1
    # 1 | 0 |    1
    # 1 | 1 |    0
    #################
    
    # ^ is xor symbol in python

    #zero xor i 
    #000 xor 100 = 100
    #100 xor 100 = 000
    zero = zero ^ i

print(zero)
