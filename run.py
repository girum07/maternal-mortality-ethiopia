from src.data_cleaning import load_data, filter_indicator
from src.analysis import compute_trend
from src.visualization import plot_trend

# Load dataset
df = load_data("/home/the-g/Desktop/maternal-mortality-ethiopi/data/raw/Maternal_mortality_national_eth.csv")

# Filter indicator
df = filter_indicator(
    df,
    "Pregnancy-related mortality rate"
)

# Compute trend metrics
df = compute_trend(df)
# Print results
print(df)

# Generate visualization
plot_trend(
    df,
    save_path="outputs/figures/trend_plot.png"
)