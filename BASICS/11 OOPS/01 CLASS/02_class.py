class Name:
    def __init__(self) -> None: # THIS METHOD RUNS AUTOMATICALLY AND IS KNOWN AS CONSTRUCTOR
        print("JOB DONE")

    @staticmethod  #this command lets you to use a method without self
    def getsalary():
        print("Your salary is 10000k.")

amrit = Name()
amrit.getsalary()