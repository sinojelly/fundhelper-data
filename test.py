# -- coding: utf-8 --

import os


def run_git_submit(work_dir):
    git_cmd = "git --git-dir=" + work_dir + "/.git --work-tree=" + work_dir + " "
    commit_cmd = git_cmd + "commit -am \"automatically submit.\""
    push_cmd = git_cmd + "push"
    status_cmd = git_cmd + "status"
    cmd = commit_cmd + " & " + push_cmd + " & " + status_cmd
    result = os.popen(cmd).read()
    print(result)
    return result


