def find_left_handed_seats(table):
    # --- To check the asigned seat
    # Init count in 0
    count = 0
    for i in range(4):
        # Borderline case first seat
        if i == 0:
            if table[0][i] == "U" and table[0][i+1] != "R":count += 1   # ---table[0][i] = "L"
            if table[1][i] == "U" :count += 1                           # ---table[1][i] = "L"
                
        # Borderline Case last seat
        elif i == len(table[0])-1:
            if table[0][i] == "U":count += 1                            # ---table[0][i] = "L"
            if table[1][i] == "U" and table[1][i-1] != "R":count += 1   # ---table[1][i] = "L" 

        # Other cases
        else:
            if table[0][i] == "U" and table[0][i+1] != "R":count += 1   # ---table[0][i] = "L"
            if table[1][i] == "U" and table[1][i-1] != "R":count += 1   # ---table[1][i] = "L"
                
    return count

if __name__ == '__main__':
    print(find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]))
    print('--------')
    print(find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]))
    print('--------')
    print(find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]))
    print('--------')
    print(find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]))
    print('--------')
    print(find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]))
    print('--------')