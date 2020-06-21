command = str(" ")
Operations = []
Answers = []

initiate_response = "Hello! Welcome to the Calculator!"
basic_instructions = "The basic operations to be used are listed below: \n '+' : Addition \n '-' : Subtraction \n '*' : Multiplication \n '/' : Division"
exponential_instructions = "For Roots and Exponents use the double asterisks (**).\n For Example: \n 2**3 = 8 and 169**0.5 = 13"
warning = "Be careful of the order of operations by using the parenthesis ()."

print(initiate_response)
print(basic_instructions)
print(exponential_instructions)
print(warning)

while command != "EXIT":
    
    calculation_answer = float(0.0)
    
    calculation_query = input("\nEnter Your Query Please:\n")
    calculated_answer = str(eval(calculation_query))
    
    print("The Answer is: " + calculated_answer)
    
    Operations.append(calculation_query)
    Answers.append(calculated_answer)
    
    print('\n')
    
    command = str(input("Exit or Continue Program? \nEnter any key to continue or enter 'Exit' to Quit: "))
    command = command.upper()

else:
    
    Index = 0
    Number = 1
    List_Size = len(Operations)
    print("The Total Calculations you did:\n")
        
    while Index < List_Size :
        print(f"{Number}.  {Operations[Index]} = {Answers[Index]} \n") 
        Index += 1
        Number += 1

    print('\n')
    print("Thanks for using the Calculation Program! :))")