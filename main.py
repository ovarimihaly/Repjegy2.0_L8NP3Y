import tkinter as tk
from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, legitarsasag, kiindulas, celallomas, indulas, idotartam, ar, tipus):
        self.jaratszam = jaratszam
        self.legitarsasag = legitarsasag
        self.kiindulas = kiindulas
        self.celallomas = celallomas
        self.indulas = indulas
        self.idotartam = idotartam
        self.ar = ar
        self.tipus = tipus

    @abstractmethod
    def get_adatok(self):
        pass

# 2. Lépés: Alosztályok definálása
class BelfoldiJarat(Jarat):
    def get_adatok(self):
        return [
            self.jaratszam, self.legitarsasag, self.kiindulas,
            self.celallomas, self.indulas, self.idotartam, self.ar, self.tipus
        ]

class NemzetkoziJarat(Jarat):
    def get_adatok(self):
        return [
            self.jaratszam, self.legitarsasag, self.kiindulas,
            self.celallomas, self.indulas, self.idotartam, self.ar, self.tipus
        ]

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def add_jarat(self, jarat):
        self.jaratok.append(jarat)

class Foglalas:
    def __init__(self, vezeteknev, keresztnev, jarat):
        self.vezeteknev = vezeteknev
        self.keresztnev = keresztnev
        self.jarat = jarat

    def get_adatok(self):
        return [
            self.vezeteknev, self.keresztnev
        ] + self.jarat.get_adatok()

legitarsasagok = {}
jaratok_lista = []
foglalasok_lista = []

adatok = [
    ["W6-101","WizzAir","Budapest","London","2025-06-05 08:30","2:30","28000","nemzetkozi"],
    ["LH-204","Lufthansa","Budapest","Frankfurt","2025-06-06 12:00","1:45","35000","nemzetkozi"],
    ["RY-876","Ryanair","Budapest","Dublin","2025-06-07 07:00","3:10","32000","nemzetkozi"],
    ["FR-331","FR","Budapest","Debrecen","2025-06-05 10:00","0:50","9000","belfoldi"],
    ["MA-000","Malév","Budapest","Pécs","2025-06-05 14:00","1:00","9500","belfoldi"],
    ["TK-768","Turkish Airlines","Budapest","Istanbul","2025-06-08 16:45","2:00","40000","nemzetkozi"],
    ["LO-445","LOT","Budapest","Warsaw","2025-06-09 13:20","1:30","30000","nemzetkozi"],
    ["AF-119","Air France","Budapest","Paris","2025-06-10 18:00","2:25","42000","nemzetkozi"],
    ["FR-897","Ryanair","Szeged","Budapest","2025-06-05 11:15","0:55","8500","belfoldi"],
    ["W6-232","WizzAir","Budapest","Barcelona","2025-06-11 06:10","2:50","37000","nemzetkozi"],
    ["IB-334","Iberia","Budapest","Madrid","2025-06-12 13:00","3:05","36000","nemzetkozi"],
    ["W6-420","WizzAir","Budapest","Milánó","2025-06-07 09:45","1:40","31000","nemzetkozi"],
    ["FR-111","Ryanair","Budapest","Róma","2025-06-08 07:00","1:50","32000","nemzetkozi"],
    ["MA-001","Malév","Budapest","Szeged","2025-06-06 08:00","0:45","8000","belfoldi"],
    ["MA-002","Malév","Budapest","Győr","2025-06-07 12:30","1:00","8500","belfoldi"],
    ["FR-990","FR","Budapest","Miskolc","2025-06-08 14:30","0:50","8000","belfoldi"],
    ["BA-234","British Airways","Budapest","London","2025-06-09 17:00","2:40","43000","nemzetkozi"],
    ["SN-789","Brussels Airlines","Budapest","Brussels","2025-06-10 10:30","2:00","41000","nemzetkozi"],
    ["FR-559","Ryanair","Budapest","Nagykanizsa","2025-06-11 09:00","1:10","7800","belfoldi"],
    ["LH-888","Lufthansa","Budapest","München","2025-06-12 15:00","1:35","34000","nemzetkozi"]
]

jarat_dict = {}
for adat in adatok:
    jaratszam, legitarsasag, kiindulas, celallomas, indulas, idotartam, ar, tipus = adat

    if legitarsasag not in legitarsasagok:
        legitarsasagok[legitarsasag] = LegiTarsasag(legitarsasag)

    if tipus == "belfoldi":
        jarat = BelfoldiJarat(jaratszam, legitarsasag, kiindulas, celallomas, indulas, idotartam, ar, tipus)
    else:
        jarat = NemzetkoziJarat(jaratszam, legitarsasag, kiindulas, celallomas, indulas, idotartam, ar, tipus)

    legitarsasagok[legitarsasag].add_jarat(jarat)
    jaratok_lista.append(jarat)
    jarat_dict[jaratszam] = jarat

