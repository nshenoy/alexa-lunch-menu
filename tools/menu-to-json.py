import sys
import json
from datetime import datetime, timedelta

def main():
    # read in arguments
    menuFile = sys.argv[1]
    jsonFile = menuFile.replace(".txt", ".json")
    menuDate = sys.argv[2]

    # convert the menu text file to JSON
    convertMenuToJson(menuFile, jsonFile)

    # test retrieving a menu item
    getLunchByDate(jsonFile, menuDate)


def convertMenuToJson(menuFile, jsonFile):
    # read in the contents of the menu txt file
    with open(menuFile) as f_in:
        menuContents = (line.rstrip() for line in f_in) 
        menuContents = list(line.replace("&", "and") for line in menuContents if line) 
    
    # parse the contents to create a list of dictionaries
    menuByDate = []
    for i in range(len(menuContents)):
        try:
            menuByDate.append({"date": datetime.strptime(menuContents[i],"%A, %B %d").date().strftime("2019-%m-%d"), "item": menuContents[i+1]})
        except:
            continue

    # sort the menu by date
    menuByDateSorted = sorted(menuByDate, key = lambda i: i["date"])

    # save the JSON file
    with open(jsonFile, "w") as fout:
        json.dump(menuByDateSorted, fout)

def getLunchByDate(jsonFile, menuDate):
    if menuDate.lower() == "today":
        searchDate = datetime.today().strftime("%Y-%m-%d")
    else:
        searchDate = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    with open(jsonFile, "r") as jsonFile:
        lunchItems = json.load(jsonFile)

        for lunchItem in lunchItems:
            if lunchItem["date"] == searchDate:
                print("{}'s lunch is {}".format(menuDate.capitalize(), lunchItem["item"]))
                break


if __name__ == "__main__":
    main()
