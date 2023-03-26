"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.7
"""
import pandas as pd

def preprocess_iris(iris: pd.DataFrame) -> pd.DataFrame:
	"""
	Preprocessing the data for Iris dataset.

	Args:
	    iris: Raw data.
	Returns:
	    Preprocessed data with reformatted 
	    attribute names
	"""
	iris = iris.set_index('Id')
	iris.rename(columns={"SepalLengthCm": "sepal_len",
                         "SepalWidthCm": "sepal_width",
                         "PetalLengthCm": "petal_len",
                         "PetalWidthCm": "pteal_width",
                         "Species": "species"},
                inplace=True)
	return iris

def create_model_input_table(iris: pd.DataFrame) -> pd.DataFrame:
	"""
	Creates model data. As there is only one table it returns the
	input.

	Args:
	    iris: Preprocessed data for iris.
	Returns:
	    model input table.
	"""

	return iris