from curses import window
from tkinter import *
from tkinter import messagebox
import requests
from requests import *
import json
import accessbdd
import badge
import reco
import mb

#TODO enlever le nb de connexion car peut être demandé en exam


#palette de couleurs
#à mettre plus dans le fichier de config.

#variables

palette = {
    "mb" : "#000032", #main_background
    "sb" : "#50c5b7", #secondary_background - color of buttons and other objects that go over the background
    "mf" : "#FFFFFF", #main_foreground
    "sf" : "#f0f465"
}
tentative = 3

def create_connection_view():
    """Shows the view for the nurse to input her credentials"""
    #création de la fenêtre principale
    window = Tk()

    #personnaliser fenêtre :
    window.title("Connexion")
    window.geometry('318x565')
    window.minsize(318,565)#TODO put minsize in config file
    #window.config(background=palette['mb'])

    #Création frame
    frame = Frame(window)
    buttons_frame = Frame(frame)

    #composants :
    label_title = Label(frame,text="Hôpital pi", font=("Courrier",20))
    label_title.pack()

    label_username = Label(frame,text="Identifiant", font=("Courrier",15))
    label_username.pack()
    
    entry_username = Entry(frame,width=20, highlightthickness=0,  font=('Courrier', 15))
    entry_username.pack()

    label_password = Label(frame,text="Mot de passe", font=("Courrier",15))
    label_password.pack()

    entry_password = Entry(frame,font=('Courrier', 15),show="*",)
    entry_password.pack()

    button_submit = Button(buttons_frame, text="Valider", font=('Courrier', 15), command=lambda:submit_credentials(entry_username.get(), entry_password.get()))
    button_submit.grid(column=0, row=0, padx=5, pady=10)
    #button_submit = Button(frame, text="Valider", font=('Courrier', 15), command=submit_credentials)
    #button_submit = Button(frame, text="Valider", font=('Courrier', 15), command=lambda:submit_credentials(tentative))
    #button_submit.pack(pady=5, padx=5)

    #button_quit = Button(frame, text="Quitter", font=('Courrier', 15), command=window.quit)
    button_quit = Button(buttons_frame, text="Quitter", font=('Courrier', 15), command=window.quit)
    #button_quit.pack(pady=5, padx=5)
    button_quit.grid(column = 1, row = 0, padx=5, pady=10)
    #ajout de la frame :
    buttons_frame.pack()
    frame.pack(expand=YES)

    #affichage de la fenêtre :
    window.mainloop() 

count = 0
def submit_credentials(login,pwd):
    global tentative
    
    if (tentative > 0):
        #messagebox.showwarning("Avertissement","Erreur dans la saisie du mot de passe {0}/3 tentative(s) restante(s)".format(tentative))
        #messagebox.showwarning("Avertissement","{0},{1}".format(login,pwd))
        if login is None or pwd is None or login=="" or pwd=="" :
            mb.show_wrong()
            messagebox.showwarning(U"Avertissement",U"Veuillez remplir tous les champs")
            mb.clear()
           
        else:
            data = accessWeb(login, pwd)
            if data.get('status')=='false' or data.get('status')=='False':
                mb.show_wrong()
                tentative -= 1
                accessbdd.insertLog(login,1,"fail")
                messagebox.showwarning(U"Avertissement",U"Identifiant ou mot de passe erroné")
                mb.clear()
                
            else :
                mb.show_right()
                messagebox.showinfo(U"Scannez votre badge",U"Appuyez sur le bouton 'ok' puis scannez votre badge.")
                mb.clear()
                badge_conn = badge.check_badge_webservice(login)
                if badge_conn[0] == False:
                    mb.show_wrong()
                    accessbdd.insertLog(login, 2, badge_conn[1])
                    messagebox.showwarning(U"Avertissement",U"Carte invalide veuillez recommencer")
                    mb.clear()
                else:
                    mb.show_right()
                    messagebox.showinfo(U"reconnaissance faciale",U"Appuyez sur le bouton 'ok' puis regarder la camera.")
                    mb.clear()
                    reco_conn = reco.face_reco(login)
                    if reco_conn[0] == False:
                        mb.show_wrong()
                        accessbdd.insertLog(login, 3, reco_conn[1])
                        messagebox.showwarning(U"Avertissement",U"echec de la reconnaisance veuillez recommencer")
                        mb.clear()
                    else:
                        mb.show_right()
                        accessbdd.insertLog(login, 4, 'coffre ouvert')
                        messagebox.showinfo(U"coffre ouvert",U"Appuyez sur le bouton 'ok' pour fermer cette page.")
                        mb.clear()
                        

    else :
        messagebox.showwarning(U"Avertissement",U"Le compte a été bloqué".format(tentative))
        tentative = 0
        mb.clear()

# def getValues(login, pwd):
#     values = []
#     values.append(login)
#     values.append(pwd)

#sudo pkill python

def accessWeb(username, password):
    url = requests.get('https://btssio-carcouet.fr/ppe4/public/connect2/{0}/{1}/infirmiere'.format(str(username), str(password)))
    text = url.text
    data = json.loads(text)
    #print(data['nom'])
    return data 





#https://docs.python.org/2/library/sqlite3.html
#id INTEGER PRIMARY KEY, 
# date_connexion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
# id_infirmiere INTEGER NOT NULL, 
# etape INTEGER NOT NULL, 
# message TEXT, 
# divers TEXT




if __name__ == "__main__" :
    create_connection_view()


#opencv