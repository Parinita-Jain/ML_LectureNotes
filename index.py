import streamlit as st

#st.write(" # Hello World")

#-------------------Taking input from user

#hrs=st.text_input("Enter No of Hours you Study : ")#,"Enter Student Name")
#st.text_input("roll_no")#,"Enter Roll Number")

#-------------- if i/p is in the form of a paragraph ,use st.text_area

#------------------Button

#st.button("Predict")


import pickle


file1=open("classifier.pkl","rb")

model=pickle.load(file1)

hrs=st.number_input("Enter No of Hours you Study : ")


def makeprediction(newob):
    #newob = float(input("Enter No of Hours you Study : "))
    #newob=st.text_input("Enter No of Hours you Study : ")
    yp = model.predict([[newob]])[0]
    print(f"If you study of {newob} hrs, you will score arround {yp:.2f} marks")
    return yp


if st.button("Predict"):
    result=makeprediction(hrs)
    st.write(result)
    