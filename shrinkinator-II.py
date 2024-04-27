import streamlit as st
import numpy as np

def get_schwarzschild_diameter(M):
	G = 6.674e-11
	c = 299792458

	return 2*(2*G*M)/(c**2)

mass_dict = {'Football': 0.4, 'Human': 65, 'Car': 1500, 'Earth': 6e+24, 'Solar System': 2e30, 'Milky Way': 6e42}
length_dict = {'Size of an atom': 0.0000000001, 'Height of a human': 1.6, 'Length of St James Park pitch': 104, 'Size of Newcastle': 15000,
				'Length of the UK': 1000000, 'Diameter of the Earth': 12000000, 'Diameter of the Sun': 1400000000, 
				'Diameter of Pluto orbit': 12000000000000}

st.set_page_config(page_title='Create a black hole!', layout='wide')
st.markdown('# :hole: Create a black hole!')
st.divider()

left_col, right_col = st.columns(2)

# object select
left_col.markdown('## What would you like to shrink today?')
selected_object = left_col.radio('Pick one', mass_dict.keys())
M = mass_dict[selected_object]

# processed diameter
right_col.markdown('## Some common lengths')
d = get_schwarzschild_diameter(M)
length_dict['Diameter of your black hole'] = d
length_dict = dict(sorted(length_dict.items(), key=lambda item: item[1]))
sizes_string = ''
for obj, diam in length_dict.items():
	if obj == 'Diameter of your black hole':
		sizes_string = sizes_string + f'- **{obj}: {diam} m**\n'
	else:
		sizes_string = sizes_string + f'- {obj}: {diam} m\n'

right_col.markdown(sizes_string)

# extra stuff
st.divider()
mass_col, radius_col = st.columns(2)
mass_col.metric('Mass of the object', f'{M} kg')
radius_col.metric('Diameter of the black hole', f'{d} meter')