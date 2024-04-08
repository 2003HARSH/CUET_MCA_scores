import streamlit as st
from utils import student_df_generator,actual_df_generator,answer_mapper,score_generator

st.title("Welcome to CUET PG score checker")
st.markdown("""---""")
st.write('Step',1,': Open your Answersheet form CUET PG website.')
st.write('Step',2,': Copy the link of your Answersheet and paste it here.')

link=st.text_input(placeholder='Enter the link of your answersheet',label='')
st.write('Step',3,': Hit Enter')
st.markdown("""---""")

if link:
    student_df=student_df_generator(link)
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
