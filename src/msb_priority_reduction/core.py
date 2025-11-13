from typing import List, Tuple

def msb_priority_reduction(vector: List[int]) -> List[Tuple[int, ...]]:
    if not isinstance(vector, list):
        raise ValueError("Input must be a list of non-negative integers.")
    if not all(isinstance(x, int) and x >= 0 for x in vector):
        raise ValueError("Input vector must contain non-negative integers only.")
    
    vec = list(vector)
    n = len(vec)
    states = [tuple(vec)]
    
    if n == 0:
        return states
    
    i = 0
    while any(x > 0 for x in vec):
        if vec[i] > 0:
            vec[i] -= 1
            states.append(tuple(vec))
        i = (i + 1) % n
        
    return states

def cli_format(vector):
    return " -> ".join(str(list(s)) for s in msb_priority_reduction(vector))

if __name__ == '__main__':
    import sys, ast
    if len(sys.argv) < 2:
        print("Usage: python -m msb_priority_reduction '[3,2,1,1]'")
        sys.exit(1)
    try:
        v = ast.literal_eval(sys.argv[1])
    except Exception:
        print("Unable to parse vector. Provide a Python-style list, e.g. '[3,2,1,1]'")
        sys.exit(1)
    print(cli_format(v))
