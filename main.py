import streamlit as st
import pandas

data = {
  'Series 1':[1,3,4,5,7],
  'Series 2':[10,30,40,100,250]

}

df = pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write('''This is our first web app.
Enjoy it!
''')

st.write(df)

st.line_chart(df)