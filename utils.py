import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import streamlit as st

def student_df_generator(link):
    try:
        response=requests.get(link)
        soup=BeautifulSoup(response.text)
        l=[]
        for i in soup.find_all('td',class_='bold'):
            l.append(i.text.strip())

        q_id=[]
        for i in range(4,len(l),11):
            q_id.append(l[i])

        chosen_option=[]
        for i in range(10,len(l),11):
            chosen_option.append(l[i])
        
        dict={'q_id':q_id,'chosen_option':chosen_option}

        student_df=pd.DataFrame(dict)
        student_df.replace('--',0,inplace=True)

        return student_df

    except:
        st.header('Some error Occoured')
        return None


def actual_df_generator():
    with open('answer.txt','r',encoding='utf-8')as f:
        soup=BeautifulSoup(f,'html.parser')
        
        l=[]
        for i in soup.find_all('td'):
            l.append(i.text.strip())

        q_id=[]
        for i in range(2,len(l),9):
            q_id.append(l[i])

        correct_option=[]
        for i in range(3,len(l),9):
            correct_option.append(l[i])

        dict={'q_id':q_id,'actual_option':correct_option}

        actual_df=pd.DataFrame(dict)
        
        return actual_df
    
def answer_mapper(q_id,actual_df):
    count=0
    for i in actual_df['q_id'].values:
        if i==q_id:
            return actual_df.iloc[count,1]
        count+=1

def score_generator(student_df):
    score=[]
    for i in range(75):
        if student_df['chosen_option'].iloc[i]==0:
            score.append(0)
        elif student_df['chosen_option'].iloc[i]==student_df['correct_option'].iloc[i]:
            score.append(4)
        elif student_df['chosen_option'].iloc[i]!=student_df['correct_option'].iloc[i]:
            score.append(-1)
    
    student_df['marks']=np.array(score)
    return student_df