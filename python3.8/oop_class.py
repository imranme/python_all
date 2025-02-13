# The blueprint to create monsters
class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

# Create some real monsters
fogthing = Monster("Black", 5)
mournsnake = Monster("Yellow", 4)
tangleface = Monster("Red", 3)

# Check whether those monsters got different existence in memory or not
print('I have ' + str(fogthing.heads) + ' heads and I\'m ' + fogthing.color)
print('I also have ' + str(mournsnake.heads) + ' heads and I\'m ' + mournsnake.color)
print('I got ' + str(tangleface.heads) + ' heads and I\'m ' + tangleface.color)



class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    def attack(self):
        print("Just attacked a Hero, Mu...hahahaha!!!")

# Create an instance/object/monster-character
mournsnake = Monster("Yellow", 4)
# Check if its created or not
print('I am a ' + str(mournsnake.heads) + ' headed monster.')
# Make an attack by the new monster
mournsnake.attack()1