

def isPermute(Str1, Str2):
    print('x')
    #check string lengths
    if len(Str1) != len(Str2):
        print('no ')
        return
    #sort th strings
    if sorted(Str1) == sorted(Str2):
        print('yes permutation')
    else:
        print('no ')


isPermute('asd','dsa')


#METHOD 2:
str1 ='assdfg'
str2='asgdfa'

cnt = {}
for i in str1:
    if i in cnt.keys():
        cnt[i]+=1
    else:
        cnt[i] = 1
print(cnt)


for i in str2:
    if i in cnt.keys():
        cnt[i]-=1
        if cnt[i] == 0:
             cnt.pop(i)

if len(cnt) == 0:
    print('yes')
else:
    print('no')






# Python program to print all permutations with
# duplicates allowed

def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
#permute(a, 0, n - 1)
