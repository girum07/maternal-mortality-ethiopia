📊 Maternal Mortality Trend in Ethiopia (DHS/HDX Data Analysis)
🎯 Objective

This project analyzes the trend of maternal mortality in Ethiopia using DHS/HDX survey data to understand how maternal mortality has changed over time and whether the observed trend is statistically consistent across survey periods.

The goal is not just visualization, but structured trend extraction from raw demographic health data.

🧠 Research Question
How has maternal mortality in Ethiopia changed across survey years?
What is the rate of change between survey periods?
Is the observed decline consistent or irregular across time gaps?

📦 Dataset
Source: DHS / HDX (Demographic and Health Surveys)
Country: Ethiopia (ISO3: ETH)
Indicators used:
Pregnancy-related mortality rate
Number of pregnancy-related deaths
Exposure years to risk population

🧪 Methodology
1. Data Cleaning
Loaded raw DHS dataset using Pandas
Filtered relevant indicator:
Pregnancy-related mortality rate
Removed irrelevant characteristics and missing values
Standardized survey year format
2. Feature Engineering

Computed temporal trend features:

year_gap → difference between survey years
change → absolute difference in mortality values
rate_of_change → normalized change per year gap
3. Trend Analysis
Time series reconstruction across survey points
Comparison of mortality values across years
Directional trend detection (increase vs decrease)
4. Visualization
Line plot of maternal mortality over time
Annotated trend slope
Saved output plots to /outputs/figures/

📉 Key Findings
Maternal mortality shows a general downward trend
Decline is not linear (variation across survey intervals)
Rate of decrease differs significantly between early and later periods

🧱 Project Structure
maternal-mortality-ethiopia/
│
├── data/
│   ├── raw/                  # Original DHS/HDX dataset
│   └── processed/           # Cleaned dataset (optional)
│
├── notebooks/
│   └── o1_maternal_mortality_report.ipynb   # Full analysis notebook
│
├── src/
│   ├── data_cleaning.py     # Loading + filtering logic
│   ├── analysis.py          # Trend computation functions
│   └── visualization.py     # Plotting functions
│
├── outputs/
│   └── figures/
│       └── trend_plot.png   # Final visualization output
│
├── run.py                  # Pipeline runner (end-to-end execution)
├── requirements.txt
└── README.md

⚙️ How to Run This Project
1. Clone repo
   git clone https://github.com/<your-username>/maternal-mortality-ethiopia.git
   cd maternal-mortality-ethiopia
2. Create virtual environment
   python3 -m venv .venv
   source .venv/bin/activate
3. Install dependencies
   pip install -r requirements.txt
4. Run full pipeline
   python run.py
   Or open notebook:
   jupyter notebook

📊 Output
Clean trend dataset
Computed rate-of-change metrics
Visualization saved to:
outputs/figures/trend_plot.png

🧠 Technical Stack
Python
Pandas (data wrangling)
Matplotlib (visualization)
Jupyter Notebook (exploration)

🚧 Limitations
Only survey-based (not continuous yearly data)
Small number of time points reduces statistical power
External socio-economic factors not included

🔭 Future Improvements
Compare Ethiopia vs regional countries
Build interactive dashboard (Streamlit)

🧾 License

Educational
