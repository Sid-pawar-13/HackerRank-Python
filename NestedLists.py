if __name__ == '__main__':
    marksheet = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([score, name])
    marksheet.sort()
    second_lowest = 0
    for i in range(len(marksheet)):
        if(marksheet[0][0] < marksheet[i][0]):
            second_lowest = marksheet[i][0]
            break
    for sublist in marksheet:
        if sublist[0] == second_lowest:
            print(sublist[1])
#records = [['Harry',3721],['Berry',3721],['Tina',3720],['Akriti',4100],['Harsh',3900]]