def convert(source,conversion_factor):
    ans=source*conversion_factor                  #function for conversion  
    return ans
source_currency=input("ENTER NAME OF SOURCE CURRENCY :")
source=int(input("ENTER AMOUNT OF SOURCE CURRENCY YOU WANT TO CONVERT :"))
final_currencyName=input("ENTER THE NAME OF FINAL CURRENCY AFTER CONVERSION :")
conversion_factor=float(input("ENTER THE CONVERSION FACTOR :"))
print(f"{source} in {source_currency} will be {convert(source,conversion_factor)} in {final_currencyName}")