# Foglalások listája (kezdetben betöltött adatokkal)
foglalasok_lista = [
    Foglalas("Dönd", "Ödön", jarat_dict["W6-101"]),
    Foglalas("Érci", "Berci", jarat_dict["FR-111"]),
    Foglalas("Medve", "László", jarat_dict["LO-445"]),
    Foglalas("Gomba", "Gerda", jarat_dict["SN-789"])
]

def beolvas_jaratokat():
    fejlec = ["Járatszám", "Légitársaság", "Kiindulás", "Célállomás", "Indulás", "Időtartam", "Ár", "Típus"]
    return fejlec, [jarat.get_adatok() for jarat in jaratok_lista]


def foglalas_kattintas(jarat):
    popup = tk.Toplevel()
    popup.title("Járat részletei")
    popup.geometry("450x550")
    popup.resizable(False, False)

    tk.Label(popup, text="Járat részletei", font=("Arial", 14, "bold"), pady=10).pack()

    adatok_frame = tk.Frame(popup)
    adatok_frame.pack(pady=10)

    mezok = ["Járatszám", "Légitársaság", "Kiindulás", "Célállomás", "Indulás", "Időtartam", "Ár", "Típus"]
    for i, (mezo, ertek) in enumerate(zip(mezok, jarat)):
        tk.Label(adatok_frame, text=mezo + ":", font=("Arial", 11, "bold"), anchor='e', width=12).grid(row=i, column=0, padx=10, pady=4, sticky='e')
        tk.Label(adatok_frame, text=ertek, font=("Arial", 11), anchor='w').grid(row=i, column=1, padx=10, pady=4, sticky='w')

    input_frame = tk.Frame(popup)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Vezetéknév:", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=5, sticky='e')
    vezeteknev_entry = tk.Entry(input_frame, font=("Arial", 11), width=25)
    vezeteknev_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="Keresztnév:", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=5, sticky='e')
    keresztnev_entry = tk.Entry(input_frame, font=("Arial", 11), width=25)
    keresztnev_entry.grid(row=1, column=1, padx=10, pady=5)

    gomb_frame = tk.Frame(popup)
    gomb_frame.pack(pady=20)

    vasarlas_gomb = tk.Button(
        gomb_frame,
        text="Vásárlás",
        font=("Arial", 11, "bold"),
        bg="green",
        fg="white",
        state="disabled",
        width=12
    )
    vasarlas_gomb.grid(row=0, column=1, padx=10)

    def frissit_gomb_allapot(*args):
        if vezeteknev_entry.get().strip() and keresztnev_entry.get().strip():
            vasarlas_gomb.config(state="normal")
        else:
            vasarlas_gomb.config(state="disabled")

    vezeteknev_entry.bind("<KeyRelease>", frissit_gomb_allapot)
    keresztnev_entry.bind("<KeyRelease>", frissit_gomb_allapot)

    def vasarlas():
        vezeteknev = vezeteknev_entry.get().strip()
        keresztnev = keresztnev_entry.get().strip()
        if not (vezeteknev and keresztnev):
            return

        foglalasok_lista.append(Foglalas(vezeteknev, keresztnev, jarat_dict[jarat[0]]))

        print(f"Mentve: {vezeteknev} {keresztnev} – {jarat[0]}")
        popup.destroy()

    vasarlas_gomb.config(command=vasarlas)

    megse_gomb = tk.Button(gomb_frame, text="Mégse", font=("Arial", 11), command=popup.destroy, width=12)
    megse_gomb.grid(row=0, column=0, padx=10)

# Táblázat
def jegy_foglalasa():

    print("\nJaratok listazasa...")

    for widget in canvas_frame.winfo_children():
        widget.destroy()

    fejlec, jaratok = beolvas_jaratokat()

    #log
    n=0
    for i in jaratok:
        print("Beolvasva -",n,"-",i)
        n=n+1
    print("Jarat sikeresen betoltve:",n)

    if not jaratok:
        tk.Label(canvas_frame, text="Nincs betölthető járat.", font=("Arial", 12)).grid(row=0, column=0, sticky='w')
        return

    oszlopok = {
        "Légitársaság": 1,
        "Kiindulás": 2,
        "Célállomás": 3,
        "Indulás": 4,
        "Ár (Ft)": 6
    }

    for i, felirat in enumerate(list(oszlopok.keys()) + [""]):
        tk.Label(
            canvas_frame,
            text=felirat,
            font=("Arial", 11, "bold"),
            padx=10, pady=6,
            anchor='center'
        ).grid(row=0, column=i, sticky='nsew', padx=5)

    for sor_index, sor in enumerate(jaratok, start=1):

        for i, index in enumerate(oszlopok.values()):
            tk.Label(
                canvas_frame,
                text=sor[index],
                font=("Arial", 11),
                padx=10, pady=4,
                anchor='center'
            ).grid(row=sor_index, column=i, sticky='nsew', padx=5)

        link = tk.Label(
            canvas_frame,
            text="Foglalás",
            font=("Arial", 11, "underline"),
            fg="blue",
            cursor="hand2"
        )
        link.grid(row=sor_index, column=len(oszlopok), sticky='nsew', padx=5)
        link.bind("<Button-1>", lambda e, jarat=sor: foglalas_kattintas(jarat))

    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

