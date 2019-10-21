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
git stash clear
------------------------------------
--- Fetches data from Github------
----git Fetch
This creates diverged from local branch and oirigin/master in this case
and did not pull anything from Github
-Best Practice to Merge them-
---git merge origin/master
leave notes
Then....
----git push
-------------------------------------
---- Deleting local Branch----
--git branch -d {name of branch}
check branch
git branch
----Deleting remote Branch---
git push origin --delete {name of the branch}

----------------------------------
----- Looking at Changes -----
git diff {name of file}
ex : git diff one.js
------------------------------
---- Removing changes --------
git checkout .
-------------------------------
--- Removing a file before git commit----
rm {name of directory}
since it is untracked file
-------------------------------
---- Reverting to a previous file--------
git log
to navitgate through log
j and k and also shift G to move all the way down
and q to exit
-next-
copy commit
-then
git checkout { paste commit } -- { path of the file }
-then
- git add .
-git commit -m
-git push
-----------------------
---- Creating a new branch with the current version of commmit -----
- git checkout 3c0829c4ce4131872cb0dbc3875ef2f13fd71e69 -b {name of the new branch}
-- This will make a new branch and change all the files to that point in time
-Deleting the branch
git branch -d {name of branch}
---------------------------
---- Reseting an entire project and delete all commits-
- git reset --hard {add commit}
--- Forcing content to github---
git push -f origin master
----------------------------
'''