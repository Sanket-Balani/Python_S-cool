import streamlit as st
import pandas as pd

#Setting up Tables
theory_marks=[]
lab_marks=[]


st.set_page_config( page_title = "CalcGPA", page_icon = None) 
#for page title & favicon


def grades(marks):
    if marks >= 90:
        grade = 10
    elif marks >= 75:
        grade = 9
    elif marks >= 65:
        grade = 8
    elif marks >= 55:
        grade = 7
    elif marks >= 50:
        grade = 6
    elif marks >= 45:
        grade = 5
    elif marks >= 40:
        grade = 4
    else:
        grade = 0
    
    return grade



def calc(sem):
    subjects = {}
    labs = {}
    GPA = 0
    flag = 0  #for the warning message when marks haven't entered
    credits = 0
    col1, col2 = st.columns(2)  #for columns: one for theory sub, and another for lab sub

    if sem == 1 :
        subjects = { 'Applied Maths-I' : 4, 'Applied Physics-I' : 3, 'Manufacturing Processes' : 4, 'Electrical Science' : 3, 'Communication Skills' : 3, 'Applied Chemistry' : 3 }
        labs = { 'Applied Physics Lab-I' : 1, 'Elecrical Science Lab' : 1, 'Engineering Graphics-I Lab' : 2, 'Applied Chemistry Lab' : 1 }
        credits = 25

    elif sem == 2:
        subjects = { 'Applied Maths-II' : 4, 'Applied Physics-II' : 3, 'Programming in C' : 3, 'EVS' : 3, 'Indian Constitution' : 2, 'Human Values and Ethics' : 1, 'Engineering Mechanics' : 3}
        labs = { 'Applied Physics Lab-II' : 1, 'Programming in C Lab' : 1, 'Engineering Graphics-II Lab' : 1, 'Workshop Practice' : 1, 'EVS Lab' : 2 }
        credits = 25

    elif sem == 3:
        subjects = { 'Applied Maths-III' : 4, 'Foundation of Computer Science' : 4, 'Switching Theory & Logic Design' : 4, 'Circuits & Systems' : 4, 'Data Structures' : 4, 'Computer Graphics & Multimedia' : 4, }
        labs = { 'Switching Theory & Logic Design Lab' : 1, 'Data Stucture Lab' : 1, 'Circuits & Systems Lab' : 1, 'Computer Graphics & Multimedia Lab' : 1 }
        credits = 28

    elif sem == 4:
        subjects = { 'Applied Maths-IV' : 4, 'Computer Organisation & Architecture' : 4, 'Theory of Computation' : 4, 'Database Management' : 4, 'Object Oriented Programming' : 3, 'Communication Systems' : 4 }
        labs = { 'Applied Maths Lab' : 1, 'Computer Organisation and Architecture Lab' : 1, 'Database Managemant Systems Lab' : 1, 'Object Oriented Programming Lab' : 1, 'Communication Systems Lab' : 1, 'NCC/NSS' : 1 }
        credits = 29

    elif sem == 5:
        subjects = { 'Algorithms Design & Analysis' : 4, 'Software Engineering' : 4, 'Java Programming' : 4, 'Industrial Management' : 3, 'Digital Communication' : 4, 'Communication Skills for Professionals' : 1 }
        labs = { 'Algorithms Design and Anaalysis Lab' : 1, 'Software Engineering Lab' : 1, 'Java Programming Lab' : 1, 'In-house Workshop' : 1, 'Digital Communication Lab' : 1, 'Communication Skills for Professionals Lab' : 1 }
        credits = 26

    elif sem == 6:
        subjects = { 'Compiler Design' : 4, 'Operating Systems' : 4, 'Computer Networks' : 4, 'Web Engineering' : 3, 'Artificial Intelligence' : 4, 'Microprocessors & Microcontrollers' : 4, }
        labs = { 'Operating Systems Lab' : 1, 'Computer Networks Lab' : 1, 'Web Engineering Lab' : 1, 'Microprocessor & Microcontroller Lab' : 1 }
        credits = 27

    elif sem == 7:
        elective1=st.selectbox('Select your 1st elective subject from Group A',('Complexicity Theory', 'Intellectual Property Rights', 'Embdedded Systems', 'Data Mining and Business Intelligence', 'Advanced Computer Architecure', 'Natural Language Processing'))
        elective2=st.selectbox('Select your 2nd elective subject from Group B', ('Digital Signal Processing', 'Simulation and Modelling', 'Advanced DBMS', 'Parallel Computing', 'Advanced Computer Networks', 'Control System', 'Sociology and Elements of Indian History for Engineers'))
        subjects = {'Information Security' : 4, 'Software Testing and Quality Assurance' : 3, 'Wireless Communication' : 3, elective1 : 3, elective2 : 3}
        labs = {'Information Security Lab' : 1, 'Software Testing and QA Lab' : 1, 'Wireless Communication Lab' : 1, 'Lab based on elective 1 or 2' : 1, 'Minor Project': 3}
        credits = 24
        
    elif sem == 8:
        elective1=st.selectbox('Select your 1st elective subject from Group A',('Digital Image Processing','Microelectronics','Ad Hoc and Sensor Networks','Soft Computing','VLSI Design','Distributed Systems','Object Oriented Software Engineering','Computer Vision','Software Project Management'))
        elective2=st.selectbox('Select your 2nd elective subject from Group B',('Human Computer Interaction','Information Theory and Coding','Web Intelligence and Big Data','Service Oriented Architecture','Multiagent Systems','Principles of Programming Languages','Telecommunication Networks','Selected Topics of Recent Trends in Computer Science and Engineering'))
        subjects = {'Mobile Computing' : 4, 'Machine Learning' : 3, 'Human Values and Professional Ethics II' : 1, elective1 : 3, elective2 : 3}
        labs = {'Mobile Computing Lab' : 1, 'Machine Learning Lab' : 1, 'Lab based on elective 1' : 1, 'Lab based on elective 2' : 2, 'Major Project' : 8}
        credits = 26

    with col1:
        with st.expander("Theory Subjects"):
            total_theory=0
            for subject in subjects:
                marks = st.number_input("{}:".format( subject ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * subjects[subject]
                theory_marks.append(marks)
                total_theory+=marks

    with col2:
        with st.expander("Practical Subjects"):
            total_lab=0
            for lab in labs:
                marks = st.number_input("{}:".format( lab ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * labs[lab]
                lab_marks.append(marks)
                total_lab+=marks

    if flag:
        st.warning("You haven't entered the marks of all subjects!")

    theory_subjects=[]
    for i in subjects.keys():
        theory_subjects.append(i)
    theory_subjects.append("Total")
    

    lab_subjects=[]
    for i in labs.keys():
        lab_subjects.append(i)
    lab_subjects.append("Total")

    theory_marks.append(total_theory)
    lab_marks.append(total_lab)
    theory_dict={'Subject':theory_subjects,'Marks':theory_marks}
    lab_dict={"Lab":lab_subjects,'Marks':lab_marks}

    theory_table=pd.DataFrame(theory_dict)
    lab_table=pd.DataFrame(lab_dict)
    
    with col1:
        st.table(theory_table)
    with col2:
        st.table(lab_table)
    

    GPA = GPA / credits
    return GPA

    

st.markdown("<h1 style='text-align: center; color: red;'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Semester GPA Calculator of B.Tech(IT)</h3>", unsafe_allow_html=True)

with st.container():
    name = st.text_input("ENTER YOUR NAME")

    if name:
        st.write("Hello {}!".format(name))
        sem = st.number_input("ENTER YOUR SEMESTER", 0, 8)

        if sem:
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center; '>Enter Marks!</h3>", unsafe_allow_html=True)

            GPA = calc(sem)

            st.write("")
            st.write("")

            cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9) #just for formatting XD
            with cl5:
                ans = st.button("Submit")
                
            
            
    
            if ans:
                msg = "Your GPA: {}".format(str(round(GPA,2)))
                st.markdown(f"<h3 style='text-align: center; '>{msg}</h3>", unsafe_allow_html=True)
                if GPA >= 8.0 :
                    st.balloons()
                    st.balloons()
                    st.balloons()


