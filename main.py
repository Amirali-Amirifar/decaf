import logging
import sys

from build import JavaToCTranspiler

def main(**args):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    transpiler = JavaToCTranspiler()
    success = transpiler.transpile(args["file"])
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename.java>")
        sys.exit(1)
    main(file=sys.argv[1])
