# Last month Joe purchased some stock in Acme Software, Inc. Here are the
# details of the purchase:
# • The number of shares that Joe purchased was 1,000.
# • When Joe purchased the stock, he paid $32.87 per share.
# • Joe paid his stockbroker a commission that amounted to 2 percent of the
# amount he paid for the stock.

# Two weeks later Joe sold the stock. Here are the details of the sale:
# • The number of shares that Joe sold was 1,000.
# • He sold the stock for $33.92 per share.
# • He paid his stockbroker another commission that amounted to 2 percent of
# the amount he received for the stock.

# Write a program that displays the following information:
# • The amount of money Joe paid for the stock.
# • The amount of commission Joe paid his broker when he bought the stock.
# • The amount that Joe sold the stock for.
# • The amount of commission Joe paid his broker when he sold the stock.
# • Display the amount of money that Joe had left when he sold the stock and
# paid his broker (both times). If this amount is positive, then Joe made a
# profit. If the amount is negative, then Joe lost money.

# Create variable for stocks bought and stocks sold
stocks_bought = 1000
stocks_sold = 1000

# Create variable for purchase price and sell price
purchase_cost = 32.87
sell_cost = 33.92

# Create a variable for commission rate as a percentage
commission_rate = 0.02

# Create variables for the total paid for the stock when bought, and commision
# paid to broker during purchase
purchase_price = stocks_bought * purchase_cost
commission_for_purchase = purchase_price * commission_rate

# Create variables for the total paid for the stock when sold, and commision
# paid to broker during sell
sell_price = stocks_sold * sell_cost
commission_for_sale = sell_price * commission_rate

# Calculate total purchas cost, and total recieved during the sell
purchase_cost_total = purchase_price - commission_for_purchase
sell_total_recieved = sell_price - commission_for_sale

# Calculate profit
profit = sell_total_recieved - purchase_cost_total

# Display Information to the user
print("Amount paid for stock:       ", purchase_price)
print("Commission paid for purchase:", commission_for_purchase)
print("Amount stock sold for:       ", sell_price)
print("Commission paid for sell:    ", commission_for_sale)
print("Profit made:                 ", profit)
