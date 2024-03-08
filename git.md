# Git commands
- git init -> initilize git hidden folder for new projects
- git add . -> stage changes
- git commit -m "This is my first project" -> commit with message
- git log -> view all previous commits
- git checkout partOfCommitID -> switch back to commit (back button - switches to the commits that you were in before)
- git checkout - -> switch back to current branch
- git checkout master -> to get to master
- git revert commitID -> delete from file but can revert
- git reset --soft HEAD~1 -> remove last commits with deleting from file 
- git reset --hard HEAD~1 -> remove last commits with deleting complete history
- git log --help
- git log -Sprint -> searches for all commits inside the files with the print word (see commit message)
- git log -Sprint -p -> see changes in particular file did you remove or insert print word
- git log -2 -> last two commits alone 
- git log --graph -> graph commits
- git push --all -> pushes all branches to repository
- git pull --rebase origin master

------

- can run in cmd prompt, bash or powershell
- don't need internet until you publish to github
- whichever the latest commit is, the master will be in
- space to scroll down in log
- q to quit log

# Branching concepts
- master branch is what you're delivering to the customer
    - need to cut a branch when you are implementing/testing a new feature / development purpose
- merging branches is when both branches are in to the master again and released to the customer
- never mess with master -> what the customer can see
- in general, 3 branches
    1. master branch, never directly commit
    2. staging branch, to test by quality engineers/testers to give okay to merge to master
    3. dev/feature branch, where you create the features
- master will always lag, end of month update or how often the cycle is (release update)
- dev branch will be the latest code, code changes every day

## Cutting a branch with git commands
- git checkout -b dev (creates a new branch from commit you're currently on and switches)

## Merging a branch to master (don't do it locally)
1. checkout to branch that you need to do the merge on (old)
2. Merge with the dev branch (new)
3. git merge dev -> you are currently on master

## Merge conflict
1. Resolve
2. Stage
3. Commit 

## Staging area
- only a few files at the same time
- checks errors

## Git vs GitHub
- Git: version control - local
- GitHub: file storage - online

