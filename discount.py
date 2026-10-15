import math
product=input("product name:")
price=float(input("product price:"))
discount_range=float(input("discount(%):"))

discount=price*discount_range/100 
final_price=price-discount

print("product:",product)
print("discount(%):",discount_range,"%")
print("bill:",final_price)