
counter = 0
while counter < 3:
    print("Outer loop iteration:", counter)
    
    for i in range(2):
        print("    Inner loop iteration:", i)
    
    counter += 1