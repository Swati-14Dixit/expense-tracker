import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import calendar
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Set page configuration
st.set_page_config(
    page_title="Expense Tracker & Analyzer",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2E86AB;
        margin-bottom: 1rem;
    }
    .expense-table {
        width: 100%;
        border-collapse: collapse;
    }
    .expense-table th {
        background-color: #2E86AB;
        color: white;
        padding: 12px;
        text-align: left;
    }
    .expense-table tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    .expense-table tr:hover {
        background-color: #e9ecef;
    }
    .anomaly {
        background-color: #ffcccc !important;
    }
</style>
""", unsafe_allow_html=True)

class ExpenseTracker:
    def __init__(self):
        self.df = None
        self.budget = 2000  # Default monthly budget
        
    def load_data(self, file_path="expenses.csv"):
        """Load expense data from CSV file"""
        try:
            self.df = pd.read_csv(file_path, names=['name', 'amount', 'category'], header=None)
            self.df['date'] = pd.date_range(end=datetime.now(), periods=len(self.df), freq='D')
            self.df['amount'] = pd.to_numeric(self.df['amount'], errors='coerce')
            self.df = self.df.dropna()
            return True
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return False
    
    def process_data(self):
        """Process and clean the data"""
        if self.df is None:
            return
        
        # Ensure proper data types
        self.df['amount'] = pd.to_numeric(self.df['amount'])
        self.df['date'] = pd.to_datetime(self.df['date'])
        
        # Add month and year columns for grouping
        self.df['month'] = self.df['date'].dt.month
        self.df['year'] = self.df['date'].dt.year
        self.df['day'] = self.df['date'].dt.day
        
    def calculate_statistics(self):
        """Calculate key statistics"""
        if self.df is None:
            return {}
        
        total_expenses = self.df['amount'].sum()
        now = datetime.now()
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        remaining_days = days_in_month - now.day
        remaining_budget = self.budget - total_expenses
        daily_budget = remaining_budget / remaining_days if remaining_days > 0 else 0
        
        # Category totals
        category_totals = self.df.groupby('category')['amount'].sum().sort_values(ascending=False)
        
        return {
            'total_expenses': total_expenses,
            'remaining_budget': remaining_budget,
            'remaining_days': remaining_days,
            'daily_budget': daily_budget,
            'category_totals': category_totals
        }
    
    def detect_anomalies(self):
        """Detect anomalous expenses using Isolation Forest"""
        if self.df is None or len(self.df) < 10:
            return pd.Series([False] * len(self.df))
        
        # Use amount and day of month as features
        X = self.df[['amount', 'day']].values
        clf = IsolationForest(contamination=0.1, random_state=42)
        anomalies = clf.fit_predict(X)
        
        # Convert to boolean (1 = normal, -1 = anomaly)
        return anomalies == -1
    
    def create_pie_chart(self):
        """Create pie chart of expenses by category"""
        if self.df is None:
            return None
        
        category_totals = self.df.groupby('category')['amount'].sum()
        fig = px.pie(
            values=category_totals.values,
            names=category_totals.index,
            title="Expenses by Category",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        return fig
    
    def create_time_series_chart(self):
        """Create time series chart of expenses over time"""
        if self.df is None:
            return None
        
        daily_expenses = self.df.groupby('date')['amount'].sum().reset_index()
        fig = px.line(
            daily_expenses,
            x='date',
            y='amount',
            title="Daily Expenses Over Time",
            labels={'amount': 'Amount ($)', 'date': 'Date'}
        )
        fig.update_traces(line=dict(color='#2E86AB', width=3))
        return fig
    
    def create_budget_visualization(self):
        """Create animated budget visualization"""
        if self.df is None:
            return None
        
        # Calculate cumulative expenses by day
        self.df = self.df.sort_values('date')
        self.df['cumulative'] = self.df['amount'].cumsum()
        self.df['budget_remaining'] = self.budget - self.df['cumulative']
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=self.df['date'],
            y=self.df['cumulative'],
            mode='lines+markers',
            name='Cumulative Expenses',
            line=dict(color='#FF6B6B', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=self.df['date'],
            y=[self.budget] * len(self.df),
            mode='lines',
            name='Total Budget',
            line=dict(color='#4ECDC4', width=2, dash='dash')
        ))
        
        fig.update_layout(
            title="Budget Usage Through the Month",
            xaxis_title="Date",
            yaxis_title="Amount ($)",
            hovermode='x unified'
        )
        
        return fig

def main():
    st.markdown('<h1 class="main-header">💰 Expense Tracker & Analyzer</h1>', unsafe_allow_html=True)
    
    # Initialize tracker
    tracker = ExpenseTracker()
    
    # Sidebar for user inputs
    with st.sidebar:
        st.header("📊 Dashboard Controls")
        
        # File upload
        uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
        if uploaded_file is not None:
            # Read uploaded file
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            tracker.df = pd.read_csv(stringio, names=['name', 'amount', 'category'], header=None)
            tracker.df['date'] = pd.date_range(end=datetime.now(), periods=len(tracker.df), freq='D')
        else:
            # Load default data
            tracker.load_data()
        
        # Budget input
        tracker.budget = st.number_input(
            "Monthly Budget ($)",
            min_value=0,
            max_value=10000,
            value=2000,
            step=100
        )
        
        # Add new expense form
        st.header("➕ Add New Expense")
        with st.form("expense_form"):
            name = st.text_input("Expense Name")
            amount = st.number_input("Amount ($)", min_value=0.0, step=0.01)
            category = st.selectbox(
                "Category",
                ["🍔 Food", "🏠 Home", "📅 Work", "🥳 Fun", "⚽️ Games", "👗 Dress", "☕️ Cafe", "✈️ Travel"]
            )
            submitted = st.form_submit_button("Add Expense")
            
            if submitted and name and amount > 0:
                new_expense = pd.DataFrame({
                    'name': [name],
                    'amount': [amount],
                    'category': [category],
                    'date': [datetime.now()]
                })
                if tracker.df is None:
                    tracker.df = new_expense
                else:
                    tracker.df = pd.concat([tracker.df, new_expense], ignore_index=True)
                st.success("Expense added successfully!")
    
    # Process data
    if tracker.df is not None:
        tracker.process_data()
        
        # Calculate statistics
        stats = tracker.calculate_statistics()
        
        # Detect anomalies
        anomalies = tracker.detect_anomalies()
        tracker.df['anomaly'] = anomalies
        
        # Remove metric cards
        if stats:
            st.write(f"Total Expenses: ${stats['total_expenses']:,.2f}")
            st.write(f"Budget Remaining: ${stats['remaining_budget']:,.2f}")
            st.write(f"Days Remaining: {stats['remaining_days']}")
            st.write(f"Daily Budget: ${stats['daily_budget']:,.2f}")
        
        # Display charts
        col1, col2 = st.columns(2)
        
        with col1:
            pie_chart = tracker.create_pie_chart()
            if pie_chart:
                st.plotly_chart(pie_chart, use_container_width=True)
        
        with col2:
            time_series = tracker.create_time_series_chart()
            if time_series:
                st.plotly_chart(time_series, use_container_width=True)
        
        # Budget visualization
        budget_viz = tracker.create_budget_visualization()
        if budget_viz:
            st.plotly_chart(budget_viz, use_container_width=True)
        
        # Display expense table with anomalies highlighted
        st.header("📋 Expense Details")
        if anomalies.any():
            st.warning("⚠️ Anomalies detected in your expenses (highlighted in red)")
        
        # Style the dataframe
        def highlight_anomalies(row):
            if row['anomaly']:
                return ['background-color: #ffcccc'] * len(row)
            else:
                return [''] * len(row)
        
        display_df = tracker.df.copy()
        display_df = display_df[['date', 'name', 'category', 'amount', 'anomaly']]
        display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
        display_df = display_df.sort_values('date', ascending=False)
        
        styled_df = display_df.style.apply(highlight_anomalies, axis=1)
        st.dataframe(styled_df, use_container_width=True)
        
        # Category breakdown
        st.header("📊 Category Breakdown")
        category_df = pd.DataFrame({
            'Category': stats['category_totals'].index,
            'Amount': stats['category_totals'].values
        })
        st.dataframe(category_df, use_container_width=True)
    
    else:
        st.info("Please upload a CSV file or use the sample data to get started.")

if __name__ == "__main__":
    main()
