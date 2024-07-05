import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_plots():
    # Load the data
    covid = pd.read_csv('USA Data.csv')
    covid = covid.loc[:, ~covid.columns.str.contains('^Unnamed')]


    # Distribution plot
    sns.displot(covid['Recovered per 1M'], kde=True)
    plt.title('Distribution of Recovered per 1M')
    plt.show()

    # Heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(covid.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

    #Pairplot
    sns.pairplot(covid)
    plt.title('Pairplot of COVID Data')
    plt.show()

    #histogram
    sns.histplot(data = covid, bins=30)
    plt.title('Histogram of Covid Data')
    plt.xlabel('Value (Bins)')
    plt.ylabel('Frequency (Count)')
    plt.show()

if __name__ == "__main__":
    create_plots()
