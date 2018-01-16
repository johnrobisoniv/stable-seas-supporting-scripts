import csv
import json


def radarGen(infile, outfile):

    # open outfile in write mode
    f = open(outfile, 'w')

    # build rowsArr and populate with data from csv
    # so we can access with indices
    with open(infile,'r') as csvFile:
        rows = csv.reader(csvFile)
        c = 0
        rowsArr = []
        for row in rows:
            rowsArr.append(row)

    # create dictionary to store output data
    radarData = {}

    # loop through rowsArray
    for i in range(1, len(rowsArr)):
        countryArray = []
        for j in range(3,len(rowsArr[i])):
            subdict = {}
            subdict['axis'] = rowsArr[0][j]
            subdict['value'] = float(rowsArr[i][j])
            countryArray.append(subdict)
        dct[rowsArr[i][1]] = countryArray
    # write dictionary, converted to json string, to outfile
    f.write( json.dumps(dct) )


if __name__ == '__main__':
    main()
