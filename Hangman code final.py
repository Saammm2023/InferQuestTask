import random
d={'1':'apple','2':'ball','3':'cat','4':'dog','5':'elephant','6':'frog','7':'goat','8':'horse','9':'icecream','10':'joker','11': 'mohol','12':'solapur','13':'talegaon','14':'pune','15':'mango','16':'strawberry'}

name=input("enter your name")
print("welcome to the game",name)



word=random.choice(list(d.values()))
#print(word)
chances=len(word)+3
print("the length of the word to be guessed is",len(word))
print("you have",chances,"chances to guess the letters")


#def answer as player_answer:
	
#print(id(word[0]))
#word='apple'
a='1'*len(word)
guessed_letters=list(a)
game_over=False 
b=list(word)
#print(b)
for k in range(chances):
    guess=input("enter your guess")
    if guess in word:
      
      i=b.index(guess)      
      print("your guessed letter is at", b.index(guess)+1, "place ")
      b[i]='1'
      chances+=1
        #for j in range(0,i):
   
        		
           
    else:
        print('wrong guess')  
    if guessed_letters==b:
            print("you win, you guessed correct that")
            break
    else : 
        continue
     
     #       game_over=True
   # if game_over:
        #		break
    

                
print("the word was", word)
#print(list(word))
