lower = int(input("men"))
upper = int(input("max"))
hamborger = []

def asidfsdifajd():
    for num in range(lower, upper + 1):

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print("this is a prime: ", num)
                hamborger.append(num)
            
           
    print("this is the final sum: ", sum(hamborger))
    
asidfsdifajd()