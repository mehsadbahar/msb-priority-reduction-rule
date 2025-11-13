from .core import cli_format
import sys
import ast

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m msb_priority_reduction '[3,2,1,1]'")
        sys.exit(1)
    
    try:
        v = ast.literal_eval(sys.argv[1])
    except Exception:
        print("Unable to parse vector. Provide a Python-style list, e.g. '[3,2,1,1]'")
        sys.exit(1)
    
    print(cli_format(v))
