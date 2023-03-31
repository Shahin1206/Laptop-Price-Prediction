# Laptop Price Prediction

## Overview
This project is about predicting the price of laptops based on their specifications. The project uses a dataset of laptop specifications and prices, and uses machine learning algorithms to train a model that can predict the price of a laptop given its specifications.

## Dataset
The dataset used in this project can be found on [Kaggle][dataset]. The dataset contains the following features:

| Column | Description |
| ------ | ------ |
| Company | the brand of the laptop |
| Product | the name of the laptop |
|TypeName | the type of laptop (gaming, ultrabook, etc.) |
|Inches | the size of the screen in inches |
|ScreenResolution | the resolution of the screen |
|Cpu | the processor model |
|Ram | the amount of RAM in GB |
|Memory | the type of storage and its size |
|Gpu | the graphics card model |
|OpSys | the operating system of the laptop |
|Weight | the weight of the laptop |
|Price | the price of the laptop (the price has been converted to INR in the output of the project) |



## Requirements
The project requires the following libraries:
- pandas
- numpy
- scikit-learn
- streamlit

You can install these libraries using pip:

``` pip install pandas ```

``` pip install numpy ```

``` pip install scikit-learn ```



## Usage
To run the project, you can use the app.py script. 

To run the script, you can use the following command:

``` streamlit run app.py ```

The script outputs price predicted by machine learning model based on the specifications entered by the user.



## Conclusion
The project demonstrates how machine learning can be used to predict the price of laptops based on their specifications. 

[//]: # (These are reference links used in the body of this note)
[dataset]: <https://www.kaggle.com/datasets/muhammetvarl/laptop-price>
