# Car Mileage Prediction Project

A comprehensive end-to-end data science project that predicts vehicle fuel efficiency using machine learning and deploys it as a modern web application.

## 🚗 Project Overview

This project demonstrates the complete data science pipeline from data collection to model deployment, inspired by the original car-mileage repository but using a different, more comprehensive dataset.

### Key Features
- **Advanced Machine Learning**: Random Forest Regressor with 90.5% accuracy (R² score)
- **Modern Web Interface**: Glassmorphic UI with smooth animations
- **Real-time Predictions**: Instant fuel efficiency calculations
- **Comprehensive Dataset**: 45,000+ vehicles from official U.S. government data
- **Cost Estimation**: Annual fuel cost projections

## 📊 Dataset

Instead of the original auto-mpg dataset, this project uses the comprehensive fuel economy dataset from the U.S. Department of Energy (fueleconomy.gov):

- **Source**: https://fueleconomy.gov/feg/download.shtml
- **Size**: 45,000+ vehicles
- **Time Range**: 1984-2026
- **Features**: Year, cylinders, displacement, drive type, transmission, fuel type, etc.

## 🛠️ Technology Stack

### Data Science
- **Python 3.11**
- **Pandas 2.0.3** - Data manipulation
- **NumPy 1.24.3** - Numerical operations
- **Scikit-Learn 1.3.0** - Machine learning
- **Matplotlib 3.7.2** - Data visualization
- **Seaborn 0.12.2** - Statistical visualization
- **Jupyter 1.0.0** - Data analysis notebooks

### Web Development
- **Django 4.2.4** - Web framework
- **HTML5/CSS3** - Frontend
- **JavaScript** - Interactive features
- **Glassmorphic Design** - Modern UI

## 📁 Project Structure

```
car-mileage-project/
├── data/
│   └── vehicles.csv              # Comprehensive fuel economy dataset
├── notebooks/
│   └── car_mileage_prediction.ipynb  # Complete data science pipeline
├── models/
│   └── car_mileage_rf_model.joblib  # Trained Random Forest model
├── webapp/
│   ├── carmileage/              # Django project
│   ├── prediction/              # Django app
│   ├── templates/              # HTML templates
│   └── static/                 # CSS/JS files
├── train_model.py              # Quick model training script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**
2. **Navigate to the project directory**
   ```bash
   cd car-mileage-project
   ```

3. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Train the machine learning model**
   ```bash
   python train_model.py
   ```
   
   This will:
   - Load and clean the dataset
   - Train a Random Forest model
   - Save the model to `models/car_mileage_rf_model.joblib`
   - Display model performance metrics

### Running the Web Application

1. **Navigate to the webapp directory**
   ```bash
   cd webapp
   ```

2. **Run Django migrations**
   ```bash
   python manage.py migrate
   ```

3. **Start the development server**
   ```bash
   python manage.py runserver
   ```

4. **Open your web browser** and go to:
   ```
   http://127.0.0.1:8000
   ```

## 📈 Model Performance

The Random Forest model achieves excellent performance metrics:

- **R² Score**: 0.9055 (explains 90.55% of variance)
- **RMSE**: 0.73 KMPL (1.72 MPG)
- **MAE**: 0.47 KMPL (1.10 MPG)

### Key Features Influencing Fuel Efficiency
1. **Engine Displacement** - Most important factor
2. **Number of Cylinders** - Inversely correlated with efficiency
3. **Fuel Type** - Different energy densities
4. **Drive Type** - AWD systems add complexity
5. **Vehicle Age** - Newer technologies improve efficiency

## 🎯 How to Use

1. **Enter Vehicle Specifications**:
   - Year of manufacture
   - Number of cylinders
   - Engine displacement (liters)
   - Drive type (FWD, RWD, AWD, etc.)
   - Transmission type
   - Fuel type

2. **Click "Predict Fuel Efficiency"** to get instant results

3. **View Results**:
   - Combined fuel efficiency in both KMPL and MPG
   - Estimated annual fuel cost (based on 15,000 miles/year)

## 🔬 Data Science Pipeline

### 1. Data Collection
- Downloaded comprehensive fuel economy dataset
- 45,000+ vehicles with detailed specifications

### 2. Exploratory Data Analysis
- Analyzed feature distributions
- Identified correlations between variables
- Visualized relationships between specifications and fuel efficiency

### 3. Data Cleaning & Preprocessing
- Removed missing values
- Filtered unrealistic measurements
- Encoded categorical variables
- Created derived features (car age)

### 4. Feature Engineering
- Label encoding for categorical variables
- Feature scaling (where needed)
- Car age calculation

### 5. Model Training
- Random Forest Regressor
- Hyperparameter tuning
- Cross-validation

### 6. Model Evaluation
- Performance metrics calculation
- Feature importance analysis
- Residual analysis

### 7. Deployment
- Django web application
- RESTful API endpoints
- Modern glassmorphic UI

## 🎨 Web Application Features

### User Interface
- **Glassmorphic Design**: Modern, translucent UI elements
- **Responsive Layout**: Works on all device sizes
- **Smooth Animations**: Interactive transitions
- **Real-time Feedback**: Loading states and error handling

### Technical Features
- **AJAX Predictions**: Asynchronous form submission
- **Dynamic Dropdowns**: Populated from actual dataset values
- **Error Handling**: Comprehensive error messages
- **Performance**: Optimized for speed

## 📚 Learning Objectives

This project demonstrates:
- **Complete Data Science Workflow**: From raw data to deployment
- **Machine Learning**: Random Forest regression
- **Web Development**: Django framework
- **Modern UI Design**: Glassmorphic effects
- **API Development**: RESTful endpoints
- **Data Visualization**: Exploratory analysis

## 🔧 Customization

### Adding New Features
1. **Update the model**: Modify `train_model.py` or the Jupyter notebook
2. **Retrain the model**: Run `python train_model.py`
3. **Update the web interface**: Modify templates in `webapp/templates/`

### Using Different Datasets
1. **Replace the dataset**: Update `data/vehicles.csv`
2. **Adjust feature columns**: Update the training script
3. **Retrain the model**: Follow the training process

## 🐛 Troubleshooting

### Common Issues

1. **Model not found error**:
   - Ensure you've run `python train_model.py`
   - Check that `models/car_mileage_rf_model.joblib` exists

2. **Django server won't start**:
   - Ensure all dependencies are installed
   - Check that virtual environment is activated

3. **Prediction errors**:
   - Verify all form fields are filled
   - Check that selected values exist in the training data

### Getting Help

1. **Check the logs**: Django provides detailed error messages
2. **Verify data**: Ensure the dataset is properly loaded
3. **Test the model**: Run the training script to verify model performance

## 📄 License

This project is for educational purposes, demonstrating data science and web development skills.

## 🙏 Acknowledgments

- **U.S. Department of Energy**: For providing the comprehensive fuel economy dataset
- **Original Repository**: Inspiration from Balagangadhar-Dev/car-mileage
- **Scikit-Learn**: Machine learning library
- **Django**: Web framework

---

**Project Status**: ✅ Complete and Functional

The web application is fully functional with a trained machine learning model providing accurate fuel efficiency predictions. Users can input vehicle specifications and receive instant predictions with cost estimates.
