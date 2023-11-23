# Page View Time Series Visualizer

# Data Visualization Project: freeCodeCamp Forum Page Views

This project aims to visualize time series data regarding the number of page views on the freeCodeCamp.org forum from May 9, 2016, to December 3, 2019. The visualizations generated using Pandas, Matplotlib, and Seaborn provide insights into the patterns in visits and highlight yearly and monthly growth.

## Project Overview

- **Tools Used**: Pandas, Matplotlib, Seaborn
- **Data Source**: "fcc-forum-pageviews.csv"
- **Visualization Types**:
  - Line chart depicting daily page views
  - Bar chart showcasing average daily page views per month grouped by year
  - Box plots illustrating data distribution within a given year or month and its comparison over time

## Tasks

1. **Data Processing**
   - Imported the dataset using Pandas
   - Cleaned the data by filtering out extreme values

2. **Visualization Functions**
   - `draw_line_plot`: Generates a line chart to display daily page views.
   - `draw_bar_plot`: Creates a bar chart showing average daily page views per month grouped by year.
   - `draw_box_plot`: Produces box plots indicating data distribution within a year or month and its trend.

## Files Included

- `fcc-forum-pageviews.csv`: Dataset containing page views data.
- `main.py`: File to execute and test the visualization functions.
- `test_module.py`: Unit tests to validate the functions.
- `README.md`: Documentation file providing an overview, instructions, and details about the project.

## Instructions for Development and Testing

1. **Development**: Modify and test your functions in `main.py`.
2. **Testing**: Run `main.py` to execute the visualization functions. Unit tests are included in `test_module.py`.

## Usage

To generate visualizations and test the functions:

1. Ensure necessary libraries (Pandas, Matplotlib, Seaborn) are installed.
2. Run `main.py` in your Python environment.

## Submission

Upon completion, submit the project's URL to freeCodeCamp for evaluation.

Feel free to modify, improve, or expand upon this project as needed.
