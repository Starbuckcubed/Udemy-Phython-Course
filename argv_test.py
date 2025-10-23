import sys

print(f"Script name: {sys.argv[0]}")

if len(sys.argv) > 1:
    print("Arguments passed:")
    for i, arg in enumerate(sys.argv[1:]):
        print(f"  Argument {i+1}: {arg}")
else:
    print("No arguments passed.")