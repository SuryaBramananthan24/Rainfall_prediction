# Rainfall Prediction Project

This repository contains code and resources for predicting rainfall using machine learning techniques.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Rainfall prediction is crucial for various applications, including agriculture, water resource management, and disaster preparedness. This project aims to develop machine learning models that predict rainfall based on historical weather data.

## Dataset
The dataset used for this project is sourced from [Global Historical Climatology Network - Daily (GHCN-D)](https://www.ncdc.noaa.gov/ghcn-daily-description). It consists of historical weather data with features such as temperature, humidity, wind speed, and previous rainfall measurements. The target variable is the amount of rainfall (in millimeters) recorded at specific time intervals.

- **Dataset Details**:
  - **Source**: [Global Historical Climatology Network - Daily (GHCN-D)](https://www.ncdc.noaa.gov/ghcn-daily-description)
  - **Features**: Temperature, Humidity, Wind Speed, Previous Rainfall
  - **Target Variable**: Rainfall (mm)
  - **Data Size**: Approximately 100,000 instances with 15 features

## Installation
To run the code in this repository, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/SuryaBramananthan24/rainfall-prediction.git
   cd rainfall-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To train a rainfall prediction model and make predictions:

1. Ensure you have Python and necessary dependencies installed (see Installation section).
2. Prepare your dataset in CSV format (`data.csv`).
3. Run the script to train and evaluate the model:
   ```bash
   python Rainfall_prediction.py --data data.csv
   ```
   
## Models
We experimented with several machine learning models for rainfall prediction, including:

- Linear Regression
- Random Forest
- Gradient Boosting

Each model was evaluated based on metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).


## Contributing
Contributions to this project are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Done By
- [Surya B](https://github.com/SuryaBramananthan24) 
