
phone_book = [{"name": "Dmytro", "age": 42}]


def print_entry(entry):
    print "-------------------------"
    print "Name:    " + entry["name"]
    print "Age:     " + str(entry["age"])


def print_phonebook():

    print ""
    print "###### Phone book #######"
    print ""

    for entry in phone_book:
        print_entry(entry)

def add_entry_phonebook(name, age):
    entry = {}
    entry["name"] = name
    entry["age"] = age
    phone_book.append(entry)

def find_entry_name_phonebook(name):
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(entry)
            return
    print "Not found!!"


def main():
    while True:
        try:
            print ""
            print ""
            print ""
            print "~ Welcome to phonebook ~"
            print "Select one of actions below:"
            print "     1 - Print phonebook entries"
            print "     2 - Add new entry"
            print "     3 - Find entry by name"
            print "     4 - Find entry by age"
            print "     5 - Delete entry by name"
            print "-----------------------------"
            print "     0 - Exit"

            choice = int(raw_input("Enter you choice: "))

            if choice==1:
                print_phonebook()
            elif choice==2:
                name = str(raw_input("    Enter name: "))
                age = int(raw_input( "    Enter age: "))
                add_entry_phonebook(name, age)
            elif choice==3:
                name = str(raw_input("    Enter name: "))
                find_entry_name_phonebook(name)
            elif choice==4:
                print "--- TBD ---"
            elif choice==5:
                print "--- TBD ---"

            elif choice==0:
                print "Bye!"
                break
            else:
                print "Enter action within range [0..5]"

        except ValueError:
             print "Oops!  Something went wrong.  Try again..."



if __name__ == '__main__':
    main()



#   H/W:
#   0. Print sequential number of phonebook entry, when phonebook is printed. E.g. 
#       [ 1 ]-----------------
#       Name: ...
#       Age: ...
#       [ 2 ]-----------------
#       Name: ...
#       Age: ...
#   1. Implement function 'find_entry_age_phonebook'
#   2. Implement function 'delete_entry_name_phonebook'
#   3. Add support to save information about surname
#   4. Modify print phonebook function, so that it prints surname as well.
