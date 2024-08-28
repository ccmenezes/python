# Lecture 02
# Operator

""" Determines if a shopping list item is eligible for free shipping """
"""Assignment operators"""
item_name='banana'
quantity=5
discount_race=0.1
eligible_items="orange banana carrot"
item_price=2 #Euro

""" Arithmetic operators """
# Calculate subtotal as item_price * quantity
subtotal=item_price * quantity

# print item_name, subtotal
print(f"item name: {item_name}, subtotal: {subtotal}")

# Initialize discount to 0
discount=0

""" Membership operators """
# Check if item_name is an eligible_items string
# (used to check if an item is eligible for a discount)
if item_name in eligible_items:
    discount=subtotal * discount_race
    subtotal=subtotal - discount
    
# print discount
print(f"discount: {item_name}, subtotal: {subtotal}")

""" Comparison operators """
# Check if discount is applied (discount > 0)
was_discount_applied = discount > 0
print(f"Was the discount applied? {was_discount_applied}")

""" Logical operators """
# Check if free shipping should be applied (quantity > 5 AND item_name = 'banana')
does_free_shipping_apply = quantity >= 5 and item_name == 'banana'
print(f"Is this item eligible for free shipping? {does_free_shipping_apply}")

