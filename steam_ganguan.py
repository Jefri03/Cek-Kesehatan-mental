import pickle
import streamlit as st

#membaca model

gangguan_data_model = pickle.load(open('gangguan_model.sav','rb'))

#Judul
st.title('Prediksi Kondisi Kesehatan Mental')
st.subheader('Pilih 1 untuk "Ya" dan 0 untuk "Tidak"')

q1 = st.text_input('Apakah Persaan anda berubah berubah?')
q2 = st.text_input('Apakah anda kelihatan murung?')
q3 = st.text_input('Apakah anda mudah merasa lelah?')
q4 = st.text_input('Apakah anda sering mengalami kurang fokus?')
q5 = st.text_input('Apakah anda sering merasa bersalah?')
q6 = st.text_input('Apakah anda mulai menyakiti diri sendiri?')
q7 = st.text_input('Apakah Anda mengalami kesulitan tidur?')
q8 = st.text_input('Apakah anda mengalami nafsu makan berkurang?')
q9 = st.text_input('Apakah anda merasa bahwa anda mudah marah?')
q10 = st.text_input('Apakah anda mulai mengasingkan diri dari lingkungan?')
q11 = st.text_input('Apakah anda mengalami halusinasi?')
q12 = st.text_input('Apakah pikiran anda sering kacau?')
q13 = st.text_input('Apakah perilaku anda sering berubah-ubah?')
q14 = st.text_input('Apakah anda sulit merasa senang?')
q15 = st.text_input('Apakah anda tidak peduli dengan penampilan atau kebersihan diri?')
q16 = st.text_input('Apakah anda enggan bersosialisasi?')
q17 = st.text_input('Apakah anda tidak memiliki emosi?')
q18 = st.text_input('Apakah anda sering merasa cemas?')
q19 = st.text_input('Apakah anda Mudah tersinggung?')
q20 = st.text_input('Apakah anda sulit mengambil keputusan?')
q21 = st.text_input('Apakah anda mengalami sakit kepala?')
q22 = st.text_input('Apakah anda sering mengalami mual ?')
q23 = st.text_input('Apakah anda mengalami sakit perut atau diare?')

#code untuk predksi

gangguan_diaknosis = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Kesehatan Mental'):
    gangguan_prediction = gangguan_data_model.predict([[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23]])
 
    if (gangguan_prediction[0]==0):
      gangguan_diaknosis = 'Anda terindikasi mengalmi gangguan depresi'
    elif (gangguan_prediction[0]==1):
        gangguan_diaknosis= ' Anda terindikasi mengalami gangguan kecemasan'
    elif (gangguan_prediction[0]==2):
        gangguan_diaknosis= ' Anda terindikasi mengalami gangguan Skizofenia'
    else :
        gangguan_diaknosis= ' Anda belum terindentifikasi , lakukan pengecekan ke dokter'
    st.success(gangguan_diaknosis)
