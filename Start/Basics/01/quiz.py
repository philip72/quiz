class Question():
    def __init__(self) -> None:
        self.points=0

        self.correct_answer=""
        self.text=""
        self.is_correct=False

class QuestionTf(Question):
    def __init__(self) -> None:
        super().__init__()

    def ask(self):
        while(True):
            print(f"(T)rue or (F)alse:{self.text}")
            response=input("? ")

            # TODO: Check to see if no response was entered
            if len(response)==0:
                print("invalid response. try again")
                continue


            # TODO: Check to see if either T of F was given
            response=response.lower()
            if response[0]!="t" and response[0]!="f":
                print("Sorry invalid , Try again")
                continue

            # TODO: mark this question if answered correctly

            if response[0]==self.correct_answer:
                self.is_correct=True

            break

class QuestionMc(Question):
    def __init__(self) -> None:
        super().__init__()
        #TODO : define the answers for this question

        self.answers=[]

    #TODO define the ask method
    def ask(self):
        while(True):
            #TODO : present the question and possible answers

            print(self.text)
            for a in self.answers:
                print(f"({a.name}) {a.text}")
            response=input("? ")

            #TODO Check to see if no responses was entered 
            if len(response)==0:
                print("Sorry that not valid response . please try again")
                continue

            #TODO mark this question as correct if answered corrctly 
            response=response.lower()
            if response[0]==self.correct_answer:
                self.is_correct=True


            break


class Answer:
    def __init__(self) -> None:
        #TODO define the answer fields
        self.text=""
        self.name=""


if __name__=="__main__":
    q1=QuestionTf()
    q1.text="Broccoli is good for you"
    q1.points=5
    q1.correct_answer="t"
    q1.ask()
    q2=QuestionMc()
    q2.text="What is 2+2"
    q2.points=10
    q2.correct_answer="b"
    ans=Answer()
    ans.name="a"
    ans.text="3"
    q2.answers.append(ans)
    ans=Answer()
    ans.name="b"
    ans.text="4"
    q2.answers.append(ans)
    ans=Answer()
    ans.name="c"
    ans.text="5"
    q2.answers.append(ans)
    q2.ask()
    
    print(q1.is_correct)
    print(q2.is_correct)



