#Data Structure1_203<String>p17_[ROT13]11655
import sys 
string = list(sys.stdin.readline())
for st in string : 
    if st.islower(): 
        a = ord(st)+13 
        if a > ord('z'):
            a = a -26
        print(chr(a), end="")
    elif st.isupper():
        a = ord(st)+13
        if a > ord('Z'):
            a = a -26
        print(chr(a), end="")
    else: 
        print(st, end="")
    