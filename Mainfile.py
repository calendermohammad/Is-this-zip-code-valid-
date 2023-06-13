# function
def validatezipcode(zipcode):    
    if len(zipcode) == 5 and zipcode.isdigit() == True:
        print("%s is a valid Zip Code!" %(zipcode))
    else:
        print("%s is not a valid Zip Code!" %(zipcode))
    
#call
zipcode = input("Please Enter Your Zip Code: ")
validatezipcode(zipcode)
