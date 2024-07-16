try:
    with open("file1.txt","r")as f1:
        result=f1.read()
    print(result.upper())
      
except FileNotFoundError as e:
    print(f"error- {e}")