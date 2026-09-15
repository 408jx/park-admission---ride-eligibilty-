print()
print()
# ------program introduction------
print("welcome to my Into The Jungle Theme Park! ")
print("lets get your tickets ready.")
print("lets also figure out what kind of ride you can go on! ")
print()
print()
# ------collecting guest information------ 
guest_name = input("whats your name? ")
visiters_age = int(input("how old are you? "))
height = float(input("what is your height in inches? "))
print()
print()
ticket = input("what type of ticket do you have (regular or premium? )")
member = input("are you a park member? (yes or no ) ")
guardian = input("are you visiting with an adult? (yes or no) ")
visit_time = input("what time are you coming to visit the park? (morning or evening) ")
print()
print()

price = 0
# ------determine the price of tickets by age------
def calculate_admission(visiters_age):
    if visiters_age <= 4:
        price = 0
    elif visiters_age <= 12:
        price = 15
    elif visiters_age <= 64:
       price = 30 
    else:
        price = 20 

    return price
print()
print()
# ------shows what type of discount you get------
def calculate_discount(price, member, visit_time):
    if member and visit_time == "evening":
        discount = 10
    elif member :
        discount = 5
    elif visit_time == "evening":
        discount = 3
    else: 
        discount = 0

    final_price = price - discount

    if final_price < 0:
        final_price = 0

    return final_price
print()
print()
# ------determines the highest ride level you are allowed to go on------ 
def ride_level(height, visiters_age):
    if 54 <= height and visiters_age >= 16:
        print ("you can go on the extreme rides")
    elif 48 <= height and visiters_age >= 12:
        print ("you can go on the thrill rides")
    elif 42 <= height and visiters_age >= 8:
        print ("you can go on the family rides")
    elif 38 <= height:
        print ("you can go on the kiddie rides")
    else:
        print("you cant go on any rides")
print()
print()
# ------determines if the guest under 13 is allowed with guardian------
def check_supervision(visiters_age, guardian):
    if visiters_age < 13 and not guardian:
        return "Adult required"
    else:
        return "Approved"
print()
print()
# -------shows what type of ticket you have------
def check_ticket(ticket):
    if ticket == "regular":
        return "you have regular ticket"
    else:
        return "PREMIUN BOUNUS: You receive a free snack and priority ride access!"
print()
print()

def check_vip(member, ticket, visiters_age):
    if ticket == "premium" and member or (visiters_age >= 65 and ticket == "premium"):
        print("VIP ACCESS")
    else:
        print("STANDARD ACCESS")    

price = calculate_admission(visiters_age)
print("==================================")
print("        Jungle Theme Park         ")
print("           Guest report           ")
print("==================================")

print("Guest:" ,guest_name)
print()
print("Age:" , visiters_age," years old")
print("height:" ,str(height)," inches")
print("ticket type:" ,ticket)
print()
print("Regular Admission:" , price)
print("Final Admission:" , calculate_discount(price, member, visit_time))
print()
print("Heighest Ride Level:")
print(ride_level(height, visiters_age))
print()
print("Supervision Status:")
print(check_supervision(visiters_age, guardian))
print()
print("premium bonus: ", check_ticket(ticket))
print()
print(check_vip(member, ticket, visiters_age))
print()
print("==================================")
print("have an awesome day at the park!  ")
print("==================================")
print()
print()
