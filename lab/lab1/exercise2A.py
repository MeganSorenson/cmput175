# Exercise 2A: Student's Choice
# reads the data in a text file where each line contains different info about a city and it's rainfall
# reorganizes data into categories (50-60mm), (60-70mm), (70-80mm), (80-90mm), (90-100mm)
# creates a new file with this reorganized info

def get_contents(filename):
    # open file and read it by line
    # filename is a str representing the name of the file to be read
    # returns a list of the lines in the file
    file = open(filename, "r")
    contents = file.readlines()
    file.close()
    # get rid of newline characters
    for i in range(len(contents)):
        contents[i] = contents[i].strip()
    return contents


def group_by_rain(contents):
    # creates dictionary of groups and groups lines based on rainfall
    # contents is a list of lines from a file
    #   with city name and rainfall separated by a space
    # returns a dictionary
    #   with str keys representing the groups
    #   with list values of the line contents

    # initial dict with empty lists as values
    rainfall_groups = {
        "[50-60 mm)": [],
        "[60-70 mm)": [],
        "[70-80 mm)": [],
        "[80-90 mm)": [],
        "[90-100 mm)": []
    }

    # split the city name and rainfall amount for each line
    # check the rainfall and assign the line contents to its respective group
    # based on rainfall amount
    for line in contents:
        line_contents = line.split(" ")
        line_rainfall = float(line_contents[1])
        if line_rainfall >= 90:
            rainfall_groups["[90-100 mm)"].append(line_contents)
        elif line_rainfall >= 80:
            rainfall_groups["[80-90 mm)"].append(line_contents)
        elif line_rainfall >= 70:
            rainfall_groups["[70-80 mm)"].append(line_contents)
        elif line_rainfall >= 60:
            rainfall_groups["[60-70 mm)"].append(line_contents)
        elif line_rainfall >= 50:
            rainfall_groups["[50-60 mm)"].append(line_contents)

    return rainfall_groups


def sort_groups(rainfall_groups):
    # sorts the values of a dict by rainfall from lowest to lowest
    # rainfall_groups is a dict
    #   keys are str representing rainfall categories
    #   values are a list of lists representing ["city", "rainfall"]
    # returns NoneType
    for value in rainfall_groups.values():
        value.sort(key=lambda x: x[1])


def make_new_file(rainfall_groups, new_filename):
    # creates a new file with the reorganized city-rain data
    # rainfall_groups is a dict
    #   keys are str representing rainfall categories
    #   values are a list of lists representing ["city", "rainfall"]
    # filename is a str of the new file's name
    #   under each category name, ther city name is centered in a field of 15 characters
    #   all uppercase for city names
    #   rainfall right aligned in a field of 5 charcaters with 1 digit to the right of the decimal
    # returns NoneType
    new_file = open(new_filename, "w")

    # for each category in the dictionary;
    #   write the category on a new line then,
    #   write the city and rain information on separate lines for each city
    #   use the string formating specification described in the function's description
    for category in rainfall_groups.keys():
        new_file.write("{} \n".format(category))
        for item in rainfall_groups[category]:
            new_file.write("{:^15}{:>5.1f} \n".format(
                item[0].upper(), float(item[1])))

    new_file.close()


def main():
    filename = "rainfall.txt"
    # open file and read lines
    contents = get_contents(filename)
    # group lines by rainfall into the five groups
    rainfall_groups = group_by_rain(contents)
    # sort the groups from lowest to highest rainfall
    sort_groups(rainfall_groups)
    # write file with the reorganized city-rain data
    new_filename = "rainfallfmt.txt"
    make_new_file(rainfall_groups, new_filename)


main()
