import streamlit as st


st.subheader('آموزش و پرورش منطقه 5')
st.header("دبیرستان خیام")
st.text('کلاس دهم 2 ')

col1, col2, col3 = st.columns(3)
col1.write("پایه دهم")

col2.write("پایه یازدهم")

col3.write("پایه دوازدهم")



tab1, tab2, tab3 = st.tabs(["ریاضی", "فیزیک","عربی"])
with tab1:
    st.write("درس ریاضی")

with tab2:
    st.write("درس فیزیک")
    st.image('Images/ElonImg.jpg')
with tab3:
    st.write("درس عربی")
    st.image('Images/bill.jpg')
with st.sidebar:
    with st.form(key='فرم ورود'):
        username = st.text_input('نام کاربری')
        password = st.text_input('پسورد')
        st.form_submit_button('کلیک کنید')



with st.container():
    st.write("This is inside the container")
    st.image('Images/lena.png')
    st.radio('انتخاب کنید', ['دهم', 'یازدهم','دوازدهم'])

st.write("This is outside the container")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("آروین امینی")
   st.image('Images/lena.png')

with col2:
   st.header("احسان جهانگیری")
   st.image('Images/bill.jpg')

with col3:
   st.header("مرتضی عسگری")
   st.image('Images/ElonImg.jpg')
