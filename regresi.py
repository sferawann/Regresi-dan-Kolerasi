import csv
import streamlit as st
import pandas as pd
import math
import os
from streamlit.script_runner import StopException, RerunException

st.title('Tugas Pemrograman Simulasi')
st.subheader(' Syahrul Fathurrahman Erawan')
st.subheader(' 152017030')
st.sidebar.subheader('Hasil')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

x = df.iloc[:, :-1].values
y = df.iloc[:, 1].values


def find_mul_sum(a, b):
    abc = 0
    for i in range(len(a)):
        abc += (a[i]*b[i])
    return abc


sx = float(sum(x))
sy = float(sum(y))
sx2 = float((sum(x)**2))
sy2 = float((sum(y)**2))
sx_2 = float(sum(x**2))
sy_2 = float(sum(y**2))
sxy = float(find_mul_sum(x, y))
n = len(df)
konstanta_a = round((sy*sx_2 - sx*sxy) / (n*sx_2 - sx2), 3)
koefisien_b = round(((n*sxy) - (sx*sy)) / ((n*sx) - sx2), 3)
paket1_r = round((n*sxy)-(sx*sy))
paket2_r = round(((n*sx_2)-sx2)*((n*sy_2)-sy2))
paket3_r = math.sqrt(paket2_r)
r = round((paket1_r/paket3_r), 3)
kd = round((r**2)*100, 3)
variabellain = round((100-kd), 3)

if st.sidebar.checkbox('Sigma X ?'):
    st.sidebar.write('Sigma X : '+str(sx))
if st.sidebar.checkbox('Sigma Y ?'):
    st.sidebar.write('Sigma Y :', str(sy))
if st.sidebar.checkbox('(Sigma x)^2 ?'):
    st.sidebar.write('(Sigma x)^2 :', str(sx2))
if st.sidebar.checkbox('(Sigma Y^)2 ?'):
    st.sidebar.write('(Sigma Y^)2 ', str(sy2))
if st.sidebar.checkbox('Sigma X^2 ?'):
    st.sidebar.write('Sigma X^2 :', str(sx_2))
if st.sidebar.checkbox('Sigma Y^2 ?'):
    st.sidebar.write('Sigma Y^2 :', str(sy_2))
if st.sidebar.checkbox('Sigma XY ?'):
    st.sidebar.write('Sigma XY :', str(sxy))
if st.sidebar.checkbox('Konstanta(a) ?'):
    st.sidebar.write('Konstanta(a) :', str(konstanta_a))
if st.sidebar.checkbox('Koefisien(b) ?'):
    st.sidebar.write('Koefisien(b) :', str(koefisien_b))


st.sidebar.subheader('X')
x_input = st.sidebar.number_input('Masukan jumlah sertifikat')

Y_hasil = konstanta_a + (koefisien_b*float(x_input))
st.sidebar.subheader('Y')
st.sidebar.text(str(Y_hasil))

if st.checkbox('Nilai Kolerasi ?'):
    st.write('Nilai Kolerasinya adalah : ', r)
    if (r < 0):
        st.write(
            'Nilai Kolerasi tersebut adalah negatif yang mengartikan bahwa perbandingannya adalah terbalik')
    else:
        st.write(
            'Nilai Kolerasi tersebut adalah positif yang mengartikan bahwa perbandingannya searah')
    if (r > 0 and r <= 0.2):
        st.write('Kekuatan Hubungan = Sangat Lemah')
    elif (r > 0.2 and r <= 0.4):
        st.write('Kekuatan Hubungan = Lemah')
    elif (r > 0.4 and r <= 0.6):
        st.write('Kekuatan Hubungan = Sedang')
    elif (r > 0.6 and r <= 0.8):
        st.write('Kekuatan Hubungan = Kuat')
    elif (r > 0.8 and r <= 1):
        st.write('Kekuatan Hubungan = Sangat Kuat')
    else:
        st.write(' Nilai r tidak masuk kemana mana')

if st.checkbox('Nilai Koefisien Determinasi ?'):
    st.write('Nilai Koefisien Determinasi Adalah = ', kd)
    st.write("Jadi kontribusi variabel X terhadap Y adalah " + str(kd) + " %" +
             " dan sisanya sebesar " + str(variabellain) + " %"+" dipengaruhi oleh variabel selain X")
