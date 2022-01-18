# assumptions:
#   no whitespace at beginning of line
#   no blank lines in files
#   all bookIDs in borrowers.txt and returns.txt also  in books.txt
#   all studentIDs in borrowers.txt and returns.txt also in students.txt

def main():
    '''
    the main function of the program
    '''
    # create dictionary with the students in each classroom
    classroom_info = extract_classroom_info()

    # for each classroom, create the tables of borrowed books and owed amounts, and append it to a file
    for classroom, students in classroom_info.items():
        # create dictionary of student_name: list of [unreturned_book_name, due_date]
        unreturned_books = create_unreturned_book_dictionary(students)
        # create the first table with the unreturned book info and appedn to file
        create_table_one(classroom, unreturned_books)


def read_file_lines(filename, separator):
    '''
    opens and reads a file  and splits each line by a specified separator;
    filename is a str representing a text file's name;
    separator is a str representing the line's content separator;
    returns a list of lines from the text file
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
    extracts classroom info from lists of students from students.txt;
    creates a dictionary with the student info as the values and the classrooms as the keys (both str);
    returns this dictionary
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
    keeps track of the unreturned books of each student and adds them to a dictionary;
    keys are student name (str), values are list of lists of (book name, due date) (str);
    returns this dictionary
    '''
    unreturned_books = {}
    for student in students:
        studentID = student[0]
        student_name = student[1]
        # calculate the books that were borrowed but not returned by the student
        student_unreturned_books = get_unreturned_book_info(studentID)
        # add info to dictionary
        if len(student_unreturned_books) > 0:
            unreturned_books[student_name] = student_unreturned_books
    return unreturned_books


def get_unreturned_book_info(studentID):
    '''
    adds up all the unreturned book info for a specific student to a list;
    studentID is a str representing an individual student ID;
    returns a list of lists of all the (book_names, due dates) borrowed but not returned by that student
    '''
    # get borrowed books
    student_borrowed_books = get_borrowed_books(studentID)
    # get rid of returned books
    student_unreturned_books = list(
        remove_returned_books(studentID, student_borrowed_books))

    # get book names due dates for unreturned books
    unreturned_book_info = []
    for bookID in student_unreturned_books:
        book_info = [get_book_name(bookID), get_due_date(bookID)]
        unreturned_book_info.append(book_info)

    return unreturned_book_info


def get_borrowed_books(studentID):
    '''
    adds up all the borrowed book IDs for a specific student and adds then to a set;
    studentID is a strign representing the ID of the student of interest;
    returns a set of all the book IDs that the student borrowed
    '''
    # get all borrowed book info from borrowed.txt
    all_borrowed_books = read_file_lines('borrowers.txt', ';')

    # keep track of borrowed books for specific student
    student_borrowed_books = set()
    for book in all_borrowed_books:
        if book[1] == studentID:  # if the student IDs match
            student_borrowed_books.add(book[0])  # add book to set

    return student_borrowed_books


def remove_returned_books(studentID, borrowed_books):
    '''
    adds up all the returned bookIDs for a specific student to a set;
    studentID is a str representing an individual student ID;
    borrowed books is a set represneting the books borrowed by the student;
    returns a set of all the bookIDs not returned by that student
    '''
    # get history of returns lines from returns.txt
    all_returned_books = read_file_lines('returns.txt', ';')

    for book in all_returned_books:
        if book[1] == studentID:  # if the student IDs match
            borrowed_books.remove(book[0])  # remove book to set

    return borrowed_books


def get_book_name(bookID):
    '''
    finds the book name given a bookID;
    bookID is a str representing the ID of the book;
    returns the book name (str) if that book ID exists, otherwise returns NoneType
    '''
    # get all book info from books.txt
    all_books = read_file_lines('books.txt', '#')

    for book_info in all_books:
        if bookID == book_info[0]:  # if book IDs match
            return book_info[1]  # return book name


def get_due_date(bookID):
    '''
    finds the due date given a bookID;
    bookID is a str representing the ID of the book;
    returns the due date (str) if that book ID exists, otherwise returns NoneType
    '''
    # get all borrowed book info from borrowed.txt
    all_borrowed_books = read_file_lines('borrowers.txt', ';')

    for book_info in all_borrowed_books:
        if bookID == book_info[0]:  # if book IDs match
            return book_info[3]  # return due date


def create_table_one(classroom, unreturned_books):
    '''
    creates a table of unreturned book info for a classroom and appends it to a file named standing.txt;
    first column of table is student names sorted alphabetically;
    second column of table is names of unreturned books;
    third column of table is due dates of unreturned books;
    last row is total books unreturned for that classroom;
    classroom is a str representing the classroom number;
    unreturned books is a dictionary of student_name : list of [unreturned_book_names, due_dates]
    '''
    # create table structure elements
    first_col_width = 16
    second_col_width = 35
    third_col_width = 14
    horizontal_border = ('+' + ('-' * (first_col_width + 2)) + '+' +
                         ('-' * (second_col_width + 2)) + '+' + ('-' * (third_col_width + 2)) + '+')

    # write items to file
    file = open('standing.txt', 'a')
    file.write('Class: {number}\n'.format(number=classroom))  # table title
    file.write('{border}\n'.format(border=horizontal_border))  # top of table
    file.write('| {col1_label:<16.16} | {col2_label:<35.35} | {col3_label:<14.14} |\n'.format(col1_label='Student Name',
               col2_label='Book', col3_label='Due Date'))  # column names
    file.write('{}\n'.format(horizontal_border))
    # write a row for each unreturned book
    total_number_unreturned = 0
    for student, book_info in unreturned_books.items():
        total_number_unreturned += len(book_info)
        for book in book_info:
            # convert due date from numerical to written format
            date = convert_date(book[1])
            file.write('| {student_name:<16.16} | {book_name:<35.35} | {due_date:<14.14} |\n'.format(
                student_name=student, book_name=book[0], due_date=date))  # unreturned book row
    if total_number_unreturned > 0:  # only add another spearator is there were unreturned book rows
        file.write('+' + ('-' * (first_col_width + 2)) + '-' + ('-' * (second_col_width + 2)) +
                   '+' + ('-' * (third_col_width + 2)) + '+' + '\n')  # horizontal border above total row
    file.write('| {row_label:<54} | {total:>14} |\n'.format(
        row_label='Total Books', total=str(total_number_unreturned)))  # total unreturned row
    file.write('{border}\n'.format(border=horizontal_border))  # table bottom

    file.close


def convert_date(date):
    '''
    converts a date from YYMMDD to Mon Day, Year;
    date is a string representing a YYMMDD date;
    returns a str of the date in converted format
    '''
    month_conversions = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
        '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
        '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }

    year = '20' + date[0:2]
    month = month_conversions[date[2:4]]
    day = date[4:]

    return '{month} {day}, {year}'.format(month=month, day=day, year=year)


def create_table_two():
    '''
    contains the amount due by the students (sorted by student_name) and appends the table to a specified file for each classroom
        -first col is student name, second col is total amount due
        -line at end indicates the total amount due by the class' students;
    student owes the cost of the book from book.txt
        -line --> bookID#title#author_names#dollar_value;
    student only owes if the book was lost or damaged but not paid (from returns.txt)
        -line --> bookID;studentID;returned_date;book_state
        -date in YYMMDD
        -book_state --> 0 = good, 1 = lost, 2 = lost and paid, 3 = damaged and paid, otherwise damaged and need replacement but not paid
    '''
    pass


def display_classroom_totals():
    '''
    prints the class number, total books borrowed by the class, and total amount due of the class;
    does this for every class
    '''
    pass


main()
