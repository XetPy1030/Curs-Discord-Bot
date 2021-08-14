import os
import git
import shutil
import tempfile

fil = os.listdir()
notfil = ["db.pickle", "conf.py"]
for i in fil:
    if i not in notfil:
        os.remove(i)


git.Repo.clone_from('https://github.com/XetPy1030/discordBotXetPy.git', to_path=os.getcwd(), branch='main')
os.execl(sys.executable, sys.executable, *sys.argv)