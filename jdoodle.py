#Write a program that asks the user to enter the total sales for the month. 
#From this figure, the application should calculate and display the following:
    # The amount of county sales tax
    # The amount of state sales tax
    # The total sales tax (county plus state)

COUNTY_SALES_TAX = 0.025
STATE_SALES_TAX = 0.05
    
def state_tax(tot_sales):
    #calculate state tax and returns it
    tax = float(tot_sales) * STATE_SALES_TAX
    return tax

def county_tax(tot_sales):
    #calculate county tax and returns it
    tax = float(tot_sales) * COUNTY_SALES_TAX
    return tax 

def total_tax(tot_sale):
    total_tax = tot_sale * (COUNTY_SALES_TAX + STATE_SALES_TAX)
    #calculate total tax and returns it
    return total_tax

def main():
    amount = float(input("Enter the total sales for the month: $"))

    print("\nState sales tax: $", format(state_tax(amount), ".2f"))
    print("County sales tax: $", format(county_tax(amount), ".2f"))
    print("Total sales tax: $", format(total_tax(amount), ".2f"))


if __name__ == "__main__":
    main()
    