"""

Class variables
Instance variables
__dict__ classmethod

"""

# Python Oops
class TV:
    num_of_tvs = 0
    price_raise = 1.05
    remote=True
    color='Black'

    def __init__(self, company, model,size,rate):
        self.company=company
        self.model=model
        self.size=size
        self.rate=rate
        self.customer_care_id='customer_care@'+company+'.com'

        #TV.num_of_tvs=TV.num_of_tvs+1
        TV.num_of_tvs += 1

    def details(self):
        return '{} {}'.format(self.company,self.model)

    def rate_increase(self):
        self.rate= int(self.rate*self.price_raise)


Samsung_tv=TV('Samsung', 2000, 32, 30000)
LG=TV('LG',2010,54,4000)


#Method

print(Samsung_tv.details())

#Thunder or Magic Method
print(Samsung_tv.__dict__)
print(TV.__dict__)

#Class variable value
print(TV.num_of_tvs)

print(Samsung_tv.color)
print(LG.color)

print(Samsung_tv.remote)
print(LG.remote)

#Instance variable
print(Samsung_tv.size)
print(LG.size)