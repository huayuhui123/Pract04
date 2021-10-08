"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

lists=[]
def main():
    data = get_data()
    print(data)
def output(lists):
    n=len(lists)
    for i in range(0,n,1):
        print("{} is taught by {} and has {} students".format(lists[i][0],lists[i][1],lists[i][2]))

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        lists.append(parts)
        print("----------")
    input_file.close()
    print(lists)
    output(lists)

main()
