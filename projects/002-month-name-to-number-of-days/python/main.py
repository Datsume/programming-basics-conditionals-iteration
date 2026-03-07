

month= input()

#january = march = may = july = august = october = december = 31
#february = 28
#april = june = september = november = 30

month_31 = ["january","march","may","july","august","october","december"]
month_30 = ["april","june","september","november"]


if month in month_31:
    print(month,"= 31 days")
elif month in month_30:
    print(month, "= 30 days")
else month:
    print(month, "= 28 days")
