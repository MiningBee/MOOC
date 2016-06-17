#bisection search
#Author: Hua Wang
#python3.5

low = 0
high = 100
mid = (low + high)/2
print ("Please think of a number between 0 and 100!")
while True:
    print ("Is your secret number %d?" % (mid))
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if x == 'h':
        high = mid
        mid = int((low + high)/2)
    elif x =='l':
        low = mid
        mid = int((low + high)/2)
    elif x == 'c':
        print ("Game over. Your secret number was: %d" % (mid))
        break
    else:
        print ("Sorry, I did not understand your input.")


#python2.7
low = 0
high = 100
mid = (low + high)/2
print "Please think of a number between 0 and 100!"
while True:
    print "Is your secret number %d?" % (mid)
    x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if x == 'h':
        high = mid
        mid = int((low + high)/2)
    elif x =='l':
        low = mid
        mid = int((low + high)/2)
    elif x == 'c':
        print "Game over. Your secret number was: %d" % (mid)
        break
    else:
        print "Sorry, I did not understand your input."



