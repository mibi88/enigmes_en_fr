from tkinter import *
from tkinter.messagebox import *

mainwindow = Tk()
mainwindow.title("Défi !")
try:
   mainwindow.iconphoto(False, PhotoImage(file="main2.png"))
except TclError:
   showwarning("Fenêtre tkinter", "Icone introuvable !")

def rstart():
   # on gère les défis affichés et cachés.
   endw.pack_forget()
   defi1.pack()
   aidedefi.pack()
   # On vide les entrées de texte :
   entree.delete(0, "end")
   entree2.delete(0, "end")
   entree3.delete(0, "end")
   entree4.delete(0, "end")
   entree5.delete(0, "end")
   entree6.delete(0, "end")
   entree7.delete(0, "end")
   entree8.delete(0, "end")
   entree9.delete(0, "end")
   entree10.delete(0, "end")
   entree11.delete(0, "end")
   entree12.delete(0, "end")
   # On affiche le message de début.
   showinfo("Statut du jeu", "Vous recommencez !")

# gestion des defis affichés
statdefi = 1


defi1 = LabelFrame(mainwindow, text="Défi n°1 !", padx=20, pady=20)
defi1.pack(fill="both", expand="yes")
def verif():
   averif=entree.get()
   if averif == actualrep:
      showinfo("Réponse au défi 1", "Bravo !!!")
      defi1.pack_forget()
      aidedefi1.pack_forget()
      defi2.pack()
      aidedefi2.pack()
   else:
      showinfo("Réponse au défi 1", "C'est pas bon, réssayez")
      statresult = 0

rep = "MDP"
averif="MDP"
textdefi1 = Label(defi1, text="Devinez le MDP* (écrivez les lettres en majuscule)!")
textdefi1.pack()
textdefi2 = Label(defi1, text="Indice : Un Chat courT sur l'Herbe DePuis unE demi-heure.")
textdefi2.pack()
actualrep = "UCTHDPE30"
entree = Entry(defi1, textvariable=rep, width=30)
entree.pack()
verifbut=Button(defi1, text="Verifier", command=verif)
verifbut.pack()

aidedefi = LabelFrame(defi1, text="Aide", padx=20, pady=20)
aidedefi.pack(fill="both", expand="yes")

aidedefi1 = Label(aidedefi, text="* Mot De Passe")
aidedefi1.config(font=("Liberation Sans", 8))
aidedefi1.pack()

# Défi n°2 !

defi2 = LabelFrame(mainwindow, text="Défi n°2 !", padx=20, pady=20)
defi2.pack(fill="both", expand="yes")

def verif2():
   averif=entree2.get()
   if averif == "chance":
      showinfo("Réponse au défi 2", "Bravo !!!")
      defi2.pack_forget()
      aidedefi2.pack_forget()
      defi3.pack()
      aidedefi3.pack()
   else:
      showinfo("Réponse au défi 2", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi2, text="Trouvez le mot magique*. Écrivez tout en minuscules.")
textdefi1.pack()
textdefi2 = Label(defi2, text="Indice : J'espère que vous aurez de la chance.")
textdefi2.pack()
entree2 = Entry(defi2, textvariable=rep, width=30)
entree2.pack()
verifbut2=Button(defi2, text="Verifier", command=verif2)
verifbut2.pack()

aidedefi2 = LabelFrame(defi2, text="Aide", padx=20, pady=20)
aidedefi2.pack(fill="both", expand="yes")

aidedefi2lb = Label(aidedefi2, text="* Qu'est ce qui est bien ?")
aidedefi2lb.config(font=("Liberation Sans", 8))
aidedefi2lb.pack()
defi2.pack_forget()
aidedefi2.pack_forget()

# Défi n°3 !

defi3 = LabelFrame(mainwindow, text="Défi n°3 !", padx=20, pady=20)
defi3.pack(fill="both", expand="yes")

def verif3():
   averif=entree3.get()
   if averif == "2":
      showinfo("Réponse au défi 3", "Bravo !!!")
      defi3.pack_forget()
      aidedefi3.pack_forget()
      defi4.pack()
      aidedefi4.pack()
   else:
      showinfo("Réponse au défi 3", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi3, text="Trouvez quelle suite de nombres n'est pas dans la suite de fibonacci*. Écrivez juste le numéro, sans espaces autour.")
textdefi1.pack()
textdefi2 = Label(defi3, text="Indice : 1. 1,1,2,3,5 | 2. 34,55,89,144,232,377,610 | 3. 2585,4183,6768,10951")
textdefi2.pack()
entree3 = Entry(defi3, textvariable=rep, width=30)
entree3.pack()
verifbut3=Button(defi3, text="Verifier", command=verif3)
verifbut3.pack()

