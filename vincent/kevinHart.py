#Resources and Adapted From:
#https://micropi.wordpress.com/2016/10/18/create-a-python-chatbot/
#Showed me how to slowprint and write the opening messages
import sys
import time

#inputs:
poker = ["poker", "coach"]
fav = ["favorite comedian", "comedian"]
tvcameo = ["cameo", "tv appearance"]



def slowprint(text): #To slowprint the text, making it more like
    #a conversation where someone is typing up the answer.
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.1)

def replay():
    text = "Is there anything else you want to know? \n"
    slowprint(text)
    answer = input().lower()
    if answer == "no":
        text = "aight, catch you later"
        slowprint(text)
        exit
    else:
        questions()

def questions():
    text = "That's cool, is there anything you want to ask me? \n"
    slowprint(text)
    answer = input().lower()
    if answer in poker:
        text = "I would die to have Jimmy Levine as my poker coach \n"
        slowprint(text)
        replay()
    elif answer in fav:
        text = "My favorite comedian of all time is Dave Chappelle \n"
        slowprint(text)
        replay()
    elif answer in tvcameo:
        text = "It would have to be Dwayne The Rock Johnson \n"
        slowprint(text)
        replay()
    #More to come


text = "Yo, it's Kevin Hart, who this? \n" #Opening Messages (input doesn't matter)
slowprint(text)
answer = input().capitalize() 

text = "Hey " + answer + " what's good? \n" #Opening Messages (input doesn't matter)
slowprint(text)
answer = input()
questions()


