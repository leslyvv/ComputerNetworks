import sys
import socket
#  scan host function that can scan a target
#  well-defined ports registered are 0 - 1023
# registered ports are 1024 to 49151
def scan_host(ip_addr, start_port, end_port):
    print("Starting tcp scanner on host", ip_addr)
    tcp_scanner(ip_addr, start_port, end_port)
    print("Scan complete ", ip_addr)


def tcp_scanner(ip_addr, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp_socket.connect_ex((ip_addr, port)):
                print("The specified IP address ", ip_addr)
                print("Port open: ", port)
                tcp_socket.close()
        except Exception:
            pass


def scan_Range(network, start_port, end_port):
    print("Starting TCP scan on network ", network)
    for host in range(1, 255):
        # adding the last octet
        ip = network + "." + str(host)
        tcp_scanner(ip, start_port, end_port)
    print("Finished TCP scan on network ", network)


def main():
    socket.setdefaulttimeout(0.01)
    network = input("Please enter a network:\n ")
    start_port = int(input("Please enter a start_port:\n "))
    end_port = int(input("Please enter a end_port:\n "))

    scan_host(network, start_port, end_port)


main()
