#The library at the Hogwarts School of Witchcraft and Wizardry has computerized its book issuing process. The relevant information is provided as text from standard input in three parts: information about books, information about borrowers and information about checkouts. Each part has a specific line format, described below.
#Information about books
#Line format: Accession Number~Title
#Information about borrowers
#Line format: Username~Full Name
#Information about checkouts
#Line format: Username~Accession Number~Due Date
#Note: Due Date is in YYYY-MM-DD format.
#You may assume that the data is internally consistent. For every checkout, there is a corresponding username and accession number in the input data, and no book is simultaneously checked out by two people.
#Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Books. The second section begins with a line containing Borrowers. The third section begins with a line containing Checkouts. The end of the input is marked by a line containing EndOfInput.
#Write a Python program to read the data as described above and print out details about books that have been checked out. Each line should describe to one currently issued book in the following format:
#Due Date~Full Name~Accession Number~Title
#Your output should be sorted in increasing order of due date. For books due on the same date, sort in increasing order of full name.

import sys

def main():
    accession_to_title = {}
    username_to_fullname = {}
    checkouts = []

    current_section = None

    for line in sys.stdin:
        line = line.strip()
        
        if line == "Books":
            current_section = "Books"
        elif line == "Borrowers":
            current_section = "Borrowers"
        elif line == "Checkouts":
            current_section = "Checkouts"
        elif line == "EndOfInput":
            break
        else:
            if current_section == "Books":
                accession_number, title = line.split('~')
                accession_to_title[accession_number] = title
            elif current_section == "Borrowers":
                username, full_name = line.split('~')
                username_to_fullname[username] = full_name
            elif current_section == "Checkouts":
                username, accession_number, due_date = line.split('~')
                full_name = username_to_fullname[username]
                title = accession_to_title[accession_number]
                checkouts.append((due_date, full_name, accession_number, title))

    # Sort by due date first, then by full name
    checkouts.sort()

    for checkout in checkouts:
        due_date, full_name, accession_number, title = checkout
        print(f"{due_date}~{full_name}~{accession_number}~{title}")

if __name__ == "__main__":
    main()


#--------------------------------------------------------------------------------------------------------#
#solution by instructor

# Dictionary to map accession number to title
books = {}
# Dictionary to map username to fullname
borrowers = {}
# List to store checkout data: accumulate, sort and print
checkouts = [] 

# Find the start of Books data
nextline = input().strip()
while nextline.find("Books") < 0:
    nextline = input().strip()

# Read upto start of Borrowers data
# Skip the line with "Books"
nextline = input().strip()
while nextline.find("Borrowers") < 0:
    (accession_number,title) = nextline.split('~')
    books[accession_number] = title
    nextline = input().strip()

# Read upto Checkout data
# Skip the line with "Borrowers"
nextline = input().strip()
while nextline.find("Checkouts") < 0:
    (username,fullname) = nextline.split('~')
    borrowers[username] = fullname
    nextline = input().strip()

# Process Checkouts
# Skip the line with "Checkouts"
nextline = input().strip()
while nextline.find("EndOfInput") < 0:
    (username,accession_number,due_date) = nextline.split('~')
    checkoutline = due_date+"~"+borrowers[username]+"~"+accession_number+"~"+books[accession_number]
    checkouts.append(checkoutline)
    nextline = input().strip()

# Print the output from checkouts
for checkoutline in sorted(checkouts):
    print(checkoutline)
