"""
- Programmer: Ben Quiñones
- Task: Write and test a program that uses the pandas module to read and analyze five years of 
water meter readings from the city of Rexburg, Idaho.
- Purpose: Prove that you can write code that uses the pandas module to read and analyze data.
"""
print()
###############
## BEGINNING ##
###############
import csv



def main(): 
  #
    #
    product_dictionary = read_products("products.csv")
    request_dictionary = read_request("request.csv")

    print("Products")
    for _ in product_dictionary:
      #
      print(_, product_dictionary[_])
      #
    
    print()
    print("Requested Items")
    for _ in request_dictionary:
      #
      product_data = product_dictionary[_]
      request_data = request_dictionary[_]
      
      print(f"{product_data[0]}: {request_data[0]} @ {product_data[1]}")

      #
    
    
    #
  #



def read_products(filename):
  #
  product_dict = {}
  with open(filename, "rt") as csv_file:
    #
    reader = csv.reader(csv_file)
    next(reader)

    for row in reader:
      #
      product_num = row[0]
      name = row[1]
      price = float(row[2])

      product_dict[product_num] = [name, price]
      #
    #
  #
  return product_dict



def read_request(filename):
  #
  request_dict = {}
  with open(filename, "rt") as csv_file:
    #
    reader = csv.reader(csv_file)
    next(reader)

    for row in reader:
      #
      product_num = row[0]
      quantity = int(row[1])

      request_dict[product_num] = [quantity]
      #
    #
  #
  return request_dict


  
if __name__ == "__main__":
  #
  main()
  #



#########
## END ##
#########
print()