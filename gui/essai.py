#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mbx

from .tarif import TarifWidget as tarif

class ProtoGuiApp:
    def __init__(self, master=None):
        # build ui
        self.topWin = tk.Tk() if master is None else tk.Toplevel(master)
        self.topWin.configure(height=800, width=1500)
        self.topWin.resizable(True, True)
        self.topWin.title("Opération MCA")

        self.style = ttk.Style(self.topWin)
        self.topWin.tk.call("source", "forest-light.tcl")
        self.topWin.tk.call("source", "forest-dark.tcl")
        self.style.theme_use("forest-light")

        self.main = tk.Menu(self.topWin, name="main")
        self.file = tk.Menu(self.main, tearoff=False)
        self.main.add(
            tk.CASCADE,
            menu=self.file,
            compound="top",
            hidemargin=True,
            label='Fichiers')
        self.Recent = tk.Menu(self.file, tearoff=False)
        self.file.add(
            tk.CASCADE,
            menu=self.Recent,
            hidemargin=True,
            label='Fichiers récents')
        self.Recent.add("command", label='File 1')
        self.Recent.add("command", label='File 2')
        self.Recent.add("command", label='File 3')
        self.file.add("command", label='Ouvrir')
        self.file.add("command", label='Fermer')
        self.file.add("command", label='Nouveau')
        self.file.add("separator")
        self.file.add("command", label='Enregistrer')
        self.file.add("command", label='Enregistrer sous')
        self.file.add("separator")
        self.file.add(
            "command",
            command=self.on_save_tarif_clicked,
            label='Enregistrer Tarif')
        self.edit = tk.Menu(self.main, tearoff=False)
        self.main.add(tk.CASCADE, menu=self.edit, label='Edition')
        self.help = tk.Menu(self.main, tearoff=False)
        self.main.add(tk.CASCADE, menu=self.help, label='Aide')
        self.help.add("command", label='Aide')
        self.help.add("command", label='A propos')
        self.topWin.configure(menu=self.main)

        self.frame = ttk.Frame(self.topWin, name="frame")
        self.frame.configure(height=200, width=200)
        self.operation = ttk.Labelframe(self.frame, name="operation")
        self.operation.configure(height=200, text='Opération', width=200)
        self.codeLabel = ttk.Label(self.operation, name="codelabel")
        self.codeLabel.configure(text='Code opération')
        self.codeLabel.grid(column=0, padx=2, pady=2, row=0, sticky="w")
        self.codeEntry = ttk.Entry(self.operation, name="codeentry")
        self.v_code = tk.StringVar()
        self.codeEntry.configure(textvariable=self.v_code)
        self.codeEntry.grid(column=1, padx=2, pady=2, row=0, sticky="w")
        self.manifLabel = ttk.Label(self.operation, name="maniflabel")
        self.manifLabel.configure(text='Manifestation')
        self.manifLabel.grid(column=0, padx=2, pady=2, row=1, sticky="w")
        self.manifEntry = ttk.Entry(self.operation, name="manifentry")
        self.v_manif = tk.StringVar()
        self.manifEntry.configure(textvariable=self.v_manif)
        self.manifEntry.grid(column=1, padx=2, pady=2, row=1, sticky="w")
        self.dateLabel = ttk.Label(self.operation, name="datelabel")
        self.dateLabel.configure(text='date')
        self.dateLabel.grid(column=0, padx=2, pady=2, row=2, sticky="w")
        self.dateEntry = ttk.Entry(self.operation, name="dateentry")
        self.v_date = tk.StringVar()
        self.dateEntry.configure(textvariable=self.v_date)
        self.dateEntry.grid(column=1, padx=2, pady=2, row=2, sticky="w")
        Separator_1 = ttk.Separator(self.operation)
        Separator_1.configure(orient="horizontal")
        Separator_1.grid(column=0, columnspan=2, pady=7, row=3, sticky="ew")
        self.mailLabel = ttk.Label(self.operation, name="maillabel")
        self.mailLabel.configure(text='Mail Facturation')
        self.mailLabel.grid(column=0, padx=2, pady="2 5", row=4, sticky="w")
        self.mailEntry = ttk.Entry(self.operation, name="mailentry")
        self.v_mailFacturation = tk.StringVar()
        self.mailEntry.configure(textvariable=self.v_mailFacturation)
        self.mailEntry.grid(column=1, padx=2, pady="2 5", row=4, sticky="w")
        Separator_2 = ttk.Separator(self.operation)
        Separator_2.configure(orient="vertical")
        Separator_2.grid(
            column=2,
            padx=2,
            pady="0 2",
            row=0,
            rowspan=5,
            sticky="ns")
        Label_2 = ttk.Label(self.operation)
        Label_2.configure(text='Client')
        Label_2.grid(column=3, padx=2, pady=2, row=0, sticky="w")
        self.customerEntry = ttk.Entry(self.operation, name="customerentry")
        self.v_customer = tk.StringVar()
        self.customerEntry.configure(textvariable=self.v_customer)
        self.customerEntry.grid(
            column=4,
            columnspan=3,
            padx=2,
            pady=2,
            row=0,
            sticky="ew")
        self.address1Label = ttk.Label(self.operation, name="address1label")
        self.adress1 = tk.StringVar(value='Adresse')
        self.address1Label.configure(text='Adresse', textvariable=self.adress1)
        self.address1Label.grid(column=3, padx=2, pady=2, row=1, sticky="w")
        self.address1Entry = ttk.Entry(self.operation, name="address1entry")
        self.v_address1 = tk.StringVar()
        self.address1Entry.configure(textvariable=self.v_address1)
        self.address1Entry.grid(
            column=4,
            columnspan=3,
            padx=2,
            pady=2,
            row=1,
            sticky="ew")
        self.address2Label = ttk.Label(self.operation, name="address2label")
        self.address2Label.configure(text='Adr. suite')
        self.address2Label.grid(column=3, padx=2, pady=2, row=2, sticky="w")
        self.address2Entry = ttk.Entry(self.operation, name="address2entry")
        self.v_address2 = tk.StringVar()
        self.address2Entry.configure(textvariable=self.v_address2)
        self.address2Entry.grid(
            column=4,
            columnspan=3,
            padx=2,
            pady=2,
            row=2,
            sticky="ew")
        self.zipLabel = ttk.Label(self.operation, name="ziplabel")
        self.zipLabel.configure(text='ZIP code')
        self.zipLabel.grid(column=3, padx=2, pady=2, row=3, sticky="w")
        self.zipEntry = ttk.Entry(self.operation, name="zipentry")
        self.v_zip = tk.StringVar()
        self.zipEntry.configure(textvariable=self.v_zip)
        self.zipEntry.grid(column=4, padx=2, pady=2, row=3, sticky="w")
        self.cityLabel = ttk.Label(self.operation, name="citylabel")
        self.cityLabel.configure(text='ville')
        self.cityLabel.grid(column=5, padx=2, pady=2, row=3, sticky="w")
        self.cityEntry = ttk.Entry(self.operation, name="cityentry")
        self.v_city = tk.StringVar()
        self.cityEntry.configure(textvariable=self.v_city)
        self.cityEntry.grid(column=6, padx=2, pady=2, row=3, sticky="e")
        self.countryLabel = ttk.Label(self.operation, name="countrylabel")
        self.countryLabel.configure(text='Pays')
        self.countryLabel.grid(column=3, padx=2, pady="2 5", row=4, sticky="w")
        self.countryEntry = ttk.Entry(self.operation, name="countryentry")
        self.v_country = tk.StringVar()
        self.countryEntry.configure(textvariable=self.v_country)
        self.countryEntry.grid(column=4, padx=2, pady="2 5", row=4, sticky="w")
        self.phoneLabel = ttk.Label(self.operation, name="phonelabel")
        self.phoneLabel.configure(text='Téléphone')
        self.phoneLabel.grid(column=5, padx=2, pady="2 5", row=4, sticky="w")
        self.phoneEntry = ttk.Entry(self.operation, name="phoneentry")
        self.v_phone = tk.StringVar()
        self.phoneEntry.configure(textvariable=self.v_phone)
        self.phoneEntry.grid(column=6, padx=2, pady="2 5", row=4, sticky="ew")
        Separator_3 = ttk.Separator(self.operation)
        Separator_3.configure(orient="vertical")
        Separator_3.grid(
            column=7,
            padx=2,
            pady="0 2",
            row=0,
            rowspan=5,
            sticky="ns")
        self.generateButton = ttk.Button(self.operation, name="generatebutton", command=self.generate)
        self.v_language = tk.StringVar(value='french')
        self.generateButton.configure(text='Générer la Facture')
        self.generateButton.grid(column=8, padx=2, pady=2, row=0, sticky="ew")
        self.french = ttk.Radiobutton(self.operation, name="french")
        self.french.configure(
            text='Français',
            value="french",
            variable=self.v_language)
        self.french.grid(column=8, padx=2, pady=2, row=1, sticky="ew")
        self.english = ttk.Radiobutton(self.operation, name="english")
        self.english.configure(
            state="normal",
            text='English',
            value="english",
            variable=self.v_language)
        self.english.grid(column=8, padx=2, pady="2 5", row=2, sticky="ew")
        self.operation.pack(
            anchor="n",
            expand=False,
            fill="x",
            padx=10,
            pady="10 5",
            side="top")
        self.details = ttk.Labelframe(self.frame, name="details")
        self.details.configure(
            height=200,
            labelanchor="nw",
            text='Détails',
            width=400)
        self.book = ttk.Notebook(self.details, name="book")
        self.tarif = tarif(self.book)
        self.tarif.grid(column=0, row=0, sticky="nsew")
        self.book.add(self.tarif, state="normal", sticky="nsew", text='Tarif')
        Treeview_1 = ttk.Treeview(self.book)
        Treeview_1.configure(selectmode="extended")
        Treeview_1.pack(side="top")
        self.book.add(
            Treeview_1,
            state="normal",
            sticky="nsew",
            text='Données Client')
        Treeview_2 = ttk.Treeview(self.book)
        Treeview_2.configure(selectmode="extended")
        Treeview_2.pack(side="top")
        self.book.add(
            Treeview_2,
            state="normal",
            sticky="nsew",
            text='Données internes')
        self.book.pack(expand=True, fill="both", padx=5, pady=5, side="top")
        self.details.pack(
            expand=True,
            fill="both",
            padx=10,
            pady="0 5",
            side="top")
        self.Status = ttk.Labelframe(self.frame, name="status")
        self.Status.configure(height=50, text='Status', width=200)
        self.mode_switch = ttk.Checkbutton(self.Status, name="mode_switch")
        self.mode_switch.configure(style="Switch", text='Dark mode')
        self.mode_switch.pack(padx=5, pady=5, side="right")
        self.mode_switch.configure(command=self.toggle_mode)
        self.Status.pack(
            expand=False,
            fill="x",
            padx=10,
            pady="0 10",
            side="top")
        self.frame.pack(expand=True, fill="both", side="top")

        # Main widget
        self.mainwindow = self.topWin

    def run(self):
        self.mainwindow.mainloop()

    def toggle_mode(self):
        if self.mode_switch.instate(["selected"]):
            self.style.theme_use("forest-dark")
        else:
            self.style.theme_use("forest-light")

    def generate(self):
        mbx.showinfo(title='Création de facture',message=f"Création de facture pour l'affaire {self.v_code.get()} en {self.v_language.get()}")

    def on_save_tarif_clicked(self):
        print(f'save tarif: {self.tarif.poste}')

if __name__ == "__main__":
    app = ProtoGuiApp()
    app.run()
