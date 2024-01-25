cost_price = int(input("Enter cost price : "))
selling_price = int(input("Enter selling price : "))
if cost_price > selling_price :
    print("the seller has incurred loss of", (selling_price-cost_price))
elif cost_price < selling_price :
    print("the seller has made profit of", (selling_price-cost_price))
else :
    print("The seller has made no profit no loss")