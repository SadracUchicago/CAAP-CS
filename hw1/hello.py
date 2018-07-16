Name = input("HELLO WORLD... and hello you! What is your name?: ")
print("Cool. Hello", Name, "nice to meet you! ")


Color = input("What's your favorite color?: ")
List_Colors = ["Orange", "Black", "Pink", "Yellow"]

if Color.lower() == List_Colors[0].lower():
    print("Hey that's my favorite color too!")
elif Color.lower() == List_Colors[3].lower():
    print("That is an absolutely horrendous color, and I cannot associate with your kind!")
elif Color.lower() == List_Colors[1].lower():
    print("Ooh That's quite dark and mysterious. I appreciate darker shades")
elif Color.lower() == List_Colors[2].lower():
    print("That used to be my favorite color, until I realized it didn't fit the tones of my skin (which is weird "
          "because I'm a computer.)")
else:
    print("Hey, I've never heard of that color! I'm just a dumb computer, however. I'll look it up right now")

