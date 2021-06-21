"""
Programmer: Ben Quiñones
Task: Compute and print the volume of a right circular cone.
Purpose: Strengthen your understanding of parameters, arguments, and local variable scope by fixing a program 
that won't run because the programmer tried to use variables that were defined in a different function.
"""
print()
###############
## BEGINNING ##
###############

def main():
    #
    province_list = readlist("provinces.txt")
    print(province_list)
    province_list.pop(0)
    province_list.pop()
    print()

    for _ in range(len(province_list)):
        #
        if province_list[_] == "AB":
            #
            province_list[_] = "Alberta"
            #
        print(province_list[_])
        #
        
    alberta_count = province_list.count("Alberta")
    
    print()
    print(f"The number of times 'Alberta' is listed is {alberta_count} times!")
    #

def readlist(filename):
    #
    text_list = []

    with open(filename, "rt") as text_file:
        #
        for line in text_file:
            #
            clean_line = line.strip()
            text_list.append(clean_line)
            #
        #
    return text_list
    #

if __name__ == "__main__":
    main()
#########
## END ##
#########
print()