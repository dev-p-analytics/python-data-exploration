import pandas as pd
import matplotlib.pyplot as plt

origin_path = "\Python\intro_to_da\Assignment 2"
origin_data = pd.read_csv(origin_path)
origin_data.describe()