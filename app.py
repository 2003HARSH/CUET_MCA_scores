import streamlit as st
from utils import student_df_generator,actual_df_generator,answer_mapper,score_generator
st.set_page_config(
        page_title="CUET MCA score checker",
)

st.title("Welcome to CUET MCA (SCQP09) score checker")
st.markdown("""---""")
st.write('Step',1,': Open your Answersheet form CUET PG website.')
st.write('Step',2,': Press Ctrl + S to save the file as a .html document.')

html_page=st.file_uploader('Upload the saved .html file to this website.')
st.markdown("""---""")

if html_page:
    student_df=student_df_generator(html_page)
    if student_df is not None:
        actual_df=actual_df_generator()

        student_df['correct_option']=student_df['q_id'].apply(answer_mapper,args=(actual_df,))


        student_df=score_generator(student_df)

        st.header('Your Marks Matrix')
        st.dataframe(student_df)

        st.write('Your total score is ',student_df['marks'].sum(),' out of ',300)
        st.write('No. of correct questions',student_df['marks'].value_counts()[4])
        st.write('No. of incorrect questions',student_df['marks'].value_counts()[-1])
        st.write('No. of unattempted questions',student_df['marks'].value_counts()[0])
