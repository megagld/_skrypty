#bmystek
from pathlib import Path
import os

input_dir = '{}{}'.format(Path(__file__).parent,'''\\''')

# Numeracja rysunków i ich nazwy
###############################################

rys=[
    ['_01','_01_Rysunek ogólny. Założenia drogowe. Plan i profil'],
    ['_02','_02_Rysunek ogólny. Rzut'],
    ['_03','_03_Rysunek ogólny. Przekrój podłużny i widok z boku'],
    ['_04','_04_Rysunek ogólny. Przekroje poprzeczne']
]

###############################################

for x in os.listdir(input_dir):
    if not x.endswith('.pdf') or len(x)<10 or x[0]!='0':
        continue
    old_name = '{}{}'.format(input_dir,x)
    new_name = old_name
    for i,j in rys:
        new_name = new_name.replace(i,j)
    if new_name not in input_dir:
        os.rename(old_name, new_name)