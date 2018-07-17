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

Live = input("So, where do you live?: ")

print("Hey, turns out my computer grandma also lives in", Live)

print("But where do you want to move?: ")

Move = (input("Where would you like to live the rest of your days?: "))

print(Move, "is a really nice place, but I think the mainframe is a better place for my kind.")

print()

print("Well it was really nice meeting you", Name, "it's great that you like the color", Color, "and that you live in "
                                                                                                "the wonderful place "
                                                                                                "known as.", Live,
      "It's also great you aspire to live in an amazing place like", Move, "Well talk to you late. Bye WORLD!!")



