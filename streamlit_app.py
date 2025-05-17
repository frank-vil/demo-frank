import streamlit as st
import pandas as pd
import requests
from io import StringIO

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


def load_original_data():
    url = 'https://raw.githubusercontent.com/frank-vil/demo-frank/main/superstore.csv'
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
  

#file_tienda = 'https://raw.githubusercontent.com/frank-vil/demo-frank/main/superstore.csv'  
#df_tienda = pd.read_csv(file_tienda, index_col=None)
df_tienda = load_original_data()
st.dataframe(df_tienda,
             hide_index=True,
             height=210)

sales_columns = st.columns(2)
sales_min = sales_columns[0].number_input('Min Sal', value=df_tienda['Sales'].min() )
sales_max = sales_columns[1].number_input("Max Sal", value=df_tienda['Sales'].max() )
