  # import numpy as np

# list1 = np.array(["List"])
dict1 = {'Help' : "Show all the commands","Start" : "Aye Gaadi start kar", "Stop" : "Thamba Thamba" , "Quit" : "Bas ab bahut hua"}

command = ""
st_count = True
sp_count = True

while command != "quit":

    command = input("Enter command here: ")
    command = command.lower()

    if(command == "help"):
        print(dict1)
    elif(command == "start"):
        if(st_count):
            print("Aye Gadi Start Kar")
            st_count = False
        else:
            print("Haju ketlu chalu karu")
    elif(command == "stop"):
        if(sp_count):
            print("Gadiya Rok")
            sp_count = False
        else:
            print("Chalu j Che Chaapli")
    elif(command == "quit"):
        print("Nikal!")
        break
    else:
        print("Merko Maaloom Nai!")