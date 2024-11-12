from typing import List

# Define vector as a list of floats or integers
Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    # Check that the vectors are the same length
    if len(v) != len(w):
        raise ValueError("Vectors must be of the same length")
    
    # Add corresponding elements
    return [v_i + w_i for v_i, w_i in zip(v, w)]
