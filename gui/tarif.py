#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser as cch  # askcolor


class TarifWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        Label_1 = ttk.Label(self)
        Label_1.configure(text='Poste')
        Label_1.grid(column=0, padx=2, pady=2, row=1, sticky="w")
        Label_3 = ttk.Label(self)
        Label_3.configure(text='Information Client')
        Label_3.grid(column=3, columnspan=6, padx=2, pady=2, row=0)
        Label_4 = ttk.Label(self)
        Label_4.configure(text='Information interne')
        Label_4.grid(column=10, columnspan=6, padx=2, pady=2, row=0)
        Label_5 = ttk.Label(self)
        Label_5.configure(text='Jour', width=7)
        Label_5.grid(column=3, padx=2, pady=2, row=1)
        Label_8 = ttk.Label(self)
        Label_8.configure(text='1/2 Jour', width=7)
        Label_8.grid(column=4, padx=2, pady=2, row=1)
        Label_9 = ttk.Label(self)
        Label_9.configure(text='Soirée', width=7)
        Label_9.grid(column=5, padx=2, pady=2, row=1)
        Label_10 = ttk.Label(self)
        Label_10.configure(text='H.sup J', width=7)
        Label_10.grid(column=6, padx=2, pady=2, row=1)
        Label_11 = ttk.Label(self)
        Label_11.configure(text='H.sup N', width=7)
        Label_11.grid(column=7, padx=2, pady=2, row=1)
        Label_12 = ttk.Label(self)
        Label_12.configure(text='Repas', width=7)
        Label_12.grid(column=8, padx=2, pady=2, row=1)
        Label_13 = ttk.Label(self)
        Label_13.configure(text='Jour', width=7)
        Label_13.grid(column=10, padx=2, pady=2, row=1, sticky="w")
        Label_14 = ttk.Label(self)
        Label_14.configure(text='1/2 Jour', width=7)
        Label_14.grid(column=11, padx=2, pady=2, row=1, sticky="w")
        Label_15 = ttk.Label(self)
        Label_15.configure(text='Soirée', width=7)
        Label_15.grid(column=12, padx=2, pady=2, row=1, sticky="w")
        Label_16 = ttk.Label(self)
        Label_16.configure(text='H.sup J', width=7)
        Label_16.grid(column=13, padx=2, pady=2, row=1, sticky="w")
        Label_17 = ttk.Label(self)
        Label_17.configure(text='H.sup N', width=7)
        Label_17.grid(column=14, padx=2, pady=2, row=1, sticky="w")
        Label_18 = ttk.Label(self)
        Label_18.configure(text='Repas', width=7)
        Label_18.grid(column=15, padx=2, pady=2, row=1, sticky="w")
        Separator_4 = ttk.Separator(self)
        Separator_4.configure(orient="vertical")
        Separator_4.grid(column=2, padx=2, row=0, rowspan=9, sticky="ns")
        Separator_5 = ttk.Separator(self)
        Separator_5.configure(orient="vertical")
        Separator_5.grid(column=9, padx=2, row=0, rowspan=9, sticky="ns")
        Separator_6 = ttk.Separator(self)
        Separator_6.configure(orient="vertical")
        Separator_6.grid(column=16, padx=2, row=0, rowspan=9, sticky="ns")
        Separator_7 = ttk.Separator(self)
        Separator_7.configure(orient="horizontal")
        Separator_7.grid(column=0, columnspan=17, row=2, sticky="ew")
        self.poste= []
        for i in range(0,6):
            self.poste.append(self.add_tarif(i+3))
        # temporary init, should provide a save and restore config
        self.poste[0]['en_poste'].insert('0',"Hôtesse")
        self.poste[1]['en_poste'].insert('0',"Responsable")
        self.poste[5]['en_poste'].insert('0',"Frais, Fees, etc")
        self.poste[0]['btn_color'].configure(background="#FFC0FF")
        self.poste[1]['btn_color'].configure(background="#FFFFC0")
        self.poste[5]['btn_color'].configure(background="#C0FFFF")

    def on_color_btn_click(self,e):
        current_color = e.widget["background"]
        _, color = cch.askcolor(current_color,title="Choisir la couleur d'affichage pour ce poste")
        if color:
            e.widget.configure(background = color,state="normal")

    def add_tarif(self,grid_row):
        tarif = {}
        tarif['en_poste'] = ttk.Entry(self)
        tarif['en_poste'].configure(width=15)
        tarif['en_poste'].grid(column=0, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['btn_color'] = tk.Button(self)
        tarif['btn_color'].configure(background="#B0B0B0",state="normal",borderwidth=0,relief="flat")
        tarif['btn_color'].grid(column=1, padx=2, pady=2, row=grid_row)
        tarif['btn_color'].bind("<Button-1>", self.on_color_btn_click)

        tarif['en_journee_cl'] = ttk.Entry(self)
        tarif['en_journee_cl'].configure(width=7)
        tarif['en_journee_cl'].grid(column=3, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_demi_cl'] = ttk.Entry(self)
        tarif['en_demi_cl'].configure(width=7)
        tarif['en_demi_cl'].grid(column=4, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_soiree_cl'] = ttk.Entry(self)
        tarif['en_soiree_cl'].configure(width=7)
        tarif['en_soiree_cl'].grid(column=5, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_hsupj_cl'] = ttk.Entry(self)
        tarif['en_hsupj_cl'].configure(width=7)
        tarif['en_hsupj_cl'].grid(column=6, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_hsupn_cl'] = ttk.Entry(self)
        tarif['en_hsupn_cl'].configure(width=7)
        tarif['en_hsupn_cl'].grid(column=7, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_repas_cl'] = ttk.Entry(self)
        tarif['en_repas_cl'].configure(width=7)
        tarif['en_repas_cl'].grid(column=8, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_journee_in'] = ttk.Entry(self)
        tarif['en_journee_in'].configure(width=7)
        tarif['en_journee_in'].grid(column=10, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_demi_in'] = ttk.Entry(self)
        tarif['en_demi_in'].configure(width=7)
        tarif['en_demi_in'].grid(column=11, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_soiree_in'] = ttk.Entry(self)
        tarif['en_soiree_in'].configure(width=7)
        tarif['en_soiree_in'].grid(column=12, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_hsupj_in'] = ttk.Entry(self)
        tarif['en_hsupj_in'].configure(width=7)
        tarif['en_hsupj_in'].grid(column=13, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_hsupn_in'] = ttk.Entry(self)
        tarif['en_hsupn_in'].configure(width=7)
        tarif['en_hsupn_in'].grid(column=14, padx=2, pady=2, row=grid_row, sticky="w")

        tarif['en_repas_in'] = ttk.Entry(self)
        tarif['en_repas_in'].configure(width=7)
        tarif['en_repas_in'].grid(column=15, padx=2, pady=2, row=grid_row, sticky="w")

        return tarif


if __name__ == "__main__":
    root = tk.Tk()
    widget = TarifWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
