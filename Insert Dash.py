#Insert Dash
#Takes a number and inserts dash in between consecutive odd numbers

def insert_dash(num):
    final = ""
    num = str(num)
    for i in range(0, len(num)):
        if i < (len(num) - 1):
            if int(num[i]) % 2 != 0 and int(num[i + 1]) % 2 != 0:
                final = final + num[i] + '-'
            else:
                final = final + num[i]
        elif i == (len(num) - 1):
            final = final + num[i]
    
    return final