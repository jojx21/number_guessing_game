import random
import time

class computers_number:
    def __init__(self,computer_choice):
        self.computer_choice = computer_choice
         
    def random_number(self):
     self.computer_choice = int(random.randint(1,100))
     return self.computer_choice

class main_game():
     def intro(self):
          print("Welcome to a guessing game! ")
          time.sleep(1)
          while True:
               try:
                    user_decision =int(input("""What version would you like to play? 
1)You have to guess a random number chosen by the computer
2)The Computer guesses a random number you have chosen
"""))
                    if user_decision ==1 or user_decision == 2:
                         break
               except:
                    print("The value entered must be either 1 or 2")
                    
          if user_decision == 1:
               print("*" * 30)
               while True:
                    a = computers_number(self)
                    a.random_number()
                    c_rnd = a.random_number()
                  
                              
                    try:
                         user_guess = int((input("Choose a number between 1 and 100: ")))
                         break
                    except:
                         print("The value must be a number. ")


               if user_guess == c_rnd:
                    b = main_game()
                    b.check_winner()

               while user_guess != c_rnd:
                    if user_guess >  c_rnd:
                         print("hmmmmm... ")
                         time.sleep(2)
                         print("The guess is wrong.")
                         print("You are higher than the number!")
                         try_again = int(input("Try again: "))

                         if try_again == c_rnd:
                              c = main_game()
                              c.check_winner()
                             
                                   
                    elif user_guess < c_rnd:
                         print("hmmmm... ")
                         time.sleep(2)
                         print("The guess is wrong.")
                         print("You are lower than the number!")
                         try_again = int(input("Try again: "))
                         if try_again == c_rnd:
                              c = main_game()
                              c.check_winner()
               
          if user_decision == 2:
               num = int(input("Enter a number: "))
               if num < 1 or num > 100:
                    print("Must be in range [1, 100]")
               else:
                    d=main_game()
                    d.computer_guesseses(num)
                          
     def computer_guesseses(self,num):
          low = 1
          high = 100
          guess = (low+high)//2
          while guess != num:
               guess = (low+high)//2
               print("The computer takes a guess...", guess)
               time.sleep(1)
               if guess > num:
                    high = guess
               elif guess < num:
                    low = guess + 1
                    print("The computer guessed", guess, "and it was correct!")


                   #The algorithm works by selecting a low and high limit to start with (in your case low=1 and high=100).
                    # It then checks the midpoint between them.
                    # If the midpoint is less than number, the midpoint becomes the new lower bound.
                    # If the midpoint is higher, it becomes the new upper bound.
                    # After doing this a new midpoint is generated between the upper and lower bound.



                    
                            
     def check_winner(self):
          print("Congraglations! We have a winner!! ")
          play_again = str(input("Would you like to play again? Type Yes Or No: ")).upper()
          if play_again in ["YES", "Y"]:
               print("*" * 30)
               time.sleep(2)
               n = main_game()
               n.intro()
          elif play_again in ["NO" , "N"]:

               print("Goodbye :( ")
               time.sleep(2)
               quit()

                
                
             


c = main_game()
c.intro()