aidedefi3 = LabelFrame(defi3, text="Aide", padx=20, pady=20)
aidedefi3.pack(fill="both", expand="yes")

aidedefi3lb = Label(aidedefi3, text="* Voici comment calculer la suite de fibonacci : Pour la trouver additionnez tout le temps les deux dernier chiffres de la suite. Commencez par 1 et 1 : 1,1,2(1+1),3(2+1), ...")
aidedefi3lb.config(font=("Liberation Sans", 8))
aidedefi3lb.pack()
defi3.pack_forget()
aidedefi3.pack_forget()

# Défi n°4 !

defi4 = LabelFrame(mainwindow, text="Défi n°4 !", padx=20, pady=20)
defi4.pack(fill="both", expand="yes")

def verif4():
   averif=entree4.get()
   if averif == "1":
      showinfo("Réponse au défi 4", "Bravo !!!")
      defi4.pack_forget()
      aidedefi4.pack_forget()
      defi5.pack()
      aidedefi5.pack()
   else:
      showinfo("Réponse au défi 4", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi4, text="Quelle distribution linux utilise* des paquets \".tcz\"")
textdefi1.pack()
textdefi2 = Label(defi4, text="Indice : 1. TinyCore | 2. Pear OS | 3. Fedora")
textdefi2.pack()
entree4 = Entry(defi4, textvariable=rep, width=30)
entree4.pack()
verifbut4=Button(defi4, text="Verifier", command=verif4)
verifbut4.pack()

aidedefi4 = LabelFrame(defi4, text="Aide", padx=20, pady=20)
aidedefi4.pack(fill="both", expand="yes")

aidedefi4lb = Label(aidedefi4, text="* Mettez juste le chiffre sans espaces autour.")
aidedefi4lb.config(font=("Liberation Sans", 8))
aidedefi4lb.pack()
defi4.pack_forget()
aidedefi4.pack_forget()

# Défi n°5 !

defi5 = LabelFrame(mainwindow, text="Défi n°5 !", padx=20, pady=20)
defi5.pack(fill="both", expand="yes")

def verif5():
   averif=entree5.get()
   if averif == "4":
      showinfo("Réponse au défi 5", "Bravo !!!")
      defi5.pack_forget()
      aidedefi5.pack_forget()
      defi6.pack()
      aidedefi6.pack()
   else:
      showinfo("Réponse au défi 5", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi5, text="Comment s'appelle*** la** distribution linux la plus ancienne* ")
textdefi1.pack()
textdefi2 = Label(defi5, text="Indice : 1. Red Hat | 2. Debian | 3. MCC Internim | 4.Slackware")
textdefi2.pack()
entree5 = Entry(defi5, textvariable=rep, width=30)
entree5.pack()
verifbut5=Button(defi5, text="Verifier", command=verif5)
verifbut5.pack()

aidedefi5 = LabelFrame(defi5, text="Aide", padx=20, pady=20)
aidedefi5.pack(fill="both", expand="yes")

aidedefi2lb = Label(aidedefi5, text="* Encore maintenue, bien sûr, pas celles abandonées.")
aidedefi2lb.config(font=("Liberation Sans", 8))
aidedefi1lb = Label(aidedefi5, text="** En 2020.")
aidedefi1lb.config(font=("Liberation Sans", 8))
aidedefi2lb.pack()
aidedefi3lb = Label(aidedefi5, text="*** Mettez juste le chiffre sans espaces autour.")
aidedefi3lb.config(font=("Liberation Sans", 8))
aidedefi3lb.pack()
aidedefi1lb.pack()

defi5.pack_forget()
aidedefi5.pack_forget()

# Défi n°6 !

defi6 = LabelFrame(mainwindow, text="Défi n°6 !", padx=20, pady=20)
defi6.pack(fill="both", expand="yes")

def verif6():
   averif=entree6.get()
   if averif == "BANANE":
      showinfo("Réponse au défi 6", "Bravo !!!")
      defi6.pack_forget()
      aidedefi6.pack_forget()
      defi7.pack()
      aidedefi7.pack()
   else:
      showinfo("Réponse au défi 6", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi6, text="Trouvez le mot* ! Écrivez le mot en majuscules.")
textdefi1.pack()
textdefi2 = Label(defi6, text="Indice : NANEAB")
textdefi2.pack()
entree6 = Entry(defi6, textvariable=rep, width=30)
entree6.pack()
verifbut6=Button(defi6, text="Verifier", command=verif6)
verifbut6.pack()

