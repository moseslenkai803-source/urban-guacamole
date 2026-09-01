class House:
    bedrooms = 3
    bathrooms = 2
    floors = 1
    area = 120
    owner = ""
    location = ""
    architect = ""

macrine_house=House()
macrine_house.owner="Macrine"
macrine_house.location="Kikuyu"
macrine_house.architect="John Doe"
print(f"Macrine's House owner {macrine_house.owner} is located in {macrine_house.location} and has {macrine_house.bedrooms} bedrooms, {macrine_house.bathrooms} bathrooms, {macrine_house.floors} floors and an area of {macrine_house.area} square meters.")

daniel_house=House()
daniel_house.owner="Daniel"
daniel_house.location="Nairobi"
daniel_house.architect="Jane Doe"
print(f"Daniel's House owner {daniel_house.owner} is located in {daniel_house.location} and has {daniel_house.bedrooms} bedrooms, {daniel_house.bathrooms} bathrooms, {daniel_house.floors} floors and an area of {daniel_house.area} square meters.")