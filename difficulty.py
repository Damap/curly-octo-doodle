def set_difficulty(difficulty):
    """Trois niveau de difficulté :
        Sympa / Sévère / Mystère"""
    if difficulty == "sympa":
        return 1
    elif difficulty == "severe":
        return 2
    else: #difficulty random
        return 3

"""
Le param Q est le paramètre qui permet de savoir à quel questions on se trouve
Le param D est le niveau de difficulté choisi avant (1, 2 ou 3)
"""
def quoting(answer, q, d):
    if d == 1:
        if answer:
            return 1
        else:
            return 0

    elif d == 2:
        if answer:
            return 1
        else:
            return -1
    else:
        #à coder
        return True

