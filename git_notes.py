'''
removing git
setting = **/.git
----------
- If you get error status after you used .gitignore file-
git rm -r --cached .
removes all local cache changes 
'''
'''
-START-
git init
starts a new repository in this directory
----------
-Show Hiding Git Diretory-
ls -la
-----------
- Shows status of repository-
git status
-----------
-Adding Files-
git add . 
this will add everything
git add my_file.py
this adds specific file
------------
-To Commit the file-
git commit -m "add message"
-------------
-Creat repository in Github-
ex : git remote add origin https://github.com/alex2chivas/my-git-project
.git
-check remotes 
git remote -v
-------------
-Push items-
ex : git push -u origin master
-------------
-Pull items-
git pull
--------------
- Viewing Branches-
git branch
----------------
-Switching and creating New Branch-
git checkout -b readme-styling
-----------------
- Merging Branches-
git merge readme-styling

---------------------
-Pushing another branch to Github-
git push -u origin another-feature
origin is the name if the remote
this reprsents the up stream

-----------------------
-Rebasing-
git rebase master
git rebase master {name of repository}
-------------------------
- Stashing new code or notes on Git without Commit-
git stash
git stash list 
git stash show
git stash apply
'''