import hashlib
import getpass as gp
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        algorithm = "sha256"
    else:
        algorithm = sys.argv[1].lower()
    if algorithm not in hashlib.algorithms_available:
        print("Error: Not a valid algorithm", file=sys.stderr)
        sys.exit(1)
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
    print(message.hexdigest())
