from tkinter import *
from tkinter.messagebox import *

mainwindow = Tk()
mainwindow.title("Défi !")
# mainwindow.iconbitmap("data/images/windowico/main.ico")

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
textdefi1 = Label(defi7, text="Trouvez le mot* !")
textdefi1.pack()
textdefi2 = Label(defi7, text="Indice : 1. Je suis bleu | 2. Je suis rouge | 3. Je suis vert | 4. Et je comporte plein d'autres couleurs | 5. Je suis donc ... !")
textdefi2.pack()
entree7 = Entry(defi7, textvariable=rep, width=30)
entree7.pack()
verifbut7=Button(defi7, text="Verifier", command=verif7)
verifbut7.pack()

aidedefi7 = LabelFrame(defi7, text="Aide", padx=20, pady=20)
aidedefi7.pack(fill="both", expand="yes")

aidedefi7lb = Label(aidedefi7, text="* Écrivez tout en minuscules.")
aidedefi7lb.config(font=("Liberation Sans", 8))
aidedefi7lb.pack()
defi7.pack_forget()
aidedefi7.pack_forget()


mainwindow.mainloop()
