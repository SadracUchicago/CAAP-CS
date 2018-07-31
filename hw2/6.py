speed_limit = int(input("What is the speed limit?:"))
offender_speed = int(input("\nWhat is the offender's speed?: "))
fine = 50
if offender_speed > speed_limit:
    fine += (offender_speed-speed_limit)*5
    if offender_speed > 90:
        fine += 200
    else:
        pass
    print(fine)
else:
    print("The person did not break the speed limit")
