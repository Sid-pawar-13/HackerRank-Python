if __name__ == '__main__':
    arr =[]
    N = int(input())
    for _ in range(N):
        cpn = input().split(' ')
        if cpn[0] == 'insert':
            arr.insert(int(cpn[1]),int(cpn[2]))
        if cpn[0] == 'remove':
            arr.remove(int(cpn[1]))
        if cpn[0] == 'sort':
            arr.sort()
        if cpn[0] == 'append':
            arr.append(int(cpn[1]))
        if cpn[0] == 'pop':
            arr.pop()
        if cpn[0] == 'reverse':
            arr.reverse()
        if cpn[0] == 'print':
            print(arr)