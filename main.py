class Portugal():
    def capital(self):
        print("capital of Portugal is:Lisbon")
    def language(self):
        print("most commonly spoken is portuguese and spanish")
    def type(self):
        print("Portugal is a developing country")

class Spain():
    def capital(self):
        print("capital of Spain is: Madrid")
    def language(self):
        print("the most commonly spoken is:Spanish")
    def type(self):
        print("Spain is a developing country")

#obj
Por = Portugal()
Spa = Spain()

for i in (Por,Spa):
    i.capital()
    i.language()
    i.type
