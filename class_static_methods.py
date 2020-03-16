"""
Regular method-Instance as first argument
Add decorator "@classmethod" to change regular to class method

"""

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

    @classmethod
    def set_price_rise(cls,price):
        cls.price_raise=price

Samsung_tv=TV('Samsung',2000,32,30000)
LG_tv=TV('LG', 2010, 54, 4000)

#Working on class variable directly
print(Samsung_tv.price_raise)
print(LG_tv.price_raise)


#Use class method to change the price value (A class variable)
TV.set_price_rise(1.25)
print(Samsung_tv.price_raise)
print(LG_tv.price_raise)

