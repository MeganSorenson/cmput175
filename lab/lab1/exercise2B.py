# Exercise 2VB: Student's Choice
# reads the data in a text file where each line contains different info about an earthquake
# reorganizes data to create lists of earthquake magnitudes and their dates for each region
# creates a new file with this reorganized info

def get_contents(filename):
    # reads a file and gets it's contents
    # each line of the file contains an earthquake magnitude, date, time, lat, long, depth, and region
    #   separated by whitespace
    # filename is a str representing the text file name
    # returns a list of lists each containing a line of data
    file = open(filename, "r")
    contents = file.readlines()
    # remove newline characters and split info at each whitespace
    for i in range(len(contents)):
        contents[i] = contents[i].strip().split(" ")

    file.close()

    return contents


def group_by_region(contents):
    # groups earthwuake data by region using a dictionary
    # contents is a list of lists each containting a single earthquake's data
    # returns a dictionary of region : list of lists of all earthwuake data
    contents_by_region = {}

    for item in contents:
        # create a new key is the region doesn't already exist in the dictionary
        contents_by_region[item[-1]] = contents_by_region.get(item[-1], [])
        # append the earthwuake data to the appropriate region key's value list
        contents_by_region[item[-1]].append(item[0:6])

    return contents_by_region


def write_newfile(new_filename, contents_by_region):
    # write a new txt file with earthquake date and magnitude data for each region
    # eahc region's data is presented as [region, [date, mag], [date, mag]...] on separate lines
    # new_filename is a str representing the file name of the new txt file
    # contents_by region is a dictionary of region: earthquake data used to create the new file
    # returns NoneType
    new_file = open(new_filename, "w")

    # for each region key in the contents_by_region dictionary
    for region in contents_by_region.keys():
        # start the line off with the region
        new_file.write("[%s" % (region))
        # then for each earthquake data list in the corresponding value list;
        for data in contents_by_region[region]:
            # add the date and magnitude data
            new_file.write(", [%s, %.1f]" % (data[1], float(data[0])))
        # finally, end the region's line off with two newline characters
        new_file.write("]\n\n")

    new_file.close()


def main():
    # read file and get contents
    filename = "earthquake.txt"
    contents = get_contents(filename)
    # group magnitude and date data by region
    contents_by_region = group_by_region(contents)
    # write new file with data nd magnitude data for each region
    new_filename = "earthquakefmt.txt"
    write_newfile(new_filename, contents_by_region)


main()
