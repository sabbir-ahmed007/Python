# Program to calculate Electricity Bill

# Given an integer U denoting the amount of KWh units of electricity consumed, the task is to calculate the electricity bill with the help of the below charges:

#         1 to 100 units – Rs. 10/unit
#         100 to 200 units – Rs. 15/unit
#         200 to 300 units – Rs. 20/unit
#         above 300 units – Rs. 25/unit

# Examples:

#     Input: U = 250
#     Output: 3500
#     Explanation:
#     Charge for the first 100 units – 10*100 = 1000
#     Charge for the 100 to 200 units – 15*100 = 1500
#     Charge for the 200 to 250 units – 20*50 = 1000
#     Total Electricity Bill = 1000 + 1500 + 1000 = 3500

#     Input: U = 95
#     Output: 950
#     Explanation:
#     Charge for the first 100 units – 10*95 = 950
#     Total Electricity Bill = 950 


def bill(input):
    if input<=100:
        return input*10
    elif 100<input<=200:
        return(100*10)+(input-100)*15
    elif 200<input<=300:
        return (100*10)+(100*15)+(input-200)*20
    else:
        return (100*10)+(100*15)+(100*20)+(input-300)*25

    
unit=int(input("Enter the unit : "))    
billing = bill(unit)
print(billing)
