def get_model_input_shape(model_name):
    """Get the input shape from timm model configuration."""
    data_config = {}
    input_size = data_config["input_size"]
    return (1, *tuple(input_size))  # Add batch dimension