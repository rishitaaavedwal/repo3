import math
a=10
b=5
maximum=np.maximum(a,b)
def find_max_bitwise(a,b)
    diff=a-b
    sign_bit=(diff>>31) & 1
    return a-(sign_bit*diff)
a=10
b=5
maximum=find_max_bitwise(a,b)
print(maximum)
print(a if a>=b else b)
maximum=math.fmax(a,b)
print(maximum)
