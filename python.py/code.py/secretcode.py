import random
import string 
def random_str():
    return ''.join(random.choice(string.ascii_letters) for _ in range(3))


print("welcome to the !! SECRET_CODE !!")
print("enter 1 for coding message: ")
print("enter 2 for decoding the message: ")

a= input("enter choice: ")
st= input("enter the string: ")
words= st.split(" ")

empty=[]
if(a=="1"):
    
    for i in words:
        if(len(i)>3):
            r1= random_str()
            r2= random_str()
            ans= r1+i[1:]+i[0]+r2
            empty.append(ans)
        else:
            empty.append(i[::-1])
    print(" ".join(empty))

else:
   
    for i in words:
        if(len(i)<=3):
            empty.append(i[::-1])
        else:
            core = i[3:-3]   # remove "jko" and "mnb"
            ans = core[-1] + core[:-1]
            empty.append(ans)
    print("decoded message:-  "," " .join(empty))
    







#     #how to remove element - a.remove(element), a.pop(index)    - in remove we will provide element so it will remove first occurance of the element and with pop() we provide index value 
#     #how to reverse the string - string[::-1]


# import random
# import string

# def random_str():
#     return ''.join(random.choice(string.ascii_lowercase) for _ in range(3))

# saved_key = ""   # 🔐 store passkey
# saved_encoded = ""  # store encoded message

# print("enter 1 for coding message: ")
# print("enter 2 for decoding the message: ")

# a = input("enter choice: ")

# if a == "1":
#     saved_key = input("Set your passkey: ")
#     st = input("enter the string: ")
#     words = st.split(" ")

#     empty = []

#     for i in words:
#         if len(i) > 3:
#             r1 = random_str()
#             r2 = random_str()
#             ans = r1 + i[1:] + i[0] + r2
#             empty.append(ans)
#         else:
#             empty.append(i[::-1])

#     saved_encoded = " ".join(empty)
#     print("Encoded message:")
#     print(saved_encoded)


# elif a == "2":
#     key = input("Enter passkey: ")

#     if key != saved_key:
#         print("❌ Wrong passkey! Access Denied.")
#     else:
#         words = saved_encoded.split(" ")
#         empty = []

#         for i in words:
#             if len(i) <= 3:
#                 empty.append(i[::-1])
#             else:
#                 core = i[3:-3]
#                 ans = core[-1] + core[:-1]
#                 empty.append(ans)

#         print("Decoded message:")
#         print(" ".join(empty))