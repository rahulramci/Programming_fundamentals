customers=list()
products=list()


def print_bill(product_name,quantity,price,name,total):
    print('_'*20)
    print(f"{name} purchases {quantity} * {product_name}")
    print(f"Unit Price: {price} (AUD)")
    print(f"{name} gets a discount of 5.0 %")
    print(f"Total Price: {total} (AUD)")
    print('_'*20)
    return

def check_membership(name):
    for customer in customers:
        if name in customer.keys():
            if customer[name]!=True:
                res=input(f"Customer {name} doesn't have a membership, Do you want have a membership, Please type y/n:")
                if res == 'y':
                    customer[name]=True
                    return True
                else:
                    return False
            else: 
                return True

def generate_bill(product_name,quantity,name):
    res = check_membership(name)
    total=0
    price=0
    for product in products:
        if product_name in product.keys():
            price=product[product_name]
            if res == True:
                total_bef_dist=quantity*price
                # print(total_bef_dist)
                discount=(total_bef_dist*5)/100
                # print("discount",discount)
                total=total_bef_dist-discount
                # print(total)
                break
            else:
                total=quantity*price
                # print(total)
    print_bill(product_name,quantity,price,name,total)

def init_transaction():
    name = input("Enter The Name Of The Customer:")
    product_name= input("Enter the Product:")
    global customers, products
    # name is key, value defines the membership which is boolean
    customers.append({name:False})
    products.append({product_name:300})
    quantity=int(input("Enter The Product Quantity:"))
    generate_bill(product_name,quantity,name)
    return 

def main():
    init_transaction()
    # print(customers)
    # print(products)

if __name__=='__main__':
    main()