aidedefi6 = LabelFrame(defi6, text="Aide", padx=20, pady=20)
aidedefi6.pack(fill="both", expand="yes")

aidedefi6lb = Label(aidedefi6, text="* Pour trouver le mot, remettez les lettres dans l'ordre.")
aidedefi6lb.config(font=("Liberation Sans", 8))
aidedefi6lb.pack()
defi6.pack_forget()
aidedefi6.pack_forget()

# Défi n°7 !

defi7 = LabelFrame(mainwindow, text="Défi n°7 !", padx=20, pady=20)
defi7.pack(fill="both", expand="yes")

def verif7():
   averif=entree7.get()
   if averif == "multicolore":
      showinfo("Réponse au défi 7", "Bravo !!!")
      defi7.pack_forget()
      aidedefi7.pack_forget()
      defi8.pack()
      aidedefi8.pack()
   else:
      showinfo("Réponse au défi 7", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi7, text="Trouvez le mot* ! Écrivez tout en minuscules.")
textdefi1.pack()
textdefi2 = Label(defi7, text="Indice : 1. Je suis bleu | 2. Je suis rouge | 3. Je suis vert | 4. Et je comporte plein d'autres couleurs | 5. Je suis donc ... !")
textdefi2.pack()
entree7 = Entry(defi7, textvariable=rep, width=30)
entree7.pack()
verifbut7=Button(defi7, text="Verifier", command=verif7)
verifbut7.pack()

aidedefi7 = LabelFrame(defi7, text="Aide", padx=20, pady=20)
aidedefi7.pack(fill="both", expand="yes")

aidedefi7lb = Label(aidedefi7, text="* Un champ de fleurs toutes différentes l'est.")
aidedefi7lb.config(font=("Liberation Sans", 8))
aidedefi7lb.pack()
defi7.pack_forget()
aidedefi7.pack_forget()

# Défi n°8 !

defi8 = LabelFrame(mainwindow, text="Défi n°8 !", padx=20, pady=20)
defi8.pack(fill="both", expand="yes")

def verif8():
   averif=entree8.get()
   if averif == "Répondez !":
      showinfo("Réponse au défi 8", "Bravo !!!")
      defi8.pack_forget()
      aidedefi8.pack_forget()
      defi9.pack()
      aidedefi9.pack()
   else:
      showinfo("Réponse au défi 8", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi8, text="Quelle phrase cette instruction* va t'elle afficher. Respectez la casse et les espaces.")
textdefi1.pack()
textdefi2 = Label(defi8, text="Indice : print(\"Répondez !\")")
textdefi2.pack()
entree8 = Entry(defi8, textvariable=rep, width=30)
entree8.pack()
verifbut8=Button(defi8, text="Verifier", command=verif8)
verifbut8.pack()

aidedefi8 = LabelFrame(defi8, text="Aide", padx=20, pady=20)
aidedefi8.pack(fill="both", expand="yes")

aidedefi8lb = Label(aidedefi8, text="* C'est une ligne de python 3.")
aidedefi8lb.config(font=("Liberation Sans", 8))
aidedefi8lb.pack()
defi8.pack_forget()
aidedefi8.pack_forget()

# Défi n°9 !

defi9 = LabelFrame(mainwindow, text="Défi n°9 !", padx=20, pady=20)
defi9.pack(fill="both", expand="yes")

def verif9():
   averif=entree9.get()
   if averif == "balle rebondissante":
      showinfo("Réponse au défi 9", "Bravo !!!")
      defi9.pack_forget()
      aidedefi9.pack_forget()
      defi10.pack()
      aidedefi10.pack()
   else:
      showinfo("Réponse au défi 9", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi9, text="Que suis-je* ? Écrivez tout en minuscules.")
textdefi1.pack()
textdefi9 = Label(defi9, text="Indice : Quand on me lance contre le sol, je rebondis très haut, Et je suis très dur. Je suis en caoutchouc.")
textdefi9.pack()
entree9 = Entry(defi9, textvariable=rep, width=30)
entree9.pack()
verifbut9=Button(defi9, text="Verifier", command=verif9)
verifbut9.pack()

aidedefi9 = LabelFrame(defi9, text="Aide", padx=20, pady=20)
aidedefi9.pack(fill="both", expand="yes")

aidedefi9lb = Label(aidedefi9, text="* Quel objet ? La réponse comporte deux mots.")
aidedefi9lb.config(font=("Liberation Sans", 8))
aidedefi9lb.pack()
defi9.pack_forget()
aidedefi9.pack_forget()

