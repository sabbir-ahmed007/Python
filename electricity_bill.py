def bill(input):
    if input<=100:
        return input*10
    elif 100<input<= 200:
        return(100*10)+(input-100)*15
    elif 200<input<300:
        return (100*10)+(100*15)+(input-200)*20
    else:
        return (100*10)+(100*15)+(100*20)+(input-300)*25

    
unit=int(input("Enter the unit : "))    
billing = bill(unit)
print(billing)
