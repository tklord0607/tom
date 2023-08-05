#安裝網頁顯示用的模組 pip instaill streamlit
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

t = np.arange(0.,1.0,0.05)
st.write(t)
y1 = np.sin(2 * np.pi * t)
y2 = np.cos(2 * np.pi * t)
st.write(y1)
st.write(y2)
figure1 = plt.figure(figsize=(8,4))
axes1 = figure1.add_subplot()
axes1.plot(y1)
axes1.plot(y2)
st.write(figure1)
#在終端機輸入：streamlit run T080503.py   可用網頁顯示輸出資料與圖型
#要離開按ctrl+c