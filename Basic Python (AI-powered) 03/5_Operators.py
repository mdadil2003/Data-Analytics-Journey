# Sample data
sales = [1200, 450, 800, 1500, 300]
categories = ["Electronics", "Furniture", "Clothing"]

product_category = "Electronics"

# Arithmetic operators
total_sales = sum(sales)
average_sales = total_sales / len(sales)

# Comparison + Logical + Membership operators
high_value_sales = []

for sale in sales:
    if (sale > average_sales) and (sale >= 500):
        high_value_sales.append(sale)

# Membership check
if product_category in categories:
    category_status = "Valid category"
else:
    category_status = "Invalid category"

# Output
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("High Value Sales:", high_value_sales)
print("Category Check:", category_status)
