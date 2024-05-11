def list_to_dict(input_list):
    """
    Returns a dictionary where each element of input_list is a value,
    and the corresponding key is the numerical index of that element in input_list.

    Args:
    input_list (list): The input list.

    Returns:
    dict: A dictionary where keys are numerical indices and values are elements from the input list.
    """
     return {index: value for index, value in enumerate(input_list)}
