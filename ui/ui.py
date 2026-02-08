import streamlit as st
import requests

st.title("COREP Reporting Assistant")

cet1 = st.number_input("CET1")
tier1 = st.number_input("Tier 1")
tier2 = st.number_input("Tier 2")
rwa = st.number_input("RWA")

if st.button("Generate COREP Report"):
    response = requests.post(
        "http://127.0.0.1:8000/scenario",
        json={
            "cet1": cet1,
            "tier1": tier1,
            "tier2": tier2,
            "rwa": rwa
        }
    )
    st.text(response.json()["template"])
