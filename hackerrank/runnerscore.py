if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    k=list(set(arr))
    k.sort()
    print(k[-2])
    
    
