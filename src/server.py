import socket
import json
import subprocess

HOST = '0.0.0.0'
PORT = 5000


def process_data(source_path):
    """
    Given a source file path, load testcases, invoke ljudge with that file,
    and return its JSON output.
    """
    # 1. Load testcase definitions
    with open('/mnt/c/Users/chiae/Documents/ljudge-for-ctf/testcases/testcases.json', 'r', encoding='utf-8') as tc_file:
        testcases = json.load(tc_file)

    # 2. Build the ljudge command
    cmd = [
        'ljudge',
        '--max-cpu-time', '1.0',
        '--max-memory', '32m',
        '--user-code', source_path
    ]

    # build ljudge command with our testcases
    for tc in testcases:
        inp, out = tc.get('input'), tc.get('output')
        cmd += ['--testcase', '--input', inp, '--output', out]

    # 3. Run ljudge
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # 4. Parse JSON output
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {
            'error': 'Failed to parse JSON output',
            'stdout': proc.stdout,
            'stderr': proc.stderr
        }

"""
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        # Read full tar stream
        buf = b''
        while True:
            chunk = conn.recv(4096)
            if not chunk:
                break
            buf += chunk

        # Extract first file from tar to /tmp
        tar_stream = io.BytesIO(buf)
        with tarfile.open(fileobj=tar_stream, mode='r|*') as tar:
            members = [m for m in tar.getmembers() if m.isfile()]
            if not members:
                raise ValueError("No files found in tar archive")
            first = members[0]
            tmp_dir = '/tmp'
            os.makedirs(tmp_dir, exist_ok=True)
            dest_path = os.path.join(tmp_dir, os.path.basename(first.name))
            with tar.extractfile(first) as src, open(dest_path, 'wb') as dst:
                # Read all bytes and write directly
                data = src.read()
                dst.write(data)

        # Process using the extracted file path
        result = process_data(dest_path)
        response = json.dumps(result).encode('utf-8')
        conn.sendall(response)
    except Exception as e:
        error_msg = {'error': str(e)}
        conn.sendall(json.dumps(error_msg).encode('utf-8'))
    finally:
        conn.close()
        print(f"Connection closed {addr}")


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}...")
        while True:
            conn, addr = server_socket.accept()
            handle_client(conn, addr)


if __name__ == '__main__':
    run_server()
"""

if __name__ == '__main__':
    process_data("/mnt/c/Users/chiae/Documents/ljudge-for-ctf/testcases/a.cpp")
