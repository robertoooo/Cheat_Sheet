# Code_Cheat_Sheets
My sheet sheets for different applications and languages

### See wiki


## GIT CLI
```console

#Adding repository 
git remote add origin remote repository URL
git pull origin master 

# Add and Commit the things you have done 
1. git add (The things you want to push)
2. git commit -m ""		//Commit the Changes	

#To merge two different local branches
3. git fetch origin master //Get changes from the branch master and pull them to remote (local) origin 
4. git rebase origin/master //Add changes from master to origin

#Push the new origin to the master 
5. git push origin master// Push the changes to the master

#To push to the master
git add . //Add all the changes
git commit -m "With these changes I have" //Commit the changes to the origin 
git push origin master //Push the changes from origin (local) to master 


git reflog //See the commits 


#See what branch you are on 
git branch -a 
git checkout sound_branch //Change to the branch sound branch 

#Reload a file from git
git checkout \path\filename	//Get the filepath and name from git status

#Check changes
git reflog //See all the recent changes 

#####################################
#Creating a new branch 
git checkout -b [name_of_your_new_branch] //Create the branch on your local machine and switch to this branch
git checkout [name_of_your_new_branch]		//Switch to another branch 
git push origin [name_of_your_new_branch]	//Push to the new branch 
git branch //see the active branches 

#####################################
#Mergin branches (test branch into master)
git checkout master
git pull origin master
git merge test
git push -f origin master //-f force 




git merge master //If you are in another branch, you will fetch master and rebase it to your branch


```
