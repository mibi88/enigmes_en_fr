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
textdefi1 = Label(defi1, text="Devinez le MDP* !")
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

mainwindow.mainloop()
