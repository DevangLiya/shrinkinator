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

def update_figure(d):
	# green color: #20c20e
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=x_vals, y=[0.45]*len(x_vals), mode='markers', marker=dict(opacity=1, size=5), showlegend=False, 
		hovertext=hover_text))
	fig.add_trace(go.Scatter(x=[d], y=[0.42], mode='markers', showlegend=False, marker=dict(size=10)))
	fig.add_annotation(x=np.log10(d)-0.07, y=0.42, text="Your black hole", ax=-150, ay=0, showarrow=True, arrowhead=1, arrowwidth=3,
		font=dict(size=24, color='#ffffff'))

	fig.update_xaxes(title_text="Length in meters", title_font=dict(size=35, color='#ffffff'), type="log", range=[np.log10(d)-7, 
		np.log10(d)+7], tickfont=dict(size=24, color='#ffffff'), showgrid=True)
	fig.update_yaxes(range=[0.2, 0.5], showticklabels=False, showgrid=False, fixedrange=True)

	# there is clearly a more elegant way to doing this but i am lazy 
	add_image(fig, "shrinkinator_img/planck.png", -35)
	add_image(fig, "shrinkinator_img/proton.png", np.log10(8.4e-16))
	add_image(fig, "shrinkinator_img/atom.png", -10)
	add_image(fig, "shrinkinator_img/hair.png", -5)
	add_image(fig, "shrinkinator_img/penny.png", np.log10(0.02))
	add_image(fig, "shrinkinator_img/human.png", np.log10(1.6))
	add_image(fig, "shrinkinator_img/footballpitch.jpg", 2)
	add_image(fig, "shrinkinator_img/ncl.png", np.log10(15000))
	add_image(fig, "shrinkinator_img/uk.png", 6)
	add_image(fig, "shrinkinator_img/earth.png", np.log10(13e6))
	add_image(fig, "shrinkinator_img/sun.png", np.log10(1.4e9))
	add_image(fig, "shrinkinator_img/solarsystem.png", np.log10(12e12))
	add_image(fig, "shrinkinator_img/milkyway.png", np.log10(9.5e20))
	fig.update_layout_images(dict(xref="x", yref="y"))

	st.plotly_chart(fig, use_container_width=True)

#======================== define constants ========================
mass_dict = {'Football': 0.4, 'Human': 65, 'Car': 1500, 'Earth': 6e+24, 'Solar System': 2e30, 'Milky Way': 6e42}
image_dict = {'Football': 'football.png', 'Human': 'human.png', 'Car': 'car.png', 'Earth': 'earth.png', 
				'Solar System': 'solarsystem.png', 'Milky Way': 'milkyway.png'}
x_vals = [1.6e-35, 8.4e-16, 1e-10, 1e-5, 0.02, 1.6, 104, 15000, 1e6, 13e6, 1.4e9, 12e12, 9.5e20]
hover_text = ['Planck length', 'A proton', 'An atom', 'Width of human hair', 'British penny', 'Human', 'Football pitch', 
				'Newcastle upon Tyne', 'United Kingdom', 'Earth', 'Sun', 'Diameter of Pluto\' orbit', 'Milky Way']

#===================== Create page layout =========================
st.set_page_config(page_title='Create a black hole!', layout='wide')
st.markdown('# :hole: Create a black hole!')
st.divider()

left_col, right_col = st.columns(2)
left_col.markdown('### What would you like to shrink today?')
selected_object = left_col.radio('Pick one', list(mass_dict.keys()) + ['Enter a weight'], index=3)
rl, rm, rr = right_col.columns(3) # why does streamlit not have a way of centering image????
rm.markdown("<p style='font-size:35px;'>Now shrinking...</p>", unsafe_allow_html=True)

if selected_object == 'Enter a weight':
	M = left_col.number_input('Please enter weight in kilogram :weight_lifter:', min_value=0.0, value=6e24)
	d = get_schwarzschild_diameter(M)
	rm.markdown(f"<p style='text-align: center; font-size:25px;'>{M} kilogram of mass</p>", 
		unsafe_allow_html=True)
else:
	d = get_schwarzschild_diameter(mass_dict[selected_object])
	# rm.markdown(f'<img src="shrinkinator_img/{image_dict[selected_object]}" width="100" style="display: block; margin: 0 auto;">',
	# 	unsafe_allow_html=True)
	rm.image(f'shrinkinator_img/{image_dict[selected_object]}', width=200)

st.markdown(f'### :straight_ruler: Diameter of your black hole is {d} meter!')
update_figure(d)
