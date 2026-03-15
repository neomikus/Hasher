import hashlib
import getpass as gp
import sys
import argparse

def init_argparse():
    parser = argparse.ArgumentParser(
        prog="Hasher",
        description="Password hasher"
    )
    parser.add_argument("--algorithm", "-a", choices=hashlib.algorithms_available, default="sha256", type=str.lower, help="Selected hash algorithm")
    parser.add_argument("--clipboard", "-c", action="store_true", default=False, help="If this flag is present, output will be directly copied to clipboard")
    return (parser)

if __name__ == "__main__":
    parser = init_argparse()
    args = parser.parse_args()
    algorithm = args.algorithm.lower()
    message = hashlib.new(algorithm)
    try:
        password = gp.getpass(prompt="Insert password: ")
    except (EOFError, KeyboardInterrupt):
        print("Exiting", file=sys.stderr)
        sys.exit(0)
    if not password:
        print("Error: Empty password", file=sys.stderr)
        sys.exit(1)
    message.update(password.encode())
    if (args.clipboard):
        try:
            import pyperclip
        except ModuleNotFoundError:
            print("Error: optional dependency pyperclip not installed", file=sys.stderr)
            sys.exit(1)
        try:
            pyperclip.copy(message.hexdigest())
        except pyperclip.PyperclipException as e:
            print("pyperclip exception:", e, file=sys.stderr)
        else:
            print("Copied to clipboard!", file=sys.stderr)
    else:
        print(message.hexdigest())
