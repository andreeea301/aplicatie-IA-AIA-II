import tkinter as tk
from tkinter import messagebox

def adauga_aliment():
    aliment = entry_aliment.get()
    calorii = entry_calorii.get()
    proteine = entry_proteine.get()
    glucide = entry_glucide.get()
    grasimi = entry_grasimi.get()

    if aliment and calorii.isdigit() and proteine.isdigit() and glucide.isdigit() and grasimi.isdigit():
        lista_alimente.insert(
            tk.END,
            f"{aliment} - {calorii} calorii, {proteine}g proteine, {glucide}g glucide, {grasimi}g grăsimi"
        )
        entry_aliment.delete(0, tk.END)
        entry_calorii.delete(0, tk.END)
        entry_proteine.delete(0, tk.END)
        entry_glucide.delete(0, tk.END)
        entry_grasimi.delete(0, tk.END)
        adauga_totaluri()
    else:
        messagebox.showwarning(
            "Eroare", "Introduceți valorile existente de pe ambalajul alimentului și macronutrienții (numerice)."
        )

def adauga_totaluri():
    total_calorii = 0
    total_proteine = 0
    total_glucide = 0
    total_grasimi = 0

    for item in lista_alimente.get(0, tk.END):
        valori = item.split(",")
        total_calorii += int(valori[0].split("-")[-1].strip().split()[0])
        total_proteine += int(valori[1].strip().split()[0][:-1])
        total_glucide += int(valori[2].strip().split()[0][:-1])
        total_grasimi += int(valori[3].strip().split()[0][:-1])

    label_total_calorii.config(text=f"Total calorii: {total_calorii}")
    label_total_proteine.config(text=f"Total proteine: {total_proteine}g")
    label_total_glucide.config(text=f"Total glucide: {total_glucide}g")
    label_total_grasimi.config(text=f"Total grăsimi: {total_grasimi}g")

root = tk.Tk()
root.title("Monitorizare calorii și macronutrienți")
root.geometry("600x500")

label_intrare = tk.Label(root, text="Introduceți alimentul și valorile nutriționale per 100g:")
label_intrare.pack(pady=5)

frame_intrare = tk.Frame(root)
frame_intrare.pack(pady=5)

entry_aliment = tk.Entry(frame_intrare, width=20)
entry_aliment.grid(row=0, column=0, padx=5)
entry_calorii = tk.Entry(frame_intrare, width=10)
entry_calorii.grid(row=0, column=1, padx=5)
entry_proteine = tk.Entry(frame_intrare, width=10)
entry_proteine.grid(row=0, column=2, padx=5)
entry_glucide = tk.Entry(frame_intrare, width=10)
entry_glucide.grid(row=0, column=3, padx=5)
entry_grasimi = tk.Entry(frame_intrare, width=10)
entry_grasimi.grid(row=0, column=4, padx=5)

button_adauga_aliment = tk.Button(frame_intrare, text="Adaugă aliment", command=adauga_aliment)
button_adauga_aliment.grid(row=0, column=5, padx=5)

lista_alimente = tk.Listbox(root, width=80)
lista_alimente.pack(pady=10)

label_total_calorii = tk.Label(root, text="Total calorii: 0", font=("Arial", 12))
label_total_calorii.pack(pady=5)

label_total_proteine = tk.Label(root, text="Total proteine: 0g", font=("Arial", 12))
label_total_proteine.pack(pady=5)

label_total_glucide = tk.Label(root, text="Total glucide: 0g", font=("Arial", 12))
label_total_glucide.pack(pady=5)

label_total_grasimi = tk.Label(root, text="Total grăsimi: 0g", font=("Arial", 12))
label_total_grasimi.pack(pady=5)

root.mainloop()
