import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("laptop_price_pred_model.pkl", "rb"))
df = pickle.load(open("df_transformed.pkl", "rb"))
df_options = pickle.load(open("df_options.pkl", "rb"))
st.title("Laptop Price Predictor")

#company
company = st.selectbox("Which company's laptop would you like to purchase?", df_options['Company'].unique())

#type
typename = st.selectbox("What type of laptop are you looking for?", df_options['TypeName'].unique())

#ram
ram = st.selectbox("How many GB of RAM is needed?", df_options['Ram'].unique())
ram = int(ram)

#weight
weight = st.number_input("How many kgs should your laptop approximately weigh?")
weight = int(weight)

#touchscreen
touchscreen = st.selectbox("Touchscreen? Y/N", ['Yes','No'])
if touchscreen == 'Yes':
      touchscreen = 1
else:
      touchscreen = 0

#ips panel
ips = st.selectbox("Do you want IPS Display?", ['Yes','No'])
if ips == 'Yes':
      ips = 1
else:
      ips = 0

#screen size in inches
screen_size = st.number_input('Enter screen size [in inches]')
if screen_size == 0:
      screen_size = 14

# resolution
resolution = st.selectbox('Select Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu_brand = st.selectbox("Which processor do you need?", df_options['Cpu brand'].unique())

#hdd
hdd = st.number_input("How many GB of HDD is required?")
hdd = int(hdd)

#ssd
ssd = st.number_input("How many GB of SSD is required?")
ssd = int(ssd)

#gpu brand
gpu = st.selectbox("Which brand's GPU are you looking for in your laptop?", df_options['Gpu brand'].unique())

#os
os = st.selectbox("Which operating system will suit your needs best?", df_options['os'].unique())

#ppi calculation
X_res = int(resolution.split('x')[0])
Y_res = int(resolution.split('x')[1])
ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size


test = pd.DataFrame(columns=['Ram', 'Weight', 'Touchscreen', 'Ips', 'ppi', 'HDD', 'SSD','Company_Acer', 'Company_Apple', 'Company_Asus', 'Company_Chuwi','Company_Dell', 'Company_Fujitsu', 'Company_Google', 'Company_HP','Company_Huawei', 'Company_LG', 'Company_Lenovo', 'Company_MSI','Company_Mediacom', 'Company_Microsoft', 'Company_Razer','Company_Samsung', 'Company_Toshiba', 'Company_Vero', 'Company_Xiaomi','TypeName_2 in 1 Convertible', 'TypeName_Gaming', 'TypeName_Netbook','TypeName_Notebook', 'TypeName_Ultrabook', 'TypeName_Workstation','Cpu brand_AMD Processor', 'Cpu brand_Intel Core i3','Cpu brand_Intel Core i5', 'Cpu brand_Intel Core i7','Cpu brand_Other Intel Processor', 'Gpu brand_AMD', 'Gpu brand_Intel','Gpu brand_Nvidia', 'os_Mac', 'os_Others/No OS/Linux', 'os_Windows'])

# fill it with 0s
test.loc[0] = 0

# update relevant columns
test['Company_'+company] = 1
test['TypeName_'+typename] = 1
test['Ram'] = ram
test['Weight'] = weight
test['Touchscreen'] = touchscreen
test['Ips'] = ips
test['ppi'] = ppi
test['Cpu brand_'+cpu_brand] = 1
test['HDD'] = hdd
test['SSD'] = ssd
test['Gpu brand_'+gpu] = 1
test['os_'+os] = 1


if st.button('Predict'):
      prediction = model.predict(test)
      st.success(int(np.exp(prediction[0])))