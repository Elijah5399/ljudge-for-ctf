ljudge-for-ctf
======

ljudge is a command line tool to compile, run, check its output and generate a JSON report. It is designed to be the backend tool for an online judge system which runs without a database.

ljudge-for-ctf builds on ljudge, with the following additions:
- `Dockerfile` and `run.sh` to simplify and standardise the deployment of challenges
- Simplified way of creating testcases to run code against them

**Note that ljudge-for-ctf currently only supports .py, .c, .cpp and .java files.**

Installation
=====
- Simply clone the repository, then follow the instructions under "usage"

Usage
=====

**For challenge creators**
- Replace the files in the testcases folder with your input and output files, and change testcases.json to be of the format shown. Use `dox2unix` to ensure testcases are free of CRLF.
- Change the ports specified in `run.sh` and `dockerfile` if necessary
- Provide participants with submitter.py and challenge description.
- Replace the flag which is hardcoded in `server.py`.
- Simply run `run.sh`.

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

Common Problems
=====

**Q: Why am I getting the error FATAL: can not mount cgroup cpuacct on '/sys/fs/cgroup/cpuacct' (Operation not permitted)?**

A: This is likely because the machine is using cgroup v2, and not the legacy cgroup. To fix this, edit `/etc/default/grub` and replace the line containing `GRUB_CMDLINE_LINUX_DEFAULT` to the following line:

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet systemd.unified_cgroup_hierarchy=0"
```

Then run `sudo update-grub` and `sudo reboot`. 

