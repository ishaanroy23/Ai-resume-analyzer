import streamlit as st
from ai_response import generate_response
from text_extractor import extract_text_from_pdf

st.set_page_config(page_title="AI Resume Analyzer/Critiquer",layout = 'wide')

st.sidebar.title("AI Resume Anlyzer/Critiquer")
st.title(":blue[Welcome to Ai Resume Anlyzer/Critiquer]")
st.sidebar.divider()

upload_file = st.sidebar.file_uploader("Upload Your Resume",type = ['.pdf'])

if upload_file is not None:
    col1,col2 = st.columns([2,3])
    button = None
    job_description = ''
    with col1:
        with st.container(border=True):
            st.markdown("### :green[Uploaded Resume:]")
            extracted_text = extract_text_from_pdf(upload_file)
            if extracted_text is None:
                st.error("Failed to extract the text from the resume")
                st.stop()
            with st.expander("Extracted Text From Resume"):
                st.write(extracted_text)

            choice = st.selectbox("Select an Option",['Resume Critque', 'Resume Analyzer'])
            if choice == "Resume Critque":
                button = st.button(":red [**Crique Resume**]")
            elif choice == "Resume Analyzer":
                job_description = st.text_area(
                    "paste the description of the job",
                    height = 200
                )
                button = st.button(":violet[**Analyze Resume**]")

    if button:
        if choice == 'Resume Analyzer' and not job_description.strip():
            st.warning("Please Paste the job description before analyzing")
        else:
            with col2:
                with st.container(border=True):
                    with st.spinner("Generating response..."):
                        print("CHOICE:", repr(choice))
                        response = generate_response(extracted_text , job_description , choice)
                        st.markdown(response)

