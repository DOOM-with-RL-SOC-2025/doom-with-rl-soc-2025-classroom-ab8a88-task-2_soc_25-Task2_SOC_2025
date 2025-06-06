"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            ID = input("ID:")
            city = input("City:")
            branchcodes = input("Branch(es):")
            # How will you convert this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5
            branchcodes = [int(x.strip()) for x in branchcodes.split(",")]
            age = input("Age: ")
            salary = input("Salary: ")
            # Create a new Engineer with given details.
            engineer = Engineer(name=name, age=age, ID=ID, city=city, branchcodes=branchcodes, salary=salary)
            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            
        
        elif last_input == 2:
            # Gather input to create a Salesperson
            # Then add them to the roster
            name = input("Name:")
            ID = input("ID:")
            age = input("Age: ")
            city = input("City:")
            branchcodes = input("Branch(es):")
            branchcodes = [int(x.strip()) for x in branchcodes.split(",")]
            salary = input("Salary: ")
            position = input("Position (Rep/Manager/Head): ")
            superior = input("Superior ID: ")
            sales_person = Salesman(name=name, age=age, ID=ID, city=city, branchcodes=branchcodes, position=position, superior=superior, salary=salary)
            sales_roster.append(sales_person)
            # pass

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            
            if not found_employee: print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")

                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names = [branch_names[code] for code in found_employee.branchcodes]
                ## ???? what comes here??
                print(f"Branches: {', '.join(branch_names)}")
                
                print(f"Salary: {found_employee.salary}")

        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            # pass
            ID = int(input("ID: "))
            new_branch = int(input("New branch code: "))
            employee = next((emp for emp in engineer_roster + sales_roster if emp.ID == ID), None)
            if employee is None:
                raise ValueError("Employee not found")
            if not employee.migrate_branch(new_branch):
                raise ValueError("Branch migration failed")
            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            # promote employee to next position
            new_position = input("Enter new position: ")
            found = False
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    if not employee.promote(new_position):
                        raise ValueError("Invalid promotion or demotion")
                    found = True
                    break
            if not found:
                raise ValueError("Employee not found")

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            # Increment salary of employee.
            amt = int(input("Enter increment amount: "))
            found = False
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    employee.increment(amt)
                    found = True
                    break
            if not found:
                raise ValueError("Employee not found")
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            # Print superior of the sales employee.
            found = False
            for employee in sales_roster:
                if employee.ID == ID:
                    superior_info = employee.find_superior()
                    if superior_info == (None, None):
                        print("No superior found")
                    else:
                        print(f"Superior ID: {superior_info[0]}, Name: {superior_info[1]}")
                    found = True
                    break
            if not found:
                raise ValueError("Employee not found")
        
        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            # Add superior of a sales employee
            found = False
            for employee in sales_roster:   
                if employee.ID == ID_E:
                    if not employee.add_superior():
                        raise ValueError("Superior cannot be added")
                    found = True
                    break
            if not found:   
                raise ValueError("Employee not found")

        else:
            raise ValueError("No such query number defined")

            
            

            


            


        






