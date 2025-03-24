# Data Analysis Assistant

## Overview
This project implements a **Data Analysis Assistant** using **Large Language Models (LLMs)** to analyze structured data (CSV or Excel) and generate insights through natural language queries. The application is built with **Streamlit** and integrates **LangChain agents** to generate and execute analysis code dynamically.

## Features
- Upload **CSV** or **Excel** files for analysis.
- Ask questions in **natural language** to analyze the dataset.
- Uses **Google Gemini-Pro** via LangChain for **intelligent query handling**.
- Dynamically generates and executes code for analysis.
- Provides **interactive visualizations** using Plotly.
- Displays **key dataset statistics** (rows, columns, column names, etc.).

## Technologies Used
- **Python** (Primary Language)
- **Streamlit** (UI framework)
- **Pandas** (Data manipulation)
- **Plotly** (Visualization)
- **LangChain** (LLM-based query handling)
- **Google Gemini-Pro** (LLM for code generation)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Shashank0769/data-analysis-assistant.git
   cd data-analysis-assistant
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up **Google API Key** for Gemini-Pro in your environment:
   ```sh
   export GOOGLE_API_KEY="your_key_here"  # For Linux/Mac
   set GOOGLE_API_KEY="your_key_here"  # For Windows
   ```

## Usage
1. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```

2. Open the app in your browser (`http://localhost:8501`).
3. Upload a **CSV** or **Excel** file.
4. Ask questions about the dataset in **natural language**.
5. View **analysis results and visualizations**.

## How It Works
1. **File Upload:** Users upload structured data in CSV or Excel format.
2. **Data Preview & Statistics:** The app displays dataset info like row/column count and column names.
3. **Query Processing:**
   - User submits a natural language query.
   - LangChain’s **Pandas DataFrame Agent** processes the request.
   - Google Gemini-Pro generates Python code for data analysis.
4. **Execution & Visualization:**
   - The generated code is executed securely.
   - If a visualization is required, **Plotly** is used to generate charts.
5. **Results Display:** The app displays insights and interactive plots.

## Limitations
- Limited to **public Google API quota**.
- Execution of user-generated code must be **handled securely**.
- LLM-generated code may require manual review for **complex queries**.

## Future Enhancements
- Support for more **file formats** (e.g., JSON, Parquet).
- **Database integration** for querying large datasets.
- **Enhanced security** for code execution.
- **Improved visualization** customization options.

## License
This project is licensed under the MIT License.

## Preview Images

![LLM_1](https://github.com/user-attachments/assets/41224e67-d414-428b-b2af-eab3f0f06c3e)

## Dataset Output

![LLM_2](https://github.com/user-attachments/assets/43fd1af1-c018-493d-81ed-3f67a5685211)

## Analysing the question

![Screenshot 2025-03-01 144624](https://github.com/user-attachments/assets/75fc61d3-7c9f-4aad-b207-8d306ec62cc7)

