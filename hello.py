import streamlit as st

st.write("URL:", st.secrets.get("SUPABASE_URL"))
st.write("KEY exists:", "SUPABASE_KEY" in st.secrets)