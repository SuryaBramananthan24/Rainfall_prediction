import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Rainfall_Data_LL.csv'  
rainfall_data = pd.read_csv(file_path)
state = 'Tamil Nadu'
state_data=rainfall_data[rainfall_data['SUBDIVISION']==state]

X = state_data[['YEAR']]
y = state_data['ANNUAL']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train ,y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate MSE and R-squared score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared Score: {r2}')

# Plot actual vs predicted
plt.figure(figsize=(10, 6))
plt.bar(X_test['YEAR'], y_test, width=8 ,label='Actual',color='blue',edgecolor='black')
plt.plot(X_test['YEAR'], y_pred, linewidth=4, label='Predicted',color='red')
plt.ylabel('Annual Rainfall of Tamil Nadu')# Assuming the dataset has columns 'YEAR' and 'ANNUAL'
plt.xlabel('YEAR')
plt.title('Actual vs Predicted Annual Rainfall')
plt.legend()
plt.show()
