if __name__ == '__main__':
    s = input()
    alpha=alnum=digit=lower=upper=False
    for x in s:
        if x.isalnum():
            alnum=True
        if x.isalpha():
            alpha=True
        if x.isdigit():
            digit=True
        if x.islower():
            lower=True
        if x.isupper():
            upper=True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)        
                            
                
        
        
