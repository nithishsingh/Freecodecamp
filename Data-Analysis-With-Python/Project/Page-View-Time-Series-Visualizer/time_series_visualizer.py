import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Step 1: Importing and setting index using Pandas
def import_data(file_path):
    data = pd.read_csv(file_path)
    data["date"] = pd.to_datetime(data["date"])
    data.set_index("date", inplace=True)
    return data


# Step 2: Cleaning the data
def clean_data(data):
    lower_bound = data["value"].quantile(0.025)
    upper_bound = data["value"].quantile(0.975)
    cleaned_data = data[(data["value"] >= lower_bound) & (data["value"] <= upper_bound)]
    return cleaned_data


# Step 3: Function to draw line plot
def draw_line_plot(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data["value"], color="red")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.grid(True)
    plt.savefig("line_plot.png")
    plt.show()


# Step 4: Function to draw bar plot
def draw_bar_plot(data):
    data["Year"] = data.index.year
    data["Month"] = data.index.strftime("%b")
    data["Month_num"] = data.index.month
    grouped = data.groupby(["Year", "Month_num", "Month"])["value"].mean().unstack()
    plt.figure(figsize=(10, 7))
    grouped.plot(kind="bar", stacked=False)
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
    plt.savefig("bar_plot.png")
    plt.show()


# Step 5: Function to draw box plots
def draw_box_plot(data):
    data.reset_index(inplace=True)
    data["Year"] = [d.year for d in data.date]
    data["Month"] = [d.strftime("%b") for d in data.date]

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x="Year", y="value", data=data, ax=axes[0])
    sns.boxplot(
        x="Month",
        y="value",
        data=data,
        ax=axes[1],
        order=[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
    )
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    plt.tight_layout()
    plt.savefig("box_plots.png")
    plt.show()


# Example usage
file_path = "fcc-forum-pageviews.csv"
data = import_data(file_path)
cleaned_data = clean_data(data)

draw_line_plot(cleaned_data)
draw_bar_plot(cleaned_data)
draw_box_plot(cleaned_data)
