#bmystek
from pathlib import Path
import os

input_dir = '{}{}'.format(Path(__file__).parent,'''\\''')

# Ilość znaków do usunięcia
###############################################

ct=9

###############################################

for x in os.listdir(input_dir):
    if not x.endswith('.pdf') or len(x)<10 or x[0]!='0':
        continue
    old_name = '{}\\{}'.format(input_dir,x)
    new_name = old_name.replace('_02_','_02_Rysunek ogólny. Rzut')
    # new_name = old_name.replace('_03_','_03_Rysunek ogólny. Przekrój podłużny i widok z boku')
    # new_name = old_name.replace('_04_','_04_Rysunek ogólny. Przekroje poprzeczne.')
    if new_name not in input_dir:
        os.rename(old_name, new_name)