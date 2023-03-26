"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_iris, create_model_input_table


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_iris,
                inputs="iris",
                outputs="preprocess_iris",
                name="preprocess_iris_node"
            ),
            node(
                func=create_model_input_table,
                inputs="preprocess_iris",
                outputs="model_input_table",
                name="create_model_input_table_node"
            ),
        ]
    )
