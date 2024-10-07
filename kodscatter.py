import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj plik CSV z podanej ścieżki
file_path = '/Users/patryksusz/Documents/STUDIA/OneDrive_3_10-7-2024/data_preproc/z_geoportal_up42.csv'
df = pd.read_csv(file_path)

# Ustawienie kolumn do wykresu
x = df['X']  # Kolumna X
y = df['Y']  # Kolumna Y
z = df['Z']  # Kolumna Z

# Utworzenie wykresu punktowego
plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=z, cmap='viridis', marker='o')  # Kolorowanie punktów na podstawie Z
plt.colorbar(label='Z')  # Dodanie paska kolorów

# Tytuł i etykiety
plt.title('Wykres punktowy (X, Y) z kolorem zależnym od Z')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
