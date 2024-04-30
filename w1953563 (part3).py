# I declare that my work contains no examples of misconduct, such as plagarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# student id: w1953563
# Date: 11.12.2022

total = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count = 0
students = []

def input_condition(marks):  #using a def to check the inputing marks are greater than 120 or not divisible by 20, if so printing out of range.
    if marks > 120 or marks % 20 != 0:
        print("out of range.")
        print()
        return 1
    else:
        return 0
        

while True:

    try:
        marks = []
        pass_marks = int(input("Enter your credits at pass: "))
        num1 = input_condition(pass_marks)
        if num1 == 1:  #checking whether the returned value from the function is 1, if it is one then continue.
            continue
        
        defer_marks = int(input("Enter your credits at defer: "))
        num2 = input_condition(defer_marks)
        if num2 == 1:
            continue
        
        fail_marks = int(input("Enter your credits at fail: "))
        num3 = input_condition(fail_marks)
        if num3 == 1:
            continue

        total = pass_marks + defer_marks + fail_marks
        if total > 120 or total < 120:
            print("Total incorrect.")
            print()
            continue

            
    except ValueError:
        print("Integer required.")
        print()
        continue

        
    if total == 120:
        
        if pass_marks == 120:
            print("progress")
            marks.append("Progress")
            count1 +=1
            
        elif pass_marks == 100:
            print("progress (module trailer)")
            marks.append("Progress (module trailer)")
            count2 +=1
            
        elif fail_marks == 20 or fail_marks == 40 or fail_marks == 60 or fail_marks == 0:
            print("Do not progress - module retriever")
            marks.append("Module retriever")
            count3 +=1
            
        elif fail_marks == 80 or fail_marks == 100 or fail_marks == 120:
            print("Exclude")
            marks.append("Exclude")
            count4 +=1

        marks.append(pass_marks)   #appending the inputing marks to a list called marks.
        marks.append(defer_marks)
        marks.append(fail_marks)
        students.append(marks)      #appending the marks list to an another list called students.
        
                
    count = count1 + count2 + count3 + count4
    
      
    print()
    print("Would you like to enter another set of data? ")
    decision = input("Enter 'y' for yes or 'q' to quite and view results: ")
    print()

    while decision not in ('y','q'):
        decision = input("Inavlid input re-enter 'y' for yes or 'q' to quite and view results: ")
        print()
    
    if decision.lower() == 'q':
        print()
        print("-"*70)
        print("Histogram")
        print()
        print("Progress", count1  ,  "  :" , '*'*count1)
        print("Trailer", count2   ,   "   :" , '*'*count2)
        print("Retriever", count3 , " :" , '*'*count3)
        print("Excluded", count4  ,  "  :" , '*'*count4)
        print()
        print(f"{count} outcomes in total.")
        print("-"*70)
        print()

          
    elif decision.lower() == 'y':
       continue


    student_results = []
    for result in students:       
        elements = result[0] + " - " + str(result[1]) + ", " + str(result[2]) + ", " + str(result[3])   # indivitually calling the elements in the students list.
        print(elements)
        student_results.append(elements)
    print()


    print("*Text File*")
    with open('coursework.txt','w') as file:     #creating a text file.
        file.write("\n".join(student_results))   #inserting data to the text file created. /  Taken from 'stackflow' 
        
 
    with open('coursework.txt','r') as file:
        contents = file.read()                  #reading the text file.
        print(contents)
        break
    
    
