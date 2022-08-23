import random
def main():
    """Start a periodic guessing game with me!!"""
    print("Guess the periodic!")
    
    list=["hydrogen","lithium","sodium","cesium","berrylium","rubidium","potasium","francium"]
    x=random.choice(list)
    guess=None
     
    print("hydrogen")  
    print("lithium")
    print("sodium")
    print("cesium")
    print("berrylium")
    print("potasium")
    print("rubidium")
    print("francium")

    print("hydrogen")
    
    while x !=guess:
        guess=str(input("pick a periodic between periodic."))
        if x == guess:
            print ("you are right!")
        elif x > guess :
            print("Try again")
        elif x < guess :
            print("Try again")
            
main()