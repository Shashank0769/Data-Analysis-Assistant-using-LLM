import streamlit as st
import pandas as pd
import plotly.express as px
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.callbacks.manager import CallbackManager
import os

st.set_page_config(page_title="Data Analysis Assistant", layout="wide")

os.environ["GOOGLE_API_KEY"] = "AIzaSyDP0es51kKH9spr-MU0I9P93sAy6vjVbPc"

def load_data(uploaded_file):
    try:
        if uploaded_file.name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xls', '.xlsx')):
            return pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None

def create_agent(df):
    callback_manager = CallbackManager([StreamlitCallbackHandler(st.container())])
    
    return create_pandas_dataframe_agent(
        ChatGoogleGenerativeAI(model="gemini-pro", temperature=0),
        df,
        verbose=True,
        callback_manager=callback_manager,
        allow_dangerous_code=True
    )

def main():
    st.title("Data Analysis")
    st.write("Upload your data and ask questions in natural language!")


    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx', 'xls'])
    
    if uploaded_file:
        df = load_data(uploaded_file)
        
        if df is not None:
            st.subheader("Data Preview")
            st.dataframe(df.head())
            
            st.subheader("Dataset Info")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Number of rows:", df.shape[0])
                st.write("Number of columns:", df.shape[1])
            with col2:
                st.write("Columns:", ", ".join(df.columns))

            agent = create_agent(df)

            st.subheader("Ask Questions")
            question = st.text_area(
                "What would you like to know about your data?"
            )

            if st.button("Analyze"):
                if question:
                    with st.spinner("Analyzing..."):
                        try:
                            enhanced_question = f"""
                            {question}
                            If the answer involves data visualization, please use plotly.express and store the figure in a variable called 'fig'.
                            """
                            response = agent.run(enhanced_question)
                            
                            st.subheader("Analysis Results")
                            st.write(response)

                        except Exception as e:
                            st.error(f"An error occurred: {str(e)}")
                            st.error("Details:", str(e))
                else:
                    st.warning("Please enter a question about your data.")

if __name__ == "__main__":
    main()