from collections import Counter
def profite():

    N = input("Enter a number of Shoes ")
    shoes = []
    for i in range(int(N)):
        numberofShoes = input("Enter a Shoe number ")
        shoes.append(int(numberofShoes))

    X = input("Enter a Number of Customer ")
    CustomerRequirement = []
    for j in range(int(X)):
        numberofCustomer = input("Enter Customer Shoe Size and price ")
        CustomerRequirement.append(tuple(numberofCustomer.split(' ')))

    print(Counter(CustomerRequirement).keys())
profite()