def list_to_dict(input_list):
    """
    Returns a dictionary where each element of input_list is a value,
    and the corresponding key is the numerical index of that element in input_list.

    Args:
    input_list (list): The input list.

    Returns:
    dict: A dictionary where keys are numerical indices and values are elements from the input list.
    """
    result_dict = {}
    for i in range(len(input_list)):
        result_dict[i] = input_list[i]
    return result_dict
