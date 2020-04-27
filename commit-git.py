import subprocess as cmd

cmd.run('cd /storage/emulated/0/git/git', check=True, shell=True)
cmd.run('pwd', check=True, shell=True)
cmd.run('ls', check=True, shell=True)
cmd.run('git add .', check=True, shell=True)
cmd.run('git commit -m "nyuuu wörzsön" ', check=True, shell=True)
cmd.run('git push', check=True, shell=True)