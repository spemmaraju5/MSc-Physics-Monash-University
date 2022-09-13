# Git Tutorial Notes (13/9/2022)

## Command Reference and Additional Notes
 1. ```git init ``` initialises an empty repository in the present directory
 2. ```git add``` adds new files into the repository
 3. ```git commit ``` commits the changes to the relevant branch in the repository (include a message with ```git commit -m '<Message>'```)
 4. ```git status``` provides a list of both tracked, and untracked files
 5. ```git diff``` provides a list of the changes and differences between files within a repository
 One can add a ```.gitignore``` file to specify the files that are to be ignored by the version control system (refer to meeting recording for the syntax). One must add the ```.gitignore''' file using ```git add```  and commit this file as well
6. ```git rm``` is not permanent (the file is moved to a staging area). The file is deleted once the delete is committed
7. ```git log``` provides a list of versions of the repository, and can be used if one seeks to recover previous versions of repositories.
8. ```git checkout <branch name>``` allows one to examine a particular branch and commit changes (with sufficient permissions)
9. ```git clone``` clones a remote repository onto the local machine
A detached HEAD state occurs when a previous version of an existing branch is checked out.
10. ```git bisect``` tracks the changes between branches. It can be initialised by ```git bisect start``` and then tag one as ```good``` and the other as ```bad```. ```git bisect reset``` resets the track changes
11. ```git mv``` can be used to rename files in an existing repository (this must be committed)
12. ```git show``` displays details about the actions taken in the commit (i.e. what was done in a specific commit)
13. ```git push``` pushes changes to the remote branch
14. ```git pull``` pulls commits from the remote branch
15. ```git branch``` specifies the name of the current branch and lists any other existing branches
16. ```git checkout -b <branch name>``` switches to (or creates) the named branch
17. ```git merge``` applies all the commits made on one branch to the ```master``` branch
18. ```git branch -d <branch name>``` deletes the branch of name ```<branch name>```
19. Avoid commiting changes into past branches (complicated to resolve). If this happens, delete your repository or start working on a clean copy of the same
To commit files via ```https``` rather than SSH, one can edit the URL field ```.git/config``` file to include the SSH URL by default
