import qcm
from difficulty import quoting, set_difficulty, is_random
import random
import time

if __name__ == '__main__':
    filename = "./QCM.txt"
    print("Bienvenue sur le QCM de projet 2 !")
    #On demande à l'utilisateur de choisir son nom d'utilisateur
    user = (input("Choissisez votre nom d'utilisateur C> "))
    print(f"Bonjour {user}")
    #On demande à l'utilisateur de choisir son niveau de difficulté
    difficulty_choice = ""
    while difficulty_choice == "" or difficulty_choice not in ["sympa", "severe", "mystere"]:
        print("Vous devez choisir un niveau existant !")
        difficulty_choice = input("Sélectionné un niveau de difficulté (sympa/severe/mystere) C> ")
    diff = set_difficulty(difficulty_choice)


    print("\n\n") #passement de ligne
    # Chargement du questionnaire
    questions = qcm.build_questionnaire(filename)
    print("Lecture du questionnaire.")
    #Tableau de notes
    quotes = []
    #Tableau de temps de réponse
    time_taked = []
    #modifié aléatoirement l'ordre des questions
    random.shuffle(questions)
    #On affiche les questions et les réponses possibles
    for q in range(len(questions)):
        print("\tQ| " + str(q + 1) + ": \"" + questions[q][0] + "\"")
        #On mélange l'ordre des réponses
        random.shuffle(questions[q][1])
        #Démarrage du "chrono"
        start_time = time.time()
        #On affiche les réponses possibles
        for r in range(len(questions[q][1])):
            print("\t\tA|" + str(r + 1) + ":" + f"\t{questions[q][1][r][0]}""")
        #On demande à l'utilisateur de choisir une réponse
        while True:
            #On gère le cas ou l'utilisateur entre une valeur non numérique
            try:
                #On demande à l'utilisateur de choisir une réponse
                answer = int(input(f"{user} C> "))
            except ValueError:
                """
                Si c'est une valeur non numérique par exemple '°' on reboucle la demande en affichant
                un petit message d'errerur
                """
                print("Entrez une valeur numérique !")
                continue
            #On gère le cas ou l'utilisateur entre une valeur qui ne satisfait pas les conditions
            if 1 <= answer <= len(questions[q][1]):
                end_time = time.time()  # Enregistrez l'heure de fin de la réponse
                time_taken = end_time - start_time  # Calculez le temps pris pour répondre
                time_taked.append(time_taken)  # Ajoutez-le au tableau time_taked
                #Cas ou l'utilisateur répond correctement à la question
                if questions[q][1][answer-1][1]:
                    print("Bonne réponse !")
                else:
                    # Cas ou l'utilisateur répond négativemet à la question
                    print("Mauvaise réponse")
                #On affiche le feedback si il y en a un
                if questions[q][1][answer - 1][2] != "":
                    print("Feedback: \"" + questions[q][1][answer - 1][2] + "\"")
                #On ajoute la note de la question au tableau de note
                quotes.append(quoting(questions[q][1][answer-1][1], q+1, diff))
                break
            else:
                #Ici on gère le cas ou l'utilisateur ne veut pas répondre
                if answer == 0:
                    end_time = time.time()  # Enregistrez l'heure de fin de la réponse
                    time_taken = end_time - start_time  # Calculez le temps pris pour répondre
                    time_taked.append(time_taken)  # Ajoutez-le au tableau time_taked
                    """
                    On ajoute une note de disons y pouvans valoir 0,-1, -2 si l'utilisateur ne veut pas répondre
                    (pour ne pas répondre ile tape 0)
                    """
                    if diff == 1:
                        quotes.append(0)
                    elif diff == 2:
                        quotes.append(-1)
                    elif diff == 3:
                        quotes.append(-2)
                    break
                print("Cette réponse n'est pas disponible, si vous ne voulez pas répondre tapez 0")
                #On reboucle la demande et on affiche la question suivante
                continue
    #On vérifie si l'utilisateur a répondu aléatoirement
    if is_random(time_taked):
        print("vous avez répondu aléatoirement")
        quotes = []
        #On ajoute des notes aléatoirement
        for q in range(len(questions)):
            quotes.append(random.randint(0, 11))
    #On affiche le total des notes
    print(f"Notes total : {sum(quotes)}/{len(questions)}")
