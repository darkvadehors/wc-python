import tkinter as tk
from software_model.software import software_list
from tkinter.constants import BOTH, LEFT, YES, RIGHT

class Windows_interface:
    def __init__(self, master):
        self.master = master
        self.software_list = ""
        self.result = ""

        # get model_pattern
        self.model_pattern = software_list()

        # Model List
        list_model_name=[] # list for the left list
        list_software = [] # list for the Right List

        #  Mode noramel
        # for model in model_pattern:
        #     for idx, val in enumerate(model):
        #         list_model_name.append(val)

        # Mode Comprehension de liste pour la forme
        # Generate idx for first left list
        [list_model_name.append(val) for model in self.model_pattern for _ , val in enumerate(model)]
        list_model_name = tk.StringVar(value=list_model_name)

        # variables
        COLOR = "#E1E1E1"
        FONT1 = "Helvetica"

        # Windows Title
        self.master.title("Workstation Configurator")

        # winodws Dimension
        self.master.minsize(420,400)
        # windows.maxsize(300,720)

        # windows Left Ico
        # windows.iconbitmap("logo.ico")

        #  Color
        self.master.config(background=COLOR)

        #  ------------------- Row 0 -------------------

        self.row0_frame_top = tk.Frame(self.master,  padx=10, pady=10)
        self.row0_frame_top.grid(columnspan=2, sticky="ws")

        # Title
        self.row0_label_title1 = tk.Label(self.row0_frame_top, text="Bienvenue dans WC",font=(FONT1, 30 ),bg=COLOR, padx=10, pady=10)
        self.row0_label_title1.pack(fill=BOTH, expand=YES)


        #  ------------------- Row 1 -------------------

        #   .d8888b.           888               .d888 888
        #  d88P  Y88b          888              d88P"  888
        #  888    888          888              888    888
        #  888                 888      .d88b.  888888 888888
        #  888                 888     d8P  Y8b 888    888
        #  888    888          888     88888888 888    888
        #  Y88b  d88P d8b      888     Y8b.     888    Y88b.
        #   "Y8888P"  Y8P      88888888 "Y8888  888     "Y888

        self.row1_frame1 = tk.Frame(self.master, padx=10, pady=10)
        self.row1_frame_left = tk.LabelFrame(self.row1_frame1, text="Choix du modèle", padx=10, pady=10)

        # ******************** list ********************

        self.list_left = tk.Listbox(self.row1_frame_left, listvariable=list_model_name, height=5 )
        self.list_left.pack(fill=BOTH, expand=YES)
        self.list_left.bind('<<ListboxSelect>>', self.software_list_generator)

        self.row1_frame_left.grid( row=0 ,column=0,sticky="nw" )
        self.row1_frame1.grid(row=1, column=0,sticky="nw")


        #   .d8888b.           8888888b.  d8b          888      888
        #  d88P  Y88b          888   Y88b Y8P          888      888
        #  888    888          888    888              888      888
        #  888                 888   d88P 888  .d88b.  88888b.  888888
        #  888                 8888888P"  888 d88P"88b 888 "88b 888
        #  888    888          888 T88b   888 888  888 888  888 888
        #  Y88b  d88P d8b      888  T88b  888 Y88b 888 888  888 Y88b.
        #   "Y8888P"  Y8P      888   T88b 888  "Y88888 888  888  "Y888
        #                                          888
        #                                     Y8b d88P
        #                                      "Y88P"                                                                                      "Y88P"

        self.row1_frame2 = tk.LabelFrame(self.master, text="Liste des Logiciels", padx=10, pady=10)
        self.row1_frame_right = tk.Listbox(self.row1_frame2, borderwidth=0, highlightthickness=0, height=5)

        # ******************** list ********************

        self.row1_frame_right.grid( row=0 ,column=0 )
        self.row1_frame2.grid(row=1, column=1,sticky="news")

        self.row2_frame = tk.Frame(self.master, padx=10, pady=10,bg="red")

        bouton_quit = tk.Button(self.row2_frame, text="Quitter",  command=self.master.destroy).pack(side=LEFT)
        send_Button = tk.Button(self.row2_frame, text ="Hello", command=self.send_data(list_software)).pack(side=RIGHT)

        self.row2_frame.grid(row=2,column=0, columnspan=2)

        self.list_left.selection_set(0)
        self.software_list_generator(list_software)
        print("list_software",list_software)


    def software_list_generator(self,list_software):
        """Generate liste of Software in the right Frame

            ARGS: idxs for the curselection of the ligne in the left list

            RETURN: insert label in the Right Liste from the list_software
        """

        #  Vide la lsite
        list_software = []
        self.frame_delete(self.row1_frame_right)

        print("list_software",list_software)

        idxs = self.list_left.curselection()
        idxs=int(idxs[0])

        # parcours le tuple pour sortir la ligne du model
        for _ ,soft in self.model_pattern[idxs].items():
            # parcours le dictionnaire pour sortir les softwares
            for x, y in enumerate(soft[:][:]):
                # ajoute les software dans la liste
                list_software.append(y)

        for key, soft in enumerate(list_software):
            self.row1_frame_right_label = idxs + key
            self.row1_frame_right_label = tk.Label( self.row1_frame_right , text= soft,anchor="w"  )
            self.row1_frame_right_label.pack(fill=BOTH, expand=YES)

        print("list_software 81",list_software)
        return list_software

    def send_data(self,list_software):
        print("list_software 85", list_software)
        self.result = list_software
        self.master.destroy


    def frame_delete(self,frame_to_delete):
        """Delete frame before insert software list

            ARGS: Frame to delete

            RETURNS: None
        """
        for widget in frame_to_delete.winfo_children():
            widget.destroy()


