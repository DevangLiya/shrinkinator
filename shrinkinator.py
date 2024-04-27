import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import numpy as np

def get_schwarzschild_diameter(M):
	G = 6.674e-11
	c = 299792458

	return 2*(2*G*M)/(c**2)

def add_image(fig, image_fn, x_pos):
	# https://plotly.com/python/images/
	pyLogo = Image.open(image_fn)
	fig.add_layout_image(dict(source=pyLogo, x=x_pos, y=0.3, sizex=1, sizey=1, xanchor="center", yanchor="middle"))

st.set_page_config(page_title='Create a black hole!', layout='wide')
st.markdown('# :hole: Create a black hole!')
st.divider()

st.markdown('### :weight_lifter:')
M = st.number_input(r"$\textsf{\Large Enter the mass in kilogram}$", min_value=0.0, value=1e24)
r = get_schwarzschild_diameter(M)
d = 2*r

st.markdown(f'### :straight_ruler: Diameter of your black hole is {d} meter!')

#============================ plotting ============================
x_vals = [1.6e-35, 8.4e-16, 1e-10, 1e-5, 0.02, 1.6, 104, 15000, 1e6, 13e6, 700e6, 1e12, 9.5e20]
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_vals, y=[0.45]*len(x_vals), mode='markers', marker=dict(opacity=1), showlegend=False))
fig.add_trace(go.Scatter(x=[d], y=[0.3], mode='markers', showlegend=False, marker=dict(size=10)))
fig.add_annotation(x=np.log10(d), y=0.31, text="Your black hole", showarrow=True, arrowhead=1)

fig.update_xaxes(title_text="Length in meters", type="log", range=[np.log10(d)-5, np.log10(d)+5])
fig.update_yaxes(range=[0.2, 0.5], showticklabels=False)

# there is clearly a more elegant way to doing this but i am lazy 
add_image(fig, "bh_mass_img/planck.png", -35)
add_image(fig, "bh_mass_img/proton.png", np.log10(8.4e-16))
add_image(fig, "bh_mass_img/atom.png", -10)
add_image(fig, "bh_mass_img/hair.png", -5)
add_image(fig, "bh_mass_img/penny.png", np.log10(0.02))
add_image(fig, "bh_mass_img/human.png", np.log10(1.6))
add_image(fig, "bh_mass_img/footballpitch.jpg", 2)
add_image(fig, "bh_mass_img/ncl.png", np.log10(15000))
add_image(fig, "bh_mass_img/uk.png", 6)
add_image(fig, "bh_mass_img/earth.png", np.log10(13e6))
add_image(fig, "bh_mass_img/sun.png", np.log10(700e6))
add_image(fig, "bh_mass_img/solarsystem.png", 12)
add_image(fig, "bh_mass_img/milkyway.png", np.log10(9.5e20))

fig.update_layout_images(dict(xref="x", yref="y"))

st.plotly_chart(fig, use_container_width=True)
#==================================================================