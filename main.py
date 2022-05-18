import random

def generate_rhythm ():
    pattern_rhythm = ""
    
    for eight_note in range(8):
        random_number = random.randint(1,2)
        if random_number == 1:
            pattern_rythm += " __  "
        elif eight_note % 2 == 0:
            pattern_rythm += "DOWN "
        else:
            pattern_rythm += " UP  "
    
    return pattern_rhythm

print("Try this: ", generate_rhythm())