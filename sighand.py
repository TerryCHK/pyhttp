# Signal handler module to prevent bad termination of server


import signal
import sys


def signal_handler(sig, frame):
    print("Server is now shutting down")
    sys.exit(0)