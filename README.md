ljudge-for-ctf
======

ljudge is a command line tool to compile, run, check its output and generate a JSON report. It is designed to be the backend tool for an online judge system which runs without a database.

ljudge-for-ctf builds on ljudge, with the following additions:
- Dockerfile and docker compose to simplify and standardise the deployment of challenges
- Simplified way of creating testcases to run code against them

**Note that ljudge-for-ctf currently only supports .py, .c, .cpp and .java files.**

Installation
=====
- Simply clone the repository, then follow the instructions under "usage"

Usage
=====

**For challenge creators**
- Replace the files in the testcases folder with your input and output files, and change testcases.json to be of the format shown.
- Change the ports specified in docker-compose.yml and dockerfile if necessary
- Provide participants with submitter.py and challenge description.
- Replace the flag which is hardcoded in `server.py`.
- Simply run `docker compose up` to start the challenge instance. This may take awhile.

**For CTF players**
- Run the submitter.py file according to the following syntax:

```bash
python3 submitter.py <PATH_TO_CODE_FILE> <TARGET_IP> <TARGET_PORT>
```

- The program's output should be in the json format, telling you the results of compilation and the results of running your program against the various testcases.
- If you see something like:

```json
{"error": "Failed to parse JSON output", "stdout": "", "stderr": "/run/lrun/mirrorfs/6d0e191bc1aaa4e9839b78c6616500fe760a18fb\ncannot mkdir: /home/judger/.cache/ljudge/kconfig\n"}
```

Then simply submit your code again.
- If you get an AC verdict, you will get the flag!