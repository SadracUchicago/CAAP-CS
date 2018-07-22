# imports random madule form library
from random import randint

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

    def enter(self):
        print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
        print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
        exit(1)

class OWeek(Scene):

    name = "O-Week"

    def enter(self):
        print(
        "You are a college student-- a person whose future is on route but whose failure is just as easily available.\n"
        "It is a time for change; a time to move away from the vices that weighed you down but also a moment from which\n"
        "the virtues of familiarity have too left./n You are scared, and, as stupid as that might sound, you know that "
        "statement resonates deeply, for it's truth can only be as hidden as your shaking hands and wavering eyes can "
        "deny.\n")
        print()
        print(
        "It's O-Week-- orientation-- an although high school has bludgeoned you wit this so pettily before, you can't "
        "help but feel as though all eyes are on you.\nThere is no reason for this; you aren't abnormally tall nor "
        "short, you aren't ugly nor stupid, you're not wearing a MAGA hat nor exuberating conspicuity, and yet all you "
        "can feel are glances piercing through your skin with every step you take on the QUAD.")
        print()
        print(
        "It is now you realize you must take action and gets past your nervous tremors. You have to take control. THIS "
        "IS THE LIFE OF THE MIND, and you are the player. It is now your job to overcome your phobias before classes "
        "start.")
        print()
        print(
        "A girl walks up to you, and you're heart rate begins to raise. She's beautiful-- a Chicana with curly hair."
        "She asks you, if you're willing to go to a party with her and her friends around the block. At that same moment,?"
        "you get a text from an old friend who lives in Chicago, asking you to come over and play on his PS4.\nQUICK!")
        print("What do you do")

        return self.action()


    def action(self):
        print("What do you do?")
        print("Type A for: Reject her and go to your old friend's house.")
        print("Type B for: Reject him and go to the party.")
        print("Type C forL Reject both and begin studying for your class next week-- math.")
        choice = input("> ")
        if choice == ':q':
            return self.exit_scene(choice)
        # this is some exception handling, you don't need to worry about it,
        # just accept that it works and keeps the program from falling apart.
        try:
           choice = int(choice)
        except ValueError:
           print("That's not an int!")
           return self.exit_scene(self.name)

        if int(choice) == 1:
            print ("Quick on the draw you yank out your blaster and fire it at the Gothon.")
            raise ValueError ('todo')
            return self.exit_scene('death') # raise ValueError ('todo')
        elif int(choice) == 2:
            print ("Like a world class boxer you dodge, weave, slip and slide right")
            raise ValueError ('todo')
            return self.exit_scene('death') # raise ValueError ('todo')
        elif int(choice) == 3:
            print ("Lucky for you they made you learn Gothon insults in the academy.")
            raise ValueError ('todo')
            return self.exit_scene('laser_weapon_armory') # raise ValueError ('todo')
        else:
            print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
            return self.exit_scene(self.name)

    def exit_scene(self, outcome):
        return outcome

class LaserWeaponArmory(Scene):

    name = raise ValueError ('todo')

    def enter(self):
        print ("You do a dive roll into the Weapon Armory, crouch and scan the room")
        raise ValueError ('todo')
        return raise ValueError ('todo')

    def action(self):
        print ("There's a keypad lock on the box")
        raise ValueError ('todo')
        code = [randint(0,9), randint(0,9), randint(0,9)]
        guesses = 0
        # loop to check three random integers, one at a time
        for i in range(3):
            print ("Enter digit %d." % (i+1))
            guess = input("[keypad]> ")
            if guess == ':q':
                return self.exit_scene(guess)
            try:
               guess = int(guess)
            except ValueError:
               print("That's not an int!")
               return self.exit_scene(self.name)
            while int(guess) != code[i] and guesses <10:
                print ("BZZZZEDDD!")
                guesses += 1
                guess =input("[keypad]> ")
                if guess == ':q':
                    return self.exit_scene(guess)
                try:
                   guess = int(guess)
                except ValueError:
                   print("That's not an int!")
                   guess = -1

        if guesses < 10:
            print ("The container clicks open and the seal breaks, letting gas out.")
            raise ValueError ('todo')
            return self.exit_scene('the_bridge')
        else:
            print ("The lock buzzes one last time and then you hear a sickening")
            raise ValueError ('todo')
            return self.exit_scene('death') # raise ValueError ('todo')

    def exit_scene(raise ValueError ('todo')):
        return raise ValueError ('todo')

class TheBridge(Scene):

    name ='the_bridge'

    def enter(self):
        raise ValueError ('todo')

    def action(self):
        raise ValueError ('todo')

    def exit_scene(self, outcome):
        raise ValueError ('todo')

class EscapePod(Scene):

    name = 'escape_pod'

    def enter(self):
        raise ValueError ('todo')


    def action(self):
        print ("There's 5 pods, which one do you take?")
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if guess == ':q':
            return self.exit_scene(guess)
        try:
           guess = int(guess)
        except ValueError:
           print("That's not an int!")
           return self.exit_scene(self.name)

        if int(guess) != good_pod:
            print ("You jump into pod %s and hit the eject button."% guess)
            raise ValueError ('todo')
            return self.exit_scene('death')
        else:
            print ("You jump into pod %s and hit the eject button."% guess)
            raise ValueError ('todo')
            return self.exit_scene('finished')

    def exit_scene(self, outcome):
        raise ValueError ('todo')