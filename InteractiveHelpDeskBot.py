# Task 1: command parser
problems = ['help', 'issue', 'contact support']
complaint = input (f"hello thank you for using fix-a-bot, please identify your problem from the following list {problems}: ")
found = 0

def problem(p1,found):
    for x in p1:
            if x == complaint.lower():
                print ("found Complaint")
                found = 1
    if found == 0:
        print  ("complaint not found")

i = problem(problems,found)

# Task 2: issue categorizer
if complaint == "issue":
    issue_type = input ('''What issue are you having
1. Login 
2. performance
3. error \n : ''')     
    if issue_type ==("login"):
         print('thank you we will now escalate your LOGIN issue to our support staff')
    elif issue_type == ("performance"):
         print(" thank you we will not escalate your PERFORMANCE issue to our support staff ")
    elif issue_type == ("error"):
         print(" thank you we will not escalate your Error issue to our support staff ")


