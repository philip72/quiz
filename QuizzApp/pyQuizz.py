class QuizzApp():
    def __init__(self):
        self.username=""
    
    def startup(self):
        #print the greeting at startup
        self.greeting()

        self.username=input("What is your name")

        print(f"Welcome, {self.username}")
        print()

    def greeting(self):
        print("..............................")
        print(".......Welcome  to PqQuiz......")
        print("...............................")
        print()
    
    def menu_header(self):
        print("..........................")
        print("Please make a selction:")
        print("(M): Repeat this menu")
        print("(L): List Quizzes")
        print("(T): Take the quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("this is not a valid selection. Please try again.")
    
    def goodbye(self):
        print("................................")
        print(f"Thanks for using PqQuiz,{self.username}!")
        print(".................................")

    def menu(self):
        self.menu_header()
        #get user selction and act on it this loop will 
        #run until the user exits the app
        selection=""
        while(True):
            selection=input("Selection?")

            if  len(selection)==0:
                self.menu_error()
                continue
            selection=selection.capitalize()

            if selection[0]=='E':
                self.goodbye()
                break
            elif selection[0]=='M':
                self.menu_header()
                continue
            elif selection[0]=='L':
                print("\nAvailable Quizzes Are: ")
                print("------------------------\n")
                continue
            elif selection[0]=='T':
                try:
                    quiznum=int(input("Quiz number: "))
                    print(f"you hvae selcted quiz {quiznum}")

                except:
                    self.menu_error()
            else:
                self.menu_error()
    def run(self):
        #EXecute the startup routine  -ask for name , print greeting, etc

        self.startup()
        #Start the main program menu and run until the user exits
        self.menu()

if __name__=="__main__":
    app=QuizzApp()
    app.run()
