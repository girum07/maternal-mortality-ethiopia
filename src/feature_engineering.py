def add_trend_features(df):
    df = df.copy()
    df["change"] = df["Value"].diff()
    df["year_gap"] = df["SurveyYear"].diff()
    df["rate_of_change"] = df["change"] / df["year_gap"]
    return df