def foglalasok_listazasa():

    print("\nFoglalások betöltése osztályból...")

    for widget in canvas_frame.winfo_children():
        widget.destroy()

    if not foglalasok_lista:
        tk.Label(canvas_frame, text="Még nincsen foglalásod :(", font=("Arial", 11)).grid(row=0, column=0, sticky='w')
        return

    fejlec = ["Utas neve", "Légitársaság", "Kiindulás", "Célállomás", "Indulás", ""]
    for col_index, mezo in enumerate(fejlec):
        tk.Label(
            canvas_frame,
            text=mezo,
            font=("Arial", 11, "bold"),
            padx=10,
            pady=6,
            anchor='center'
        ).grid(row=0, column=col_index, sticky='nsew')

    n=0

    for row_index, foglalas in enumerate(foglalasok_lista, start=1):
        jarat = foglalas.jarat
        teljes_nev = f"{foglalas.vezeteknev} {foglalas.keresztnev}"
        adatok = [teljes_nev, jarat.legitarsasag, jarat.kiindulas, jarat.celallomas, jarat.indulas]

        print("Betoltve -",n,jarat.jaratszam, teljes_nev, adatok)
        n=n+1

        for col_index, ertek in enumerate(adatok):
            tk.Label(
                canvas_frame,
                text=ertek,
                font=("Arial", 11),
                padx=10,
                pady=4,
                anchor='center'
            ).grid(row=row_index, column=col_index, sticky='nsew')

        link = tk.Label(
            canvas_frame,
            text="Lemondás",
            font=("Arial", 11, "underline"),
            fg="red",
            cursor="hand2"
        )
        link.grid(row=row_index, column=len(adatok), sticky='nsew', padx=5)

        def lemondas_popup(foglalas_obj):
            popup = tk.Toplevel()
            popup.title("Foglalás lemondása")
            popup.geometry("450x500")
            popup.resizable(False, False)

            tk.Label(popup, text="Foglalás lemondása", font=("Arial", 14, "bold"), pady=10).pack()

            mezok = ["Vezetéknév", "Keresztnév", "Járatszám", "Légitársaság", "Kiindulás", "Célállomás", "Indulás", "Időtartam", "Ár", "Típus"]
            ertekek = foglalas_obj.get_adatok()

            adatok_frame = tk.Frame(popup)
            adatok_frame.pack(pady=10)

            for i, (mezo, ertek) in enumerate(zip(mezok, ertekek)):
                tk.Label(adatok_frame, text=mezo + ":", font=("Arial", 11, "bold"), anchor='e', width=12).grid(row=i, column=0, padx=10, pady=4, sticky='e')
                tk.Label(adatok_frame, text=ertek, font=("Arial", 11), anchor='w').grid(row=i, column=1, padx=10, pady=4, sticky='w')

            gomb_frame = tk.Frame(popup)
            gomb_frame.pack(pady=20)

            def vegleges_lemondas():
                foglalasok_lista.remove(foglalas_obj)
                popup.destroy()
                foglalasok_listazasa()

            megse_btn = tk.Button(gomb_frame, text="Mégse", font=("Arial", 11), width=12, command=popup.destroy)
            megse_btn.grid(row=0, column=0, padx=10)

            lemond_btn = tk.Button(gomb_frame, text="Lemondás", font=("Arial", 11, "bold"), width=12, bg="red", fg="white", command=vegleges_lemondas)
            lemond_btn.grid(row=0, column=1, padx=10)

        link.bind("<Button-1>", lambda e, f=foglalas: lemondas_popup(f))
    print("Foglalás betoltve:",n)

    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


# GUI
ablak = tk.Tk()
ablak.title("Repülőjegy Foglalási Rendszer")
ablak.geometry("1000x600")

cimke = tk.Label(ablak, text="Repülőjegy Foglalási Rendszer", font=("Arial", 18, "bold"), pady=10)
cimke.pack()

gombok_keret = tk.Frame(ablak)
gombok_keret.pack(pady=8)

foglalas_gomb = tk.Button(gombok_keret, text="Jegy foglalása", font=("Arial", 13), command=jegy_foglalasa)
foglalas_gomb.grid(row=0, column=0, padx=10)

listazas_gomb = tk.Button(gombok_keret, text="Foglalásaim", font=("Arial", 13), command=foglalasok_listazasa)
listazas_gomb.grid(row=0, column=1, padx=10)

keret = tk.Frame(ablak)
keret.pack(expand=True, fill='both', padx=20, pady=10)

canvas = tk.Canvas(keret, bd=0, highlightthickness=0)
scrollbar = tk.Scrollbar(keret, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

canvas_frame = tk.Frame(canvas)
canvas_window = canvas.create_window((0, 0), window=canvas_frame, anchor="n")

def kozepre_igazitas(event):
    canvas_width = event.width
    canvas.coords(canvas_window, canvas_width // 2, 0)

canvas.bind("<Configure>", kozepre_igazitas)

ablak.mainloop()