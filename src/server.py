import io
import os
import sys
import tarfile
import json
import subprocess

def process_data(source_path):
    with open('/testcases/testcases.json', 'r', encoding='utf-8') as tc_file:
        testcases = json.load(tc_file)

    cmd = [
        'ljudge',
        '--max-cpu-time', '1.0',
        '--max-memory', '32m',
        '--user-code', source_path
    ]

    for tc in testcases:
        inp, out = tc.get('input'), tc.get('output')
        cmd += ['--testcase', '--input', inp, '--output', out]

    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {
            'error': 'Failed to parse JSON output',
            'stdout': proc.stdout,
            'stderr': proc.stderr
        }

def main():
    try:
        buf = sys.stdin.buffer.read()

        # Extract tar stream
        tar_stream = io.BytesIO(buf)
        with tarfile.open(fileobj=tar_stream, mode='r:*') as tar:
            members = [m for m in tar.getmembers() if m.isfile()]
            if not members:
                raise ValueError("No files found in tar archive")
            first = members[0]
            tmp_dir = '/tmp'
            os.makedirs(tmp_dir, exist_ok=True)
            dest_path = os.path.join(tmp_dir, os.path.basename(first.name))
            with tar.extractfile(first) as src, open(dest_path, 'wb') as dst:
                dst.write(src.read())

        result = process_data(dest_path)
        print(json.dumps(result))

    except Exception as e:
        error_msg = {'error': str(e)}
        print(json.dumps(error_msg))

if __name__ == '__main__':
    main()
