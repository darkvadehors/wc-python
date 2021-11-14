import tkinter as tk
import logging
from app.software_model.software import model_pattern
from tkinter.constants import BOTH, BOTTOM, YES

class Windows_interface:
    """Make windows selection

        ARGS:
            None

        Return:
            List of software to install
    """

    def __init__(self):
        self.ui_windows = tk.Tk()
        # get model_pattern
        self.model_pattern = model_pattern()
        self.result_list_to_return = []


        # Model List
        list_left_model_name=[] # list for the left list
        self.list_right_software_name = [] # list for the Right List

        #  Mode noramel
        # for model in model_pattern:
        #     for idx, val in enumerate(model):
        #         list_left_model_name.append(val)

        # Mode Comprehension de liste pour la forme
        # Generate idx for first left list
        [list_left_model_name.append(val)
         for model in self.model_pattern
         for _ , val in enumerate(model)]

        list_left_model_name = tk.StringVar(value=list_left_model_name)

        # variables
        COLOR = "#E1E1E1"
        FONT1 = "Helvetica"

        # Windows Title
        self.ui_windows.title("Workstation Configurator")

        # winodws Dimension
        self.ui_windows.minsize(420,400)
        # windows.maxsize(300,720)

        # windows Left Ico
        # windows.iconbitmap("logo.ico")

        #  Color
        self.ui_windows.config(background=COLOR)

        #  ------------------- Row 0 -------------------

        row0 = tk.Frame(self.ui_windows,  padx=10, pady=10)
        # row0.grid(columnspan=2, sticky="ws")
        row0.pack(fill=BOTH, expand=YES)

        # Title
        row0_label_title1 = tk.Label(row0,
                                     text="Bienvenue dans le WC",
                                     font=(FONT1, 30 ),
                                     bg=COLOR,
                                     padx=10,
                                     pady=10)

        row0_label_title1.pack(fill=BOTH, expand=YES)

        #  ------------------- Row 1 -------------------

        row1 = tk.Frame(self.ui_windows,  padx=10, pady=10)
        # row1.grid(columnspan=2)
        row1.pack(fill=BOTH, expand=YES)

        self.row1_frame1 = tk.Frame(row1, padx=10, pady=10)
        row1_frame_left = tk.LabelFrame(self.row1_frame1,
                                        text="Choix du modèle",
                                        padx=10,
                                        pady=10)

        # ******************** list ********************

        self.list_left = tk.Listbox(row1_frame_left,
                                    listvariable=list_left_model_name,
                                    height=5 )
        self.list_left.pack(fill=BOTH, expand=YES)
        self.list_left.bind('<<ListboxSelect>>',
                            self.software_right_list_generator)

        row1_frame_left.grid( row=0 ,column=0,sticky="nw" )
        self.row1_frame1.grid(row=1, column=0,sticky="nw")


        row1_frame2 = tk.LabelFrame(row1, text="Liste des Logiciels",
                                    padx=10,
                                    pady=10)
        self.row1_frame_right = tk.Listbox(row1_frame2,
                                           borderwidth=0,
                                           highlightthickness=0,
                                           height=5)

        # ******************** list ********************

        self.row1_frame_right.grid( row=0 ,column=0 )
        row1_frame2.grid(row=1, column=1,sticky="news")


        row2 = tk.Frame(self.ui_windows, padx=10, pady=10,bg="red")

        row_bottom = tk.Frame(row2)
        row_bottom.pack(side=BOTTOM)
        bouton_quit = tk.Button(row2,
                                text="Quitter",
                                anchor="se",
                                command=self.close_windows)
        bouton_quit.pack(side=BOTTOM)
        send_Button = tk.Button(row2,
                                text ="Installer",
                                anchor="sw",
                                command=self.send_data)
        send_Button.pack(side=BOTTOM)

        # row2.grid(row=3, columnspan=2)
        row2.pack(fill=BOTH, expand=YES)

        self.list_left.selection_set(0)
        self.result_list_to_return = self.software_right_list_generator()
        # self.software_right_list_generator()
        logging.info(self.result_list_to_return)
        #return self.list_right_software_name


        self.ui_windows.mainloop()

    def software_right_list_generator(self, *args):
        """Generate liste of Software in the right Frame

            ARGS: idxs for the curselection of the ligne in the left list

            RETURN: insert label in the Right Liste
                from the list_right_software_name
        """
        logging.info("Enter in generator")
        #  Vide la lsite
        list_right_software_name = []
        self.frame_delete(self.row1_frame_right)

        # model => designer
        model = self.list_left.get(self.list_left.curselection())
        logging.info("Model in gerenator : " + model)

        # insrt in list new software
        for idx_tuple,dict_ligne in enumerate(self.model_pattern):
            for x in self.model_pattern[idx_tuple].items():
                if x[0]== model:
                    list_right_software_name = dict_ligne[model]

        for key, soft in enumerate(list_right_software_name):
            row1_frame_right_label = key
            row1_frame_right_label = tk.Label( self.row1_frame_right ,
                                              text= soft,
                                              anchor="w"  )

            row1_frame_right_label.pack(fill=BOTH, expand=YES)

        self.list_right_software_name = list_right_software_name
        return list_right_software_name

    def send_data(self):
        """Update result_list_to_return for wc.py

        Returns:
            str: string contains software dictionnary
        """

        self.result_list_to_return = self.list_right_software_name
        self.ui_windows.destroy()
        return self.result_list_to_return

    def frame_delete(self,frame_to_delete):
        """Delete frame before insert software list

            ARGS: Frame to delete

            RETURNS: None
        """
        for widget in frame_to_delete.winfo_children():
            widget.destroy()

    def close_windows(self):
        """Close windows and empty software list

        Returns:
            None
        """
        self.result_list_to_return = []
        self.ui_windows.destroy()
        return self.result_list_to_return


if __name__ == "__main__":
    pass