def main():
    root = tk.Tk()
    app = Windows_interface(root)
    root.mainloop()


if __name__ == "__main__":
    print(main())











    # ws = Tk()
    # ws.title("PythonGuides")
    # ws.geometry('400x300')
    # ws['bg'] = '#ffbf00'

    # def printValue():
    #     pname = player_name.get()
    #     pname1 = player_name1.get()
    #     Label(ws, text=f'{pname} {pname1}, Registered!', pady=20, bg='#ffbf00').pack()


    # player_name1 = Entry(ws)
    # player_name1.pack(pady=30)
    # player_name = Entry(ws)
    # player_name.pack(pady=30)


    # Button(
    #     ws,
    #     text="Register Player",
    #     padx=10,
    #     pady=5,
    #     command=printValue
    #     ).pack()




    # ws.mainloop()






        # label = Label(windows_def, text="WorkStation Configurator")
        # label.pack()


        # software_liste = ["Firefox","chrome"]



        # row_1 = PanedWindow(windows_def, orient=VERTICAL)

        # # frame 1
        # row_1_frame1 = Frame(row_1, borderwidth=2 , bd=1, relief=SUNKEN)
        # row_1_frame1.pack(side=LEFT, padx=30, pady=30)

        # # frame 2
        # row_1_frame2 = Frame(row_1, borderwidth=2, bd=1, relief=SUNKEN)
        # row_1_frame2.pack(side=RIGHT, padx=30, pady=30)

        # row_1.grid(side=TOP,  fill=BOTH, pady=2, padx=2)


        # # Ajout de labels
        # label_left = Label(row_1, text="tutu1")
        # label_left.pack(padx=10, pady=10)

        # label_right = Label(row_1, text="tutu2")
        # label_right.pack(padx=10, pady=10)






        # Button(windows_def, text ='Annuler').pack(side=LEFT, padx=25, pady=5)
        # Button(windows_def, text ='Démarrer').pack(side=RIGHT, padx=25, pady=5)







        # bottom = Label(m2, text="bottom pane")
        # m2.add(bottom)

        # row_1 = PanedWindow(windows_def, orient=VERTICAL)
        # row_1.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)

        # windows_def['bg']='white'


        # row_2.add(Label(p, text='Volet 1', background='blue', anchor=CENTER))


        # row_2.add(Label(p, text='Volet 2', background='white', anchor=CENTER) )

        # # row_1
        # row_1 = Frame(windows_def, borderwidth=2, relief=GROOVE)
        # row_1.pack(side=LEFT, padx=2, pady=2)

        # # column_left
        # column_left = Frame(row_1, borderwidth=2, relief=GROOVE)
        # column_left.pack(side=LEFT, padx=2, pady=2)

        # # column_right
        # column_right = Frame(row_1, borderwidth=2, relief=GROOVE)
        # column_right.pack(side=RIGHT , padx=2, pady=2)



        # # row_2
        # row_2 = Frame(windows_def, borderwidth=2, relief=GROOVE)
        # row_2.pack(side=BOTTOM , padx=2, pady=2, after=row_1)

        # p.add(Label(p, text='Volet 3', background='red', anchor=CENTER) )

        # bouton = Button(row_2, text="Quitter", command=windows_def.quit)
        # bouton["fg"] = "red"
        # bouton.pack()

        # # frame 3 dans frame 2
        # #Frame3 = Frame(column_right, bg="white", borderwidth=2, relief=GROOVE)
        # #Frame3.pack(side=RIGHT, padx=5, pady=5)

        # # Ajout de labels
        # Label(column_left, text="Choisir un modèle:").pack(padx=10, pady=5)
        # Label(column_right, text="Liste des logiciels à installer").pack(padx=10, pady=10)
        # #Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)




    # liste
        # liste = Listbox(column_left)
        # for idx,software in enumerate(software_liste):
        #     liste.insert(idx, software)
        # liste.pack()
