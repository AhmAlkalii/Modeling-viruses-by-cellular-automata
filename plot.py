import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_plots():
    # Load the data
    covid = pd.read_csv('USA Data.csv')

    # Distribution plot
    sns.displot(covid['Recovered per 1M'], kde=True)
    plt.title('Distribution of Recovered per 1M')
    plt.show()

    # Heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(covid.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

    # Pairplot
    sns.pairplot(covid)
    plt.title('Pairplot of COVID Data')
    plt.show()

if __name__ == "__main__":
    create_plots()
