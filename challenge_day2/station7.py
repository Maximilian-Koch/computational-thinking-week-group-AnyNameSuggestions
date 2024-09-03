def solution_station_7(equation):
    variables = {'a': 3, 'b': -1, 'c': 4, 'd': 7, 'e': 0.5}
    
    for var, value in variables.items():
        equation = equation.replace(var, str(value))
    
    try:
        result = eval(equation)
    except Exception as e:
        return f"Error in evaluating the equation: {e}"
    
    return result
