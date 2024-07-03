import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def main():
    load_dotenv()

    # UI STUFF
    st.set_page_config(page_title="Ask your pdf")
    st.header("Ask your PDF")
    pdf = st.file_uploader("Upload your pdf", type="pdf")



    if pdf is not None:
        # Reading the pdf file
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()


        st.write(text)



if __name__ == '__main__':
    main()
