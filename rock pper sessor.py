# rock paper sessor


import random

a=input("first your turn:")

    
c=["rock","paper","sessor"]
b=(random.choice(c))
print(b)


if (a=="rock" and b=="paper"):
    print("rock user  is lose")
elif(a==b):
    print("match tied play again")
    
elif (a=="sessor" and b=="paper"):
    print("sessor user win ")
elif (a=="paper" and b=="rock"):
    print("paper user win ")
elif(a=="rock" and b=="sessor"):
    print("rock user is win")
elif(a=="sessor" and b=="paper"):
    print("you lose")
elif(a=="sessor" and b=="rock"):
     print("you lose")
elif(a=="paper" and b=="sessor"):
    print("you lose")

print("do you want to play again y/n")
q=input()
while True:
    
   if(q=='y' or q=='Y'):

      import random
      a=input("first your turn:")

      c=["rock","paper","sessor"]
      b=(random.choice(c))
      print(b)


      if (a=="rock" and b=="paper"):
        print("rock user  is lose")
      elif(a==b):
        print("match tied play again")
    
      elif (a=="sessor" and b=="paper"):
         print("sessor user win ")
      elif (a=="paper" and b=="rock"):
        print("paper user win ")
      elif(a=="rock" and b=="sessor"):
         print("rock user is win")
      elif(a=="sessor" and b=="paper"):
        print("you lose")
      elif(a=="sessor" and b=="rock"):
        print("you lose")
      elif(a=="paper" and b=="sessor"):
         print("you lose")

      
      else:
         break
  



    
