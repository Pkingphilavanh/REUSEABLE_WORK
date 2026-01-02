import subprocess
import time
from datetime import datetime

def start_iperf_server(port):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log = f"iperf3_{port}_{timestamp}.log"
    
    # Start the iperf server on the given port
    process = subprocess.Popen(['iperf3', '-s', '-p', str(port)], stdout=log, stderr=log)
    time.sleep(1)
    if process.poll() is not None:
        raise RunTimeError(f"Failed to start iperf3 on port {port}. See log file {log}.")
        
    return process

def main():
    # List of ports for each iperf server
    ports = [5201, 5202, 5203]

    # Start the servers
    processes = []
    for port in ports:
        print(f"Starting iperf server on port {port}...")
        process = start_iperf_server(port)
        print(f"Started iperf server on port {port} (PID {process.pid})")
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

