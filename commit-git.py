#import  git

#repo = '/storage/emulated/0/git/git/.git'  # make sure .git folder is properly configured
#comtext = 'nyuuu vorzson'

#def git_push():
#    try:
#        git.Repo = Repo(repo)
#        git.Repo.git.add(update=True)
#        git.Repo.index.commit(comtext)
#        origin = git.Repo.remote(name='origin')
        #origin.push()
    #except:
#        print('Some error occured while pushing the code')    

#git_push()



import subprocess as cmd

cmd.run('cd /storage/emulated/0/git/git', check=True, shell=True)
cmd.run('pwd', check=True, shell=True)
cmd.run('ls', check=True, shell=True)
cmd.run('git status', check=True, shell=True)
cmd.run('git add .', check=True, shell=True)
cmd.run('git commit -m "nyuuu worzson" ', check=True, shell=True)
cmd.run('git push', check=True, shell=True)