# Défi n°10 !

defi10 = LabelFrame(mainwindow, text="Défi n°10 !", padx=20, pady=20)
defi10.pack(fill="both", expand="yes")

def verif10():
   averif=entree10.get()
   if averif == "diable":
      showinfo("Réponse au défi 10", "Bravo !!!")
      defi10.pack_forget()
      aidedefi10.pack_forget()
      defi11.pack()
      aidedefi11.pack()
   else:
      showinfo("Réponse au défi 10", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi10, text="Que suis-je* ? Écrivez tout en minuscules.")
textdefi1.pack()
textdefi10 = Label(defi10, text="Indice : Qui est ce qui est rouge, et qui a une fourche ?")
textdefi10.pack()
entree10 = Entry(defi10, textvariable=rep, width=30)
entree10.pack()
verifbut10=Button(defi10, text="Verifier", command=verif10)
verifbut10.pack()

aidedefi10 = LabelFrame(defi10, text="Aide", padx=20, pady=20)
aidedefi10.pack(fill="both", expand="yes")

aidedefi10lb = Label(aidedefi10, text="* Quel objet ? Je fais parti du logo de FreeBSD.")
aidedefi10lb.config(font=("Liberation Sans", 8))
aidedefi10lb.pack()
defi10.pack_forget()
aidedefi10.pack_forget()

# Défi n°11 !

defi11 = LabelFrame(mainwindow, text="Défi n°11 !", padx=20, pady=20)
defi11.pack(fill="both", expand="yes")

def verif11():
   averif=entree11.get()
   if averif == "1889":
      showinfo("Réponse au défi 11", "Bravo !!!")
      defi11.pack_forget()
      aidedefi11.pack_forget()
      defi12.pack()
      aidedefi12.pack()
   else:
      showinfo("Réponse au défi 11", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi11, text="Donnez l'année*.")
textdefi1.pack()
textdefi11 = Label(defi11, text="Indice : Quand la tour eiffel a-t-elle été finie ?")
textdefi11.pack()
entree11 = Entry(defi11, textvariable=rep, width=30)
entree11.pack()
verifbut11=Button(defi11, text="Verifier", command=verif11)
verifbut11.pack()

aidedefi11 = LabelFrame(defi11, text="Aide", padx=20, pady=20)
aidedefi11.pack(fill="both", expand="yes")

aidedefi11lb = Label(aidedefi11, text="* Le chiffre sans rien autour.")
aidedefi11lb.config(font=("Liberation Sans", 8))
aidedefi11lb.pack()
defi11.pack_forget()
aidedefi11.pack_forget()

# Défi n°12 !

defi12 = LabelFrame(mainwindow, text="Défi n°12 !", padx=20, pady=20)
defi12.pack(fill="both", expand="yes")

def verif12():
   averif=entree12.get()
   if averif == "MACHIN":
      showinfo("Réponse au défi 12", "Bravo !!!")
      defi12.pack_forget()
      aidedefi12.pack_forget()
      # !!! pack de la fin
      endw.pack()
      # defi13.pack()
      # aidedefi13.pack()
   else:
      showinfo("Réponse au défi 12", "C'est pas bon, réssayez")

rep = "MAGIQUE"
averif="MAGIQUE"
textdefi1 = Label(defi12, text="Retrouvez le mot* et écrivez le mot tout en majuscules")
textdefi1.pack()
textdefi12 = Label(defi12, text="Indice : IMHNAC")
textdefi12.pack()
entree12 = Entry(defi12, textvariable=rep, width=30)
entree12.pack()
verifbut12=Button(defi12, text="Verifier", command=verif12)
verifbut12.pack()

aidedefi12 = LabelFrame(defi12, text="Aide", padx=20, pady=20)
aidedefi12.pack(fill="both", expand="yes")

aidedefi12lb = Label(aidedefi12, text="* Remettez les lettres dans l'ordre.")
aidedefi12lb.config(font=("Liberation Sans", 8))
aidedefi12lb.pack()
defi12.pack_forget()
aidedefi12.pack_forget()

# Menu de fin

endw = LabelFrame(mainwindow, text="Bravo !", padx=20, pady=20)
endw.pack(fill="both", expand="yes")
messagefin = Label(endw, text="Bravo ! Vous avez résolu tout les défis !")
messagefin.pack()

verifbut12=Button(endw, text="Recommencer", command=rstart)
verifbut12.pack()
endw.pack_forget()

mainwindow.mainloop()
