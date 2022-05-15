import time

#helper functions
def print_delayed(text, delay = 2):
    print(text)
    time.sleep(delay)
    return

def get_valid_input(question):
    ans = input(question + "\n")
    while ans != "1" and ans != "2":
        print("You can only press 1 or 2")
        ans = input(question)
    return ans

def introduction():
    print_delayed("Welcome to Herediatry 2.0")
    print_delayed("Your son comes into your room and asks if he can go to a school party")
    print_delayed("You allow him to go, as long as he takes his little sister")
    print_delayed("You just get to the party")

def part1():
    print_delayed("You chose to leave your sister alone")
    print_delayed("You shouldn't of done this...she's only 13")    
    print_delayed("She wanders around the party")
    print_delayed("She noticed chocolate cake, but knows she has a peanut allergy")
    ans = get_valid_input("Enter 1 if she eats the cake\nEnter 2 if she passes ")
    if ans == "1":
        print_delayed("You chose she eats the cake even though she has a deadly allergy")
        print_delayed("You are not a nice person")
        print_delayed("You just killed a little girl")
    else:
        print_delayed("Great. She knows not to eat food from strangers")
        print_delayed("Your sister lives")

def part2():
    print_delayed("You brought your sister into the room full of weed")
    print_delayed("You know she suffers from asthma..")
    print_delayed("She is curious about the weed")
    ans = get_valid_input("Enter 1 to remove your sister from the party\nEnter 2 to offer her a puff ")
    if ans == "1":
        print_delayed("You are a great brother!")
        print_delayed("You bring her home and you are safe and sound")
    else:
        print_delayed("Are you crazy?")
        print_delayed("You just killed your sister")

def launcher():
    ans = get_valid_input("Enter 1 to leave your sister alone\nEnter 2 to bring her with you while you are doing drugs ")
    if ans == "1":
        part1()
    else:
        part2()

def game():
    introduction()    
    launcher()

def main():
    game()
    print("bye")

if __name__ == "__main__":
    main()
    
