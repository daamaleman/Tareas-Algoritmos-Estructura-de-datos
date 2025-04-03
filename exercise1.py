from functools import reduce

# Function to request data from the user
def request_data():
    sales = []
    while True:
        product = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if product.lower() == 'salir':
            break
        try:
            quantity = int(input(f"Ingrese la cantidad vendida de {product}: "))
            unit_price = float(input(f"Ingrese el precio unitario de {product}: "))
            sales.append({"product": product, "quantity": quantity, "unit_price": unit_price})
        except ValueError:
            print("Por favor, ingrese valores válidos.")
    return sales

# Function to calculate total sales per product
def calculate_totals_per_product(sales):
    return list(
        map(lambda x: {"product": x["product"], "total": x["quantity"] * x["unit_price"]}, sales)
    )

# Function to filter products with total sales greater than a threshold
def filter_sales_greater_than(totals_per_product, threshold=100):
    return list(filter(lambda x: x["total"] > threshold, totals_per_product))

# Function to calculate the overall total sales
def calculate_overall_total(totals_per_product):
    return reduce(lambda acc, x: acc + x["total"], totals_per_product, 0)

# Function to calculate the average of total sales
def calculate_average_sales(overall_total, product_count):
    return overall_total / product_count if product_count > 0 else 0

# Main function
def main():
    sales = request_data()
    totals_per_product = calculate_totals_per_product(sales)
    sales_greater_than_100 = filter_sales_greater_than(totals_per_product)
    overall_total = calculate_overall_total(totals_per_product)
    average_sales = calculate_average_sales(overall_total, len(totals_per_product))

    # Results
    print("Totales por producto:", totals_per_product)
    print("Ventas mayores a 100:", sales_greater_than_100)
    print("Total general de ventas:", overall_total)
    print("Promedio de ventas:", average_sales)

# Run the program
if __name__ == "__main__":
    main()