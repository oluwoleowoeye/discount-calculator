def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount_amount=price*(discount_percent/100)
        final_price=price-discount_amount
        return final_price
    else:
        return price
original_price=float(input("Enter the original price of item: "))
discount_percent=float(input("Enter the discount percentage of item: "))
final_price=calculate_discount(original_price,discount_percent)
if discount_percent >=20:
    print(f"final price after {discount_percent}% discount: NGN{final_price}")
else:
    print(f"no dicount applied discount: NGN{original_price}")