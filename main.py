def find_left_handed_seats(table):
    count = 0
    for i in range(4):
        if table[0][0] == "U":
            table[0][0] = "L"
            count += 1
        if table[0][i] == "U" and i != 4 and table[0][i+1] != "R":
            table[0][i] = "L"
            count += 1
        if table[1][i] == "U" and i != 0 and table[1][i-1] != "R":
            table[1][i] = "L"
            count += 1


    return table

if __name__ == '__main__':
    print(find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]))
    print('--------')
    #print(find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]))
    print('--------')
    #print(find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]))
    print('--------')
    #print(find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]))
    print('--------')
    #print(find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]))
    print('--------')