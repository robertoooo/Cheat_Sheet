# Code_Cheat_Sheets
My sheet sheets for different applications and languages

### See wiki


## GIT CLI PUSH MERGE COMMIT
```shell class:"lineNo"

#Adding repository 
git remote add origin <remote repository URL>
git pull origin master 

#To push to the master
git add . //Add all the changes
git commit -m "With these changes I have" //Commit the changes to the origin 
git push origin master //Push the changes from origin (local) to master 	

```

### Merge
```shell class:"lineNo"


#To merge two different local branches
3. git fetch origin master //Get changes from the branch master and pull them to remote (local) origin 
4. git rebase origin/master //Add changes from master to origin

#Push the new origin to the master 
5. git push origin master// Push the changes to the master

#####################################
#Mergin branches (test branch into master)
git checkout master
git pull origin master
git merge test
git push -f origin master //-f force 

git merge master //If you are in another branch, you will fetch master and rebase it to your branch

```

### Status of remote origin/URL, Remove origin
```shell class:"lineNo"


git remote show origin //Full output of remote repo 
git config --get remote.origin.url //Get the remote URL (offline)

git remote -v //View current remotes
git remote rm origin //Remove the origin remotes 

```

### Various Commands
```shell class:"lineNo"

#Reload a file from git
git checkout \path\filename	//Get the filepath and name from git status


git reflog //See all the recent changes  

```

### Branches, Creating, Status, Diff
```shell class:"lineNo"

#####################################
#Creating a new branch 
git checkout -b [name_of_your_new_branch] //Create the branch on your local machine and switch to this branch
git checkout [name_of_your_new_branch]		//Switch to another branch 
git push origin [name_of_your_new_branch]	//Push to the new branch 
git branch //see the active branches 


#See what branch you are on 
git branch -a 
git checkout sound_branch //Change to the branch sound branch 

git diff master remotes/origin/master //Compare the local and remote master 

```
## Diff between local and remote branch in VS code
Open file in VS Code
```shell class:"lineNo"
code  ~/.gitconfig
```
And add the following lines 
```shell class:"lineNo"
[diff]
    tool = default-difftool
[difftool "default-difftool"]
    cmd = code --wait --diff $LOCAL $REMOTE
```
To compare differences between local and remote branch
```shell class:"lineNo"
git difftool master origin/master
```

### Hotkeys
C:\Programs\Git\etc\profile.d\aliases.sh
```shell
alias st='git status'
alias co='git checkout'
alias aa='git add .'
alias push='git push origin master'
```
