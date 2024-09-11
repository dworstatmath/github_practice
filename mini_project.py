import random
rps=["rock", "paper", "scissors"]
message=["Try again", "You won a point", "Your opponent won a point"]
def choose_rps():
  return(random.choice(["rock", "paper", "scissors"]))
def playGame(banana):
  won_loss_ratio=[0,0]
  while won_loss_ratio[0]<banana and won_loss_ratio[1]< banana:
    player="rock"
    computer="rock"
    while (rps.index(player)-rps.index(computer))%3==0:
      player=input("rock, paper, or scissors? ")
      computer=choose_rps()
      print("computer chose " + computer)
      print(message[(rps.index(player)-rps.index(computer))%3]+"\n")
      if (rps.index(player)-rps.index(computer))%3==1:
        won_loss_ratio[0]+=1
      elif (rps.index(player)-rps.index(computer))%3==2:
        won_loss_ratio[1]+=1
  if won_loss_ratio[0]>won_loss_ratio[1]: 
    print ("You won!"+ str (won_loss_ratio))
  else:
    print("You lost" + str (won_loss_ratio))
playGame(int(input("how many games do you want to play to?")))