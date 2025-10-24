import math
import customtkinter as ctk
from tkinter import messagebox

# Déclaration des points et des étiquettes pour la classification
points = []
labels = []  # Liste des labels pour les points 

def calculer_distance(point1, point2):
    """Calcule la distance euclidienne entre deux points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def ajouter_point():
    try:
        x, y = map(float, entry_point.get().split(','))
        label = entry_label.get().strip()
        if not label:
            raise ValueError("Le label est vide.")
        points.append((x, y))
        labels.append(label)
        points_list.insert("end", f"({x}, {y}) - {label}\n")
        entry_point.delete(0, "end")
        entry_label.delete(0, "end")
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

def calculer_resultat():
    if not points:
        messagebox.showerror("Erreur", "Aucun point n'a été saisi.")
        return
    try:
        reference = tuple(map(float, entry_reference.get().split(',')))
        if len(reference) != 2:
            raise ValueError("Veuillez entrer un point valide.")
        
        # Recherche du point le plus proche
        distances = [(calculer_distance(reference, point), i) for i, point in enumerate(points)]
        distances.sort()  # Trie les distances par ordre croissant
        distance_min, index_min = distances[0]
        distance_max = distances[-1][0]  # Distance maximale
        
        # Calcul de la précision
        precision = (1 - (distance_min / distance_max))*100
        
        # Affichage des résultats
        result_label.configure(
            text=f"Point le plus proche: {points[index_min]} ({labels[index_min]})\n"
                 f"Distance: {distance_min:.4f}\n"
                 f"Précision: {precision:.4f}%"
        )
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


def reinitialiser():
    points.clear()
    labels.clear()
    points_list.delete(1.0, "end")
    entry_point.delete(0, "end")
    entry_label.delete(0, "end")
    entry_reference.delete(0, "end")
    result_label.configure(text="")

# Interface graphique (inchangée sauf pour ajouter un champ de label)
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.title("Trouver le Point le Plus Proche ")
app.geometry("800x500")

# Section pour ajouter des points
frame_ajout = ctk.CTkFrame(app)
frame_ajout.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(frame_ajout, text="Saisir un point (x,y):", anchor="w").pack(side="left", padx=10, pady=5)
entry_point = ctk.CTkEntry(frame_ajout, width=200, placeholder_text="Exemple : 1,2")
entry_point.pack(side="left", padx=10)
ctk.CTkLabel(frame_ajout, text="Label:", anchor="w").pack(side="left", padx=10, pady=5)
entry_label = ctk.CTkEntry(frame_ajout, width=200, placeholder_text="Exemple : Ville A")
entry_label.pack(side="left", padx=10)
btn_ajouter = ctk.CTkButton(frame_ajout, text="Ajouter", command=ajouter_point)
btn_ajouter.pack(side="left", padx=10)

# Liste des points saisis
frame_points = ctk.CTkFrame(app)
frame_points.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(frame_points, text="Points saisis:", anchor="w").pack(anchor="w", padx=10, pady=5)
points_list = ctk.CTkTextbox(frame_points, height=150, state="normal", wrap="word")
points_list.pack(padx=10, pady=5, fill="x")

# Saisie du point de référence
frame_reference = ctk.CTkFrame(app)
frame_reference.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(frame_reference, text="Point de référence (x,y):", anchor="w").pack(side="left", padx=10, pady=5)
entry_reference = ctk.CTkEntry(frame_reference, width=200, placeholder_text="Exemple : 3,2")
entry_reference.pack(side="left", padx=10)

# Bouton pour calculer le résultat
btn_calculer = ctk.CTkButton(app, text="Calculer", command=calculer_resultat)
btn_calculer.pack(pady=10)

# Affichage des résultats
result_label = ctk.CTkLabel(app, text="", font=("Arial", 16), text_color="darkred")
result_label.pack(pady=10)

# Bouton pour réinitialiser
btn_reset = ctk.CTkButton(app, text="Réinitialiser", command=reinitialiser)
btn_reset.pack(pady=10)

# Lancer l'application
app.mainloop()
