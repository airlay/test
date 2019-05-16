def hourglassSum():
    arr = [[-9, -9, -9, 1, 1, 1],
           [0, -9, 0, 4, 3, 2],
           [-9, -9, -9, 1, 2, 3],
           [0, 0, 8, 6, 6, 0],
           [0, 0, 0, -2, 0, 0],
           [0, 0, 1, 2, 4, 0]]

    # get all the our glasses and put it in a new array
    rollsize = len(arr)
    columnsize = len(arr[0])
    result = []
    # glass hour is 3x3 matrix
    glasshoursize = 3
    for i in range(rollsize):
        for j in range(columnsize):
            if i+glasshoursize <= rollsize and j+glasshoursize <= rollsize:
                result.append(sum(arr[i][j:j+glasshoursize])+ arr[i+1][j+1]+ sum(arr[i+2][j:j+glasshoursize]))

    return (max(result))

if __name__ == '__main__':
    hourglassSum()
