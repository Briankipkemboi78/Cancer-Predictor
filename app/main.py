import streamlit as st
import pickle
import pandas as pd



def main():
    st.set_page_config(
        page_title="Breast Cancer Predictor",
        page_icon=":female-doctor",
        layout="wide",
        initial_sidebar_state="expanded"
        )
    
    with st.container():
        st.title("Breast Cancer Predictor")
        st.write("Please connect this app to your cytology lab to help diagnose breast cancer from your tissue sample. This app uses machine learning model to tell whether a breast mass is benign or malignant based on the measurements it receives from cytology lab.")

        st.columns(4, 1)
    



if __name__ == '__main__':
    main()