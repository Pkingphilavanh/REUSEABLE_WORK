import subprocess
import time

def start_iperf_server(port):
    # Start the iperf server on the given port
    process = subprocess.Popen(['iperf3', '-s', '-p', str(port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    # List of ports for each iperf server
    ports = [5201, 5202, 5203]

    # Start the servers
    processes = []
    for port in ports:
        print(f"Starting iperf server on port {port}...")
        process = start_iperf_server(port)
        processes.append(process)
        time.sleep(1)  # Ensure servers are started with a small delay

    # Optionally, you can keep the script running, waiting for user to stop servers
    try:
        while True:
            time.sleep(10)  # Keep the script running
    except KeyboardInterrupt:
        print("Shutting down iperf servers...")
        # Terminate the processes when the script is interrupted
        for process in processes:
            process.terminate()

if __name__ == '__main__':
    main()
