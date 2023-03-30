Laptop Price Prediction

Overview
This project is about predicting the price of laptops based on their specifications. The project uses a dataset of laptop specifications and prices, and uses machine learning algorithms to train a model that can predict the price of a laptop given its specifications.



Dataset
The dataset used in this project can be found on Kaggle. The dataset contains the following features:
Company: the brand of the laptop
Product: the name of the laptop
TypeName: the type of laptop (gaming, ultrabook, etc.)
Inches: the size of the screen in inches
ScreenResolution: the resolution of the screen
Cpu: the processor model
Ram: the amount of RAM in GB
Memory: the type of storage and its size
Gpu: the graphics card model
OpSys: the operating system of the laptop
Weight: the weight of the laptop
Price: the price of the laptop in euros



Requirements
The project requires the following libraries:
pandas
scikit-learn
streamlit
You can install these libraries using pip:
pip install pandas scikit-learn



Usage
To run the project, you can use the app.py script. 

To run the script, you can use the following command:
streamlit run app.py
The script outputs price predicted by machine learning model based on the specifications entered by the user.



Conclusion
The project demonstrates how machine learning can be used to predict the price of laptops based on their specifications. The model achieves a low error rate, which suggests that it can be useful for predicting laptop prices in practice.