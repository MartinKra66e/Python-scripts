import subprocess

def nmap_scan(ip_address):
    # Construct the Nmap command
    nmap_command = ['nmap', ip_address]

    try:
        # Run the Nmap command and capture the output
        result = subprocess.run(nmap_command, capture_output=True, text=True)

        # Print the Nmap scan result
        print(result.stdout)

        # Check for errors
        if result.returncode != 0:
            print(f"Error: Nmap scan failed with code {result.returncode}")
            print(result.stderr)
            return None

        # Check if port 80 is open
        if '80/tcp' in result.stdout:
            print("Port 80 is open. Running WhatWeb...")

            # Run WhatWeb on the target
            whatweb_command = ['whatweb', '-v', f'http://{ip_address}:80']
            whatweb_result = subprocess.run(whatweb_command, capture_output=True, text=True)

            # Print the WhatWeb result
            print(whatweb_result.stdout)

            # Check for errors
            if whatweb_result.returncode != 0:
                print(f"Error: WhatWeb scan failed with code {whatweb_result.returncode}")
                print(whatweb_result.stderr)

    except Exception as e:
        print(f"An error occurred: {e}")

# Example: Scan the IP address '192.168.1.1'
ip_to_scan = '192.168.1.1'
nmap_scan(ip_to_scan)
