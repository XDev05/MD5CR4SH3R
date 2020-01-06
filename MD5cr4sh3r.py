import hashlib
print('''




     _______.____    ____  _______.       ______ .______      _  _         _______. __    __   ____   .______          _______.
    /       |\   \  /   / /       |      /      ||   _  \    | || |       /       ||  |  |  | |___ \  |   _  \        /       |
   |   (----` \   \/   / |   (----`     |  ,----'|  |_)  |   | || |_     |   (----`|  |__|  |   __) | |  |_)  |      |   (----`
    \   \      \_    _/   \   \         |  |     |      /    |__   _|     \   \    |   __   |  |__ <  |      /        \   \    
.----)   |       |  | .----)   |        |  `----.|  |\  \----.  | |   .----)   |   |  |  |  |  ___) | |  |\  \----.----)   |   
|_______/        |__| |_______/     _____\______|| _| `._____|  |_|   |_______/    |__|  |__| |____/  | _| `._____|_______/    
                                   |______|                                                                                    







    ''')
flag = 0
md5_hash = input("Drag your md5 hash: ")
wordlist = input("please Put Your File name: ")
try:
    pass_file = open(wordlist,"r")
except:
    print("There is No file found :(")
    quit()
 
for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    # print(word)
    # print(digest)
    # print(pass_hash)
    if digest.strip() == md5_hash.strip():
        print("password found")
        print("Password is " + word)
        flag = 1
        break
 
if flag == 0:
    print("password not in list")
