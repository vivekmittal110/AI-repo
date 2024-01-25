percentage = int(input("Enter your percentage : "))
if percentage > 80 and percentage < 101:
    print("very good")
elif percentage > 60 and percentage < 81:
    print("good")
elif percentage > 40 and percentage < 61:
    print("average")
elif percentage > 100:
    print("invalid percentage")
else :
    print("fail")