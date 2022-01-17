# books.txt contains info about all books in the library
#   bookID#title#author_names#dollar_value

# students.txt contains a list of students
#   studentID, student_name, class

# borrowers.txt contains the history of all loans
#   bookID;studentID;borrow_date;return_date
#   date in YYMMDD

# returns.txt contains info about the returns
#   bookID;studentID;returned_date;book_state
#   date in YYMMDD
#   book_state --> 0 = good, 1 = lost, 2 = lost and paid, 3 = damaged and paid, otherwise damaged and need replacement but not paid

# assumptions:
#   no whitespace at beginning of line
#   no blank lines in files
#   all bookIDs in borrowers.txt and returns.txt also  in books.txt
#   all studentIDs in borrowers.txt and returns.txt also in students.txt

def main():
    '''
    -the main function of the program
    '''
    # create dictionary with the students in each classroom
    classroom_info = extract_classroom_info()

    # for each classroom, create the tables of borrowed books and owed amounts, and append it to a file
    for classroom, students in classroom_info.items():
        # create dictionary of student_name: list of [unreturned_bookID, due date]
        unreturned_books = create_unreturned_book_dictionary(students)
        print(unreturned_books)


def read_file_lines(filename, separator):
    '''
    -opens and reads a file  and splits each line by a specified separator
    -filename is a str representing a text file's name
    -separator is a str representing the line's content separator
    -returns a list of lines from the text file
    '''
    # open and read file
    file = open(filename, 'r')
    contents = file.readlines()
    for i in range(len(contents)):
        contents[i] = contents[i].strip().split(separator)
    file.close()

    return contents


def extract_classroom_info():
    '''
    -extracts classroom info from lists of students from students.txt (line --> studentID,student_name,class)
    -creates a dictionary with the student info as the values and the classrooms as the keys (both str)
    -returns this dictionary
    '''
    # get student info lines from student.txt file
    contents = read_file_lines('students.txt', ',')

    # create dictionary to add to using the file contents
    classroom_info = {}

    for line_contents in contents:
        # get class number from the components and add student info appropriately to dictionary
        classroom = line_contents[2]
        student_info = (line_contents[0], line_contents[1])
        # create new classrooom key if it doesn't already exist
        classroom_info[classroom] = classroom_info.get(
            classroom, [])
        # add student info to dictionary
        classroom_info[classroom].append(student_info)

    return classroom_info


def create_unreturned_book_dictionary(students):
    '''
    -keeps track of the unreturned books of each student and adds them to a dictionary
    -keys are student name (str), values are list of lists of (book ID, due date) (str)
    -returns this dictionaru
    '''
    unreturned_books = {}
    for student in students:
        studentID = student[0]
        student_name = student[1]
        # calculate the books that were borrowed but not returned by the student
        student_unreturned_books = get_unreturned_books(studentID)
        # add info to dictionary
        if len(student_unreturned_books) > 0:
            unreturned_books[student_name] = student_unreturned_books
    return unreturned_books


def get_unreturned_books(studentID):
    '''
    -adds up all the borrowed bookIDs for a specific student to a set
    -studentID is a str representing an individual student ID
    -returns a list of lists of all the (bookIDs, due dates) borrowed by that student
    '''
    # get history of loans lines from borrowed.txt
    all_borrowed_books = read_file_lines('borrowers.txt', ';')
    # keep track of borrowed books for student
    student_borrowed_books = set()
    for book in all_borrowed_books:
        if book[1] == studentID:  # if the student IDs match
            student_borrowed_books.add(book[0])  # add book to set

    # get rid of returned books
    student_unreturned_books = list(
        remove_returned_books(studentID, student_borrowed_books))

    # add due dates to unreturned books
    student_unreturned_books = get_due_dates(
        all_borrowed_books, student_unreturned_books)

    return student_unreturned_books


def remove_returned_books(studentID, borrowed_books):
    '''
    -adds up all the returned bookIDs for a specific student to a set
    -studentID is a str representing an individual student ID
    -borrowed books is a set represneting the books borrowed by the student
    -returns a set of all the bookIDs not returned by that student
    '''
    # get history of returns lines from returns.txt
    all_returned_books = read_file_lines('returns.txt', ';')

    for book in all_returned_books:
        if book[1] == studentID:  # if the student IDs match
            borrowed_books.remove(book[0])  # remove book to set

    return borrowed_books


def get_due_dates(all_borrowed_books, student_unreturned_books):
    new_unreturned_list = []
    for book in student_unreturned_books:
        for book_info in all_borrowed_books:
            if book == book_info[0]:  # if book IDs match
                # add list of (book_ID, due date) to new list
                new_unreturned_list.append([book, book_info[3]])

    return new_unreturned_list


def create_table_two():
    '''
    -contains the amount due by the students (sorted by student_name) and appends the table to a specified file for each classroom
        first col is student name, second col is total amount due
        line at end indicates the total amount due by the class' students
    -student owes the cost of the book from book.txt
        line --> bookID#title#author_names#dollar_value
    -student only owes if the book was lost or damaged but not paid (from returns.txt)
        line --> bookID;studentID;returned_date;book_state
        date in YYMMDD
        book_state --> 0 = good, 1 = lost, 2 = lost and paid, 3 = damaged and paid, otherwise damaged and need replacement but not paid
    '''
    pass


def display_classroom_totals():
    '''
    -prints the class number, total books borrowed by the class, and total amount due of the class
    -does this for every class
    '''
    pass


main()
