#COMPLETE
import csv
import os


FILENAME = "region1_sales.csv"

def import_sales_from_file():
    print("Enter name of file to import: ")
    
   

#COMPLETE
def exit_program():
    print("Terminating program.")
    

#NEEDS TO BE FIXED WON'T DISPLAY MORE 1.0
#  GION1_SALES.CSV won't display more THAN 2 !
def command_view():
    print("\tDate\t\tQuarter\t\tAmount")
    print("---------------------------------------------------------------")
    for line in sales:
        print('1\t{} \t {} \t\t{}'.format(line[0], line[1],line[2]))
    print("==============================================================")
    print("TOTAL:")
        
def write_sales(sales):
    try:
        with open(FILENAME, "w", newline="") as file:
#            raise BlockingIOError("Error raised for testing.")
            writer = csv.writer(file)
            writer.writerows(sales)
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

# THIS IS WRONG NEED TO DELETE OR FIX!!!
#def command_add():
    #amount = 0.0
    #for line in sales:
        #try:
            #float(line[1])
            #amount += float(line[1])
        #except ValueError:
            #print("Using sales amount of 0 for {}".format(line[0]))

    #average = round(amount / 12, 2)

    #print('amount:     {}\n'
          #'Monthly average:  {}'.format(amount, average))

# NEEDS WORK THIS ONE IS ADD BUT NEEDS TO WRITE A CSV FILE!
#def command_add():
#    new_sales = input("Amount: ")
#    for i in range(len(sales) + 1):
#        if command_add == sales[i][0]:
#            sales[i][1] = new_sales
#            break
#    with open('./monthly_sales.csv', 'w') as csvfile:
#        write = csv.writer(csvfile, delimiter=',', lineterminator='\n')
#        for row in sales:
#            write.writerow(row)
#        print('Sales ammount for {} was modified.'.format(command_add))

def command_add():
    amount = input("Amount:\t\t ")
    year = input("Year:\t\t ")
    month = input("Month  (1-12):\t ")
    day = input("Day  (1-31):\t ")
#    while True:
#        try:
#            amount = input("Amount:\t")
#            year = int(input("Year: "))
#            month = input("Month (1-12):\t ")
#            day = input("Day 1-31:\t ")

#        except ValueError:
#            print("Invalid integer. Please try again.")
#            continue
#        if year <= 0:
#            print("Year must be greater than zero. Please try again.")
#            continue
#        else:
#            break
    sale = [amount, year, month, day]
    sales.append(sale)
    write_sales(sales)
    print(f"{sales} was added.\n")


# COMPLETE
def main_program():
    print_once = True
    print('SALES DATA IMPORTER')
    
    while True:
        if print_once:
            print("\nCOMMAND MENU\n"
              "view    - View all sales\n"
              "add     - Add sales\n"
              "import  - Import sales from file\n"
              "menu    - Show menu\n"
              "exit    - Exit program")

        print_once = False
        
        command = input("\nPlease enter a command: ")
        if command.lower() == 'view':
            command_view()
        elif command.lower() == 'add':
            command_add()
        elif command.lower() == 'import':
            command_import()
        elif command.lower() == 'menu':
            main_program()
        elif command.lower() == 'exit':
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
            

#COMPLETE
if __name__ == "__main__":
    sales = []
    if not os.path.exists('./region1_sales.csv'):
        print("Program can't find csv file")
        exit()
    with open('region1_sales.csv', 'r') as csfile:
        reader = csv.reader(csfile.readlines())
        for line in reader:
            sales.append(line)

    main_program()

  