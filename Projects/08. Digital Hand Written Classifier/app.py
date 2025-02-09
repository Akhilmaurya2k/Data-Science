import numpy as np
import PIL
from pickle import load
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

knn_classifier = load(open('models/knn_model.pkl', 'rb'))
lr_classifier = load(open('models/lr_model.pkl', 'rb'))
sv_classifier = load(open('models/sv_model.pkl', 'rb'))
dt_classifier = load(open('models/dt_model.pkl', 'rb'))
rf_classifier = load(open('models/rf_model.pkl', 'rb'))

import streamlit as st
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

st.title("Digital Hand written classifier")

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:
    st.image(image_file, width=250)
    photos = Image.open(image_file)
    #photos = photos.thumbnail((28,28))
    photos_gray_0 = photos.convert("L")
    photos_gray_0 = photos_gray_0.resize((28,28))
    photos_arr_0 = np.array(photos_gray_0)

    option = st.selectbox('Which model do you what to use?',('Support vector classifier','KNN', 'LogisticRegression' ,'decision Tree','RandomForestClassifier'))
    st.write('You selected:', option)

    btn_click = st.button('predict')

    if option == 'KNN':
        if btn_click == True:
            prediction = knn_classifier.predict([photos_arr_0.ravel()])
            st.text('The number is :')
            st.title(prediction[0])
    if option == 'LogisticRegression':
        if btn_click == True:
            prediction = lr_classifier.predict([photos_arr_0.ravel()])
            st.text('The number is :')
            st.title(prediction[0])
    if option == 'Support vector classifier':
        if btn_click == True:
            prediction = sv_classifier.predict([photos_arr_0.ravel()])
            st.text('The number is :')
            st.title(prediction[0])
    if option == 'decision Tree':
        if btn_click == True:
            prediction = dt_classifier.predict([photos_arr_0.ravel()])
            st.text('The number is :')
            st.title(prediction[0])
    if option == 'RandomForestClassifier':
        if btn_click == True:
            prediction = rf_classifier.predict([photos_arr_0.ravel()])
            st.text('The number is :')
            st.title(prediction[0])
