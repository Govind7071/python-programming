#create a function that accpets any number of keyword arguments and prints them in the format key:value
def kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


kwargs(name="govind",title="yadav")
kwargs(name="akash")
kwargs(river="ganga",fruit="mango",sweet="gulab jamun")