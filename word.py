import random 
a=open(r"C:\Users\Asus\Desktop\words.txt","r")
b=a.read().split()
word=random.choice(b)
print(word)
letter=[]
pos=[]
for i in range(0,6):
    c=input(f"Enter a {len(word)} letter word ")
    if c==word:
        print("you won")
        break
    else:
        for i in c:
            # for a in range(0,len(word)):
            #     print(i[a])
                if i in word:
                    if word.index(i)==c.index(i):
                        if i not in pos:
                           pos.append(i)
                           
                    elif i not in letter:
                       letter.append(i)
        
        for i in range(0,len(word)):
                if word[i] in pos:
                    print(word[i],end=' ')
                else:
                    print(" _ ",end='')
        print()
        print("Correct letters are",letter)
            
            
            
