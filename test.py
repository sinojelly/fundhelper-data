# -- coding: utf-8 --

import os
import subprocess


def run_external_cmd(cmd, msg_in=''):
    try:
        proc = subprocess.Popen(cmd,
                                shell=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                )
        stdout_value, stderr_value = proc.communicate(msg_in)
        return stdout_value, stderr_value
    except ValueError as err:
        # log("ValueError: %s" % err)
        return None, None
    except IOError as err:
        # log("IOError: %s" % err)
        return None, None


def run_git_submit(work_dir):
    git_cmd = "git --git-dir=" + work_dir + "/.git --work-tree=" + work_dir + " "
    commit_cmd = git_cmd + "commit -am \"automatically submit.\""
    push_cmd = git_cmd + "push"
    status_cmd = git_cmd + "status"
    cmd = commit_cmd + " & " + push_cmd + " & " + status_cmd
    # result = os.popen(cmd).read()
    stdout_value, stderr_value = run_external_cmd(cmd)
    print(stdout_value.decode())
    print("---------------err-------------")
    print(stderr_value.decode())
    return stdout_value, stderr_value


if __name__ == '__main__':
    run_git_submit("D:\\Develop\\projects\\web-projects\\fundhelper-data")
    # run_git_submit("/usr/local/fundhelper-data")


