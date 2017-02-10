class Cup():
    color = ""
    @staticmethod
    def getCup(cupColor):
        if cupColor == "red":
            return RedCup()
        elif cupColor == "blue":
            return BlueCup()
        elif cupColor == "green":
            return GreenCup()
        else:
            return None

class RedCup(Cup):
    color = "red"

class BlueCup(Cup):
    color = "blue"

class GreenCup(Cup):
    color = "green"

redCup = Cup.getCup('red')
print("%s (%s)" % (redCup.color, redCup.__class__.__name__))
blueCup = Cup.getCup('blue')
print("%s (%s)" % (blueCup.color, blueCup.__class__.__name__))
greenCup = Cup.getCup('green')
print("%s (%s)" % (greenCup.color, greenCup.__class__.__name__))
