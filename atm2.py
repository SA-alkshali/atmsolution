ef atm(request):
    if request > balance:
        print("you dont have enought mony !!")
    elif request < 0:
        print("you must enter number larger than ZERO !")
    else:
        while request >= 0:
            if request >= 100:
                request -= 100
                print("give 100")
            elif request >= 50:
                request-=50
                print("give 50")
            elif request >=10:
                request -=10
                print("give 10")
            elif request >=5:
                request -=5
                print("give 5")
            elif request >=1:
                request-=1
                print("give 1")


atm(1272)
