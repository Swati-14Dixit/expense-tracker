# Expense Tracker & Analyzer

A professional-grade expense tracking and analysis system designed to help individuals and small businesses monitor their spending patterns, detect anomalies, and maintain budget discipline. This application provides dual interfaces - a modern web dashboard and a lightweight command-line tool - to accommodate different user preferences and workflows.

## Why I Built This Tracker

I created this expense tracker to solve the common challenges of personal finance management:
- **Lack of visibility** into spending patterns and trends
- **Difficulty identifying** unusual or excessive expenses
- **Manual budget tracking** that's time-consuming and error-prone
- **Limited analytics** in most basic expense tracking tools

This application combines machine learning-powered anomaly detection with intuitive visualizations to provide actionable insights into your financial habits.

## What It Does

- **📊 Comprehensive Tracking**: Monitor expenses across multiple categories with detailed analytics
- **🤖 Smart Detection**: Uses Isolation Forest algorithm to identify unusual spending patterns
- **📈 Visual Analytics**: Interactive charts and graphs for better financial insights  
- **💰 Budget Management**: Real-time budget tracking with daily spending recommendations
- **🔄 Dual Interfaces**: Choose between web dashboard or command-line for flexibility
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

## Features

### Web Interface (Streamlit)
- 📊 Interactive dashboard with visualizations
- 📈 Real-time expense tracking and analysis
- 🎯 Anomaly detection using machine learning
- 📱 Responsive design for mobile and desktop
- 💰 Budget management and forecasting
- 📋 Expense categorization with emojis

### Command-Line Interface
- ➕ Add expenses quickly via terminal
- 📊 View expense summaries by category
- 💵 Budget tracking and daily budget calculation
- 🗂️ Simple CSV-based data storage

## Professional Setup & Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment recommended

### Step-by-Step Installation

1. **Clone or Download the Project**
   ```bash
   # If using git
   git clone <repository-url>
   cd expense_tracker
   
   # Or download and extract the project files
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**
   ```bash
   python -c "import streamlit; import pandas; print('Dependencies installed successfully')"
   ```

## Professional Usage Guide

### Web Interface (Recommended for Full Features)

1. **Start the Application**
   ```bash
   streamlit run app.py
   ```

2. **Access the Dashboard**
   - Open your browser and navigate to `http://localhost:8501`
   - The application will automatically load with sample data

3. **Key Features to Explore:**
   - **Dashboard Overview**: View total expenses, remaining budget, and daily allowance
   - **Upload Data**: Use the sidebar to upload your own CSV file or use the sample data
   - **Add Expenses**: Use the form in the sidebar to add new expenses in real-time
   - **Visual Analytics**: Explore pie charts, time series, and budget visualizations
   - **Anomaly Detection**: Review highlighted unusual expenses for investigation

4. **Data Management**
   - Export your data anytime using the CSV download functionality
   - Set custom monthly budgets based on your financial goals

### Command-Line Interface (For Quick Operations)

1. **Run the CLI Application**
   ```bash
   python expense_tracker.py
   ```

2. **Follow the Interactive Prompts:**
   - Enter expense name and amount
   - Select from predefined categories
   - View immediate summary of your spending

3. **CLI Advantages:**
   - Faster data entry for power users
   - Scriptable for automation
   - Lightweight operation without browser overhead

## Professional Architecture

### File Structure
```
expense_tracker/
├── app.py                 # Main Streamlit web application
├── expense_tracker.py     # Command-line interface  
├── expense.py            # Expense class definition (data model)
├── expenses.csv          # Sample expense data for demonstration
├── requirements.txt      # Python dependencies
└── README.md            # This documentation
```

### Technical Architecture
- **Frontend**: Streamlit for responsive web interface
- **Backend**: Pure Python with pandas for data processing
- **Machine Learning**: Scikit-learn for anomaly detection
- **Data Storage**: CSV-based for simplicity and portability
- **Visualization**: Plotly for interactive charts and graphs

## Professional Dependencies

### Core Dependencies
- **pandas >=1.5.0** - Data manipulation and analysis
- **numpy >=1.24.0** - Numerical computing foundation
- **streamlit >=1.22.0** - Web application framework

### Visualization & Analytics
- **plotly >=5.13.0** - Interactive visualizations
- **matplotlib >=3.7.0** - Static plotting backend
- **seaborn >=0.12.0** - Statistical data visualization

### Machine Learning
- **scikit-learn >=1.2.0** - Anomaly detection algorithms

### Development & Testing
- Virtual environment tools
- Git for version control

## Professional Data Management

### Data Format Specification
Expenses are stored in `expenses.csv` with a standardized format:
```
expense_name,amount,category
```

### Example Data
```
Coffee,4.50,☕️ Cafe
Groceries,85.30,🍔 Food
Internet Bill,79.99,🏠 Home
Conference Ticket,299.00,📅 Work
```

### Data Integrity Features
- Automatic data validation and cleaning
- Type checking for amount fields
- Date tracking for temporal analysis
- Category validation against predefined list

## Professional Expense Categories

### Standardized Categories
- **🍔 Food** - Groceries, restaurants, dining
- **🏠 Home** - Rent, utilities, maintenance  
- **📅 Work** - Business expenses, office supplies
- **🥳 Fun** - Entertainment, hobbies, leisure
- **⚽️ Games** - Gaming, sports, activities
- **👗 Dress** - Clothing, accessories, personal care
- **☕️ Cafe** - Coffee shops, beverages
- **✈️ Travel** - Transportation, trips, commuting

### Category Benefits
- Consistent classification for accurate analytics
- Emoji-based visual identification
- Customizable through code modification

## Advanced Features

### Web Dashboard Capabilities

**Real-time Analytics**
- Live expense tracking with instant updates
- Monthly budget progress monitoring
- Daily spending allowance calculations
- Category-wise spending breakdowns

**Machine Learning Integration**
- **Isolation Forest Algorithm**: Detects anomalous expenses
- **Automatic Flagging**: Highlights unusual spending patterns
- **Configurable Sensitivity**: Adjustable anomaly detection thresholds

**Interactive Visualizations**
- **Pie Charts**: Category distribution analysis
- **Time Series**: Spending trends over time
- **Budget Tracking**: Visual budget utilization
- **Responsive Design**: Optimized for all device sizes

**Data Management**
- CSV file upload/download functionality
- Real-time data validation
- Persistent storage with automatic backups

### CLI Interface Advantages

**Efficiency Features**
- Rapid data entry without GUI overhead
- Keyboard-only operation for power users
- Scriptable for batch processing
- Lightweight resource usage

**Professional Workflow**
- Immediate expense summarization
- Budget status at a glance
- Portable operation (no internet required)
- Integration with other tools via stdout

## Professional Deployment

### Production Considerations
- Use dedicated virtual environment
- Regular data backups recommended
- Consider database migration for large datasets
- Cloud deployment options available via Streamlit Cloud

### Performance Optimization
- Efficient pandas operations for large datasets
- Caching mechanisms for improved responsiveness
- Optimized ML model training for anomaly detection

## Contributing & Customization

### Extending Functionality
- Add new expense categories in the category lists
- Modify anomaly detection sensitivity parameters
- Integrate with external APIs (banking, accounting software)
- Add user authentication and multi-user support

### Professional Development
- Follow PEP 8 coding standards
- Use type hints for better code quality
- Implement comprehensive testing suite
- Document all changes thoroughly

## License & Support

This project is open source and available under the MIT License. For professional support or customization services, please contact the development team.

---

**Built with ❤️ for better financial management and data-driven decision making.**
