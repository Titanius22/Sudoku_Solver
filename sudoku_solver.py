import csv
import timeit

def return_empty_2d_matrix():
    return [
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]
             ]


def return_empty_3d_matrix():
    return [
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]]
             ]


def import_input():
    
    global zero_count

    matrix = return_empty_2d_matrix()

    with open('sudoku_input.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = 0
        for row in csv_reader:
            column_count = 0
            for element in row:
                if element: # if the string is "", then it equals false
                    matrix[row_count][column_count] = int(element)
                else:
                    zero_count += 1
                column_count += 1
                if column_count == 9:
                    break
            row_count +=1
            if row_count == 9:
                break
    return matrix


def check_row(rowNum):
    #print(input_matrix[rowNum])
    return set(range(1, 10)).difference(set(input_matrix[rowNum]))
    

def check_box(rowNum, colNum):
    box = []

    startingRow = rowNum - (rowNum%3)
    startingCol = colNum - (colNum%3)

    for row in range(startingRow, startingRow+3):
        for col in range(startingCol, startingCol+3):
            box.append(input_matrix[row][col])
    return set(range(1, 10)).difference(set(box))


def check_column(colNum):
    box = []

    for row in range(0, 9):
        box.append(input_matrix[row][colNum])
    return set(range(1, 10)).difference(set(box))


#Variables
input_matrix = []
box_search_order = []
zero_count = 0
found_count = 0


def main1():
    
    start = timeit.default_timer()

    global input_matrix
    global box_search_order
    global found_count
    
    input_matrix = import_input()
    choices_matrix = return_empty_3d_matrix()
    box_search_order = [[0,0],
                        [0,2],
                        [2,0],
                        [2,2],
                        [0,1],
                        [1,0],
                        [1,2],
                        [2,1],
                        [1,1]
                       ]

    
    for out_row in input_matrix:
        print(out_row)
    
    for i in range(0, 5):
        for box in box_search_order: #for each box
            missing_box_set = check_box(3*box[0], 3*box[1])
            if len(missing_box_set) < 1:
                continue
            for row in range(3*box[0], 3 + (3*box[0])): #each row in box
                missing_row_set = check_row(row)
                if len(missing_row_set) < 1:
                    continue
                for col in range(3*box[1], 3 + (3*box[1])): #each col item
                    if input_matrix[row][col] == 0:
                        missing_col_set = check_column(col)
                        choices_matrix[row][col] = missing_box_set.intersection(missing_row_set, missing_col_set)
                        if len(choices_matrix[row][col]) == 1:
                            #print("found one!!")
                            found_count += 1
                            input_matrix[row][col] = next(iter(choices_matrix[row][col]))
        
        print("Done!!")
        print("zeros: " + str(zero_count))
        print("found: " + str(found_count))
        for out_row in input_matrix:
            print(out_row)


    stop = timeit.default_timer()

    print('Time: ', stop - start) 

if __name__ == '__main__':
    main1()