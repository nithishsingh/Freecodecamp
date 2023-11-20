# Mean-Variance-Standard Deviation Calculator


This project contains a Python script that calculates the mean, variance, standard deviation, maximum, minimum, and sum of a 3x3 matrix using NumPy.

## Usage

1. Clone the repository or download the files to your local machine.

2. Ensure you have Python installed.

3. Install the necessary dependencies:

    ```bash
    pip install numpy
    ```

4. Run the `main.py` script to test the `calculate()` function:

    ```bash
    python main.py
    ```

## File Structure

- `mean_var_std.py`: Contains the `calculate()` function that computes statistics for a 3x3 matrix.
- `main.py`: Demonstrates the usage of the `calculate()` function with test cases.

## Functionality

The `calculate()` function takes a list of 9 numbers as input, converts it into a 3x3 matrix, and computes various statistics:

- Mean along rows, columns, and flattened matrix.
- Variance along rows, columns, and flattened matrix.
- Standard deviation along rows, columns, and flattened matrix.
- Maximum value along rows, columns, and flattened matrix.
- Minimum value along rows, columns, and flattened matrix.
- Sum along rows, columns, and flattened matrix.

## Testing

The project includes a `test_module.py` file containing unit tests for the `calculate()` function.

To run the tests:

```bash
python test_module.py
```


## Enhancements

* **Command-Line Interface:** Develop a CLI tool for user interaction and convenient matrix input/output.
* **Interactive Mode:** Implement an interactive mode that prompts users for matrix data and displays calculated statistics.
* **Data Visualization:** Integrate data visualization libraries to generate plots and charts for visual data representation.

## Contributions

Contributions are welcome! Feel free to fork the repository, make your changes, and submit pull requests.

