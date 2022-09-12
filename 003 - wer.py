import pandas as pd
# tu trzeba wprowadzić ścieżkę do pliki:

df = pd.read_excel (r'C:\_magazyn\0139_A2\2021.12.14 - Strony postępowania\04_Weryfikacja powtórzeń\7.xlsx', sheet_name='prywatne')
# print (df)

wlasciciele= pd.DataFrame(df, columns= ['Właściciel'])

# konwersja do zwykłej listy
dane=df['Właściciel'].tolist()
#usunięcie duplikatów
dane=set(i.strip() for i in dane)





