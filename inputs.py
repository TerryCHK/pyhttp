# Argument parser for intialization of the server
# Default server will be hosted at localhost:5005

import argparse


def show_server_info(server_addr):
    address, port = server_addr
    print(f"Server running on {address}:{port}")

def get_host(args):
    """
    Process the input arguments and return the address:port combination
    """
    # Default values
    address = "localhost"
    port = 5000
    if args.address:
        address = args.address
    if args.port:
        port = args.port
    if args.verbose:
        show_server_info(address, port)
    return (address, port)

def setup_host():
    """
    Argument parser for starting the server
    """
    parser = argparse.ArgumentParser(description="Input arguments for server")
    parser.add_argument("-a", "--address", help="Address to host server on",
        required=False)
    parser.add_argument("-p", "--port", help="Port to host server on",
        required=False, type=int)
    parser.add_argument("-v", "--verbose", help="Verbose mode",
        required=False, action='store_true')
    args = parser.parse_args()
    return get_host(args)
