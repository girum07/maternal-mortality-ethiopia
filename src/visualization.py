import matplotlib.pyplot as plt

def plot_trend(df, save_path=None):
    plt.plot(df["SurveyYear"], df["Value"])
    plt.title("Maternal Mortality Trend in Ethiopia")
    plt.xlabel("Year")
    plt.ylabel("Value")
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()