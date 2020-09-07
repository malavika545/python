'''1.	Read mobile dataset using pandas, and preprocess it (fill null values).'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("mobile_cleaned-1549119762886.csv")
print(data.isnull().sum())
print(data.isnull().sum().sum())
print(data.describe())
data['weight']=data['weight'].fillna(data['weight'].mean())
data['stand_by_time']=data['stand_by_time'].fillna(data['stand_by_time'].mean())
data['no_of_reviews_in_gsmarena_in_week']=data['no_of_reviews_in_gsmarena_in_week'].fillna(data['no_of_reviews_in_gsmarena_in_week'].mean())
data['phone_height']=data['phone_height'].fillna(data['phone_height'].mean())
data['talk_time']=data['talk_time'].fillna(data['talk_time'].mean())
data['video_resolution']=data['video_resolution'].fillna(data['video_resolution'].mean())
data['primary_camera_resolution']=data['primary_camera_resolution'].fillna(data['primary_camera_resolution'].mean())
print(data.isnull().sum())
print(data.isnull().sum().sum())