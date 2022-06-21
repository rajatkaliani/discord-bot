import requests
res = requests.get("https://api.coingecko.com/api/v3/coins/list")
print(res)
jsonResponse = res.json()
# print(jsonResponse)

class Crypto:
    def __init__(self, id, symbol, name):
        self.id = id
        self.symbol = symbol
        self.name = name

# 1) Create an empty array
# 2) Add all the cryptos as Crypto objects into the new array
# 3) In a new loop, you're only going to print the cryptos that start with the letter a


# A-Cryptos are cryptos with names that start with A
# 4) Find the total number of A-Cryptos where their symbol starts with a vs. doesn't & print
newCrypto = []
aCrypto = 0
notACrypto = 0
for obj in jsonResponse:
    newobj = Crypto(obj["id"], obj["symbol"], obj["name"])
    newCrypto.append(newobj)
    # This conditional statement checks if the first letter of all crypto object names start with a
    if (newobj.name[0] == "A" or newobj.name[0] == "a"):
    # This conditional statement checks if the first letter of each crypto symbol starts with a
        if (newobj.symbol[0].lower() != "a"):
            print(newobj.symbol)
            # A counter to check how many crypto symbols of the crypto names that start with A dont start with A
            notACrypto = notACrypto + 1
        else:
            #  A counter to check how many crypto symbols of the crypto names that start with A start with A
            aCrypto = aCrypto + 1
            # this prints
print(aCrypto)
print(notACrypto)

                



    

