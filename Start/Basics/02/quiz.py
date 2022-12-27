

class Quiz:
    def __init__(self):
        #TODO : define the quiz properties
        self.name=""
        self.descrption=""
        self.question=[]
        self.score=0
        self.correct_count=0
        self.total_points=0

    
    def print_header(self):
        print("\n\n**************************")
        #TODO : print the quiz header

        print(f"QUIZ NAME : {self.name}")
        print(f"DESCRIPTION :  {self.descrption}")
        print(f"QUESTIONS: {len(self.question)}")
        print(f"TOTAL POINTS: {self.total_points}")

        print("************************")

    def print_results(self):
        print("*****************************\n")

        print("*******************************\n")

    def take_quiz(self):
        #TODO: initialize the quiz state
        self.score=0
        self.correct_count=0
        for q  in self.question:
            q.is_correct=False

        #TODO : print the header
        self.print_header()

        #TODO : execute each question and record the results 
        for q in self.question:
            q.ask()
            if (q.is_correct):
                self.correct_count+=1
                self.score+=q.points

        print("----------------------------------------\n")



        #TODO return the results
        return(self.score, self.correct_count, self.total_points)


class Question:
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
    qz=Quiz()
    qz.name="Sample Quiz"
    qz.descrption="This is a sample quiz"

    q1=QuestionTf()
    q1.text="Broccoli is good for you"
    q1.points=5
    q1.correct_answer="t"
    qz.question.append(q1)

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
    qz.question.append(q2)

    qz.total_points=q1.points+q2.points
    result=qz.take_quiz()
    print(result)
    
    