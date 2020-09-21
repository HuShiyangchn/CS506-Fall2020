def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    csvmatrix = []
    with open(csv_file_path, "r") as file_object:
        lines = file_object.readlines()
        for line in lines:
            line = line.split(",")
            for i in range(len(line)):
                line[i] = eval(line[i])
            csvmatrix.append(line)
    print (csvmatrix[1])
    return csvmatrix

#read_csv("E://github//CS506-Fall2020//02-library//tests//test_files//dataset_1.csv")
