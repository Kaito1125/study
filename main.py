import streamlit as st
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Display Image')

latest_iteration = st.empty()
bar = st.progress(0)

img = Image.open('thumbnail_A.jpg')
display = st.checkbox('こじをを表示させる')

if display:
    for i in range(100):
        latest_iteration.text(f'こじを降臨中 {i+1}　％')
        bar.progress(i + 1)
        time.sleep(0.08)
    st.image(img, caption="こじを")
