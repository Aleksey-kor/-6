import math
f=open('text.txt')
unchiper_text=f.read()
f.close()
unchiper_text=unchiper_text.replace(' ', '')
unchiper_text=unchiper_text.replace('\n', '')
unchiper_text=unchiper_text.lower()
key=input("Введите ключ \n")
alphabet="abcdefghijklmnopqrstuvwxyz";
def keyMoreLength(key,text):
    return key*int(len(unchiper_text)/len(key))+key[0:len(unchiper_text)%len(key)]
key=keyMoreLength(key,unchiper_text)
chiper_text=''
for i in range(len(unchiper_text)):
    if alphabet.index(key[i])<alphabet.index(unchiper_text[i]):
        chiper_text+=alphabet[int((alphabet.index(key[i])-alphabet.index(unchiper_text[i])))]
    else:
        chiper_text+=alphabet[int(math.fabs(alphabet.index(key[i])-alphabet.index(unchiper_text[i])))]
print(chiper_text)
f=open("code.txt","w")
f.write(chiper_text)
f.close()
