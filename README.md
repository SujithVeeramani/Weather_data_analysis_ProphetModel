# Weather data analysis by Prophet Model
This repository hosts a web application built with FastAPI for time series data analysis and forecasting using the Prophet model. Users can upload CSV files, select relevant columns, and visualize predictions through an interactive web interface. The application leverages Matplotlib for result visualization, creating a dynamic and user-friendly experience.

## Key Features:
### File Upload and Processing: 
Easily upload time series data in CSV format and select specific columns for analysis.
### Prophet Model Forecasting: 
Utilizes the Prophet model to generate forecasts with daily resampling for a future period of 730 days.
### Interactive Web Interface:  
User-friendly interface for exploring processed data and visualizing forecasting results.

## Instructions:
- Clone the repository:
  ```bash
  git clone https://github.com/SujithVeeramani/Weather_data_analysis_ProphetModel
  cd Weather_data_analysis_ProphetModel
- Install Dependencies:
  ```bash
  pip install prophet fastapi uvicorn pandas matplotlib scipy seaborn plotly
- Run the Application:
  ```bash
  uvicorn upload:app --reload
-Access the Web Interface:
Open your browser and go to http://127.0.0.1:8000 to interact with the time series forecasting application

Feel free to explore, analyze, and visualize your weather data effortlessly with this application!

## Contact me
### Have any issues while using this? Feel free to contact me

- LinkedIN  - https://www.linkedin.com/in/sujithvl/
- Instagram - https://www.instagram.com/sujith_vl_/
