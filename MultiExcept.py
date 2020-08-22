data = [1,2,3,4]

try:
    value = data[4]
except IndexError:
    print("Except Index out of range")
except:
    print("Except")
finally:
    print("Finally")
