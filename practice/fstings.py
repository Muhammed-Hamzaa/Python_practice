p1="placeholder1"
p2="placehloder2"

temp= "{1} is a good boy and {0} is a bad boy.".format(p1,p2)
print(temp)

#  or from python 3.6 onwards we can use f string

temp=f"{{p1}} is a good boy and {{p2}} is a bad boy."
print(temp)

temp=f"{p1} is a good boy and {p2} is a bad boy."
print(temp)

price=49.0022

# :.3f used to show upto two decimals
txt="for only{:.3f}"
print(txt.format(49.0022))

txt=f"for only {price:.3f}"
print(txt)