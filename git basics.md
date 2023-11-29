# Git Basics

### Install
GitHub Desktop
desktop.github.com

Git for All Platforms
git-scm.com

## step by step for beginner

### Get Git via Git itself for updates:
- git clone https://git.kernel.org/pub/scm/git/git.git

### configuration for Git
- Git comes with a tool called "git config" that lets you get and set configuration variables that control
all aspects of how Git looks and operates. These variables can be stored in three different place
- 1. [path]/etc/gitconfig file: Contains values applied to every user on the system and all their
repositories. If you pass the option --system to git config.

- 2. ~/.gitconfig or ~/.config/git/config file: Values specific personally to you, the user. You can
make Git read and write to this file specifically by passing the --global option, and this affects
all of the repositories you work with on your system.

3. config file in the Git directory (that is, .git/config) of whatever repository you’re currently
using: Specific to that single repository. You can force Git to read from and write to this file with
the --local option, but that is in fact the default. Unsurprisingly, you need to be located
somewhere in a Git repository for this option to work properly.

- You can view all of your settings and where they are coming from using: git config --list --show-origin

### you identity
The first thing you should do when you install Git is to set your user name and email address. This
is important because every Git commit uses this information, and it’s immutably baked into the
commits you start creating: 
- git config --global user.name "Steven"
- git config --global user.email "example@gmail.com"

### Editor
- you can configure the default text editor that will be used when Git needs you to type in a message. could be "nano" (terminal based), Visual Studio Code (graphical) by "code --wait", or "emacs"
- git config --global core.editor "code --wait"

###  Your default branch name
- By default Git will create a branch called master when you create a new repository with "git init"
- To set main as the default branch name do: git config --global init.defaultBranch main

### check your settings
- git config --list --show-origin

### getting help
- git help <conmmand>
- git command --help
- git command -h (this is a more concise version with simple information)

### Getting a Git Repository (one of two ways below)
1. You can take a local directory that is currently not under version control, and turn it into a Git
repository, If you have a project directory that is currently not under version control and you want to start
controlling it with Git, you first need to go to that project’s directoryj. and then 
  - cd /Users/user/my_project
  - git init (you can reinitialise it if it was initialised before).
  - This creates a new subdirectory named .git that contains all of your necessary repository files — a Git repository skeleton
  - If you want to start version-controlling existing files (as opposed to an empty directory), you should probably begin tracking those files and do an initial commit. You can accomplish that with a few git add commands that specify the files you want to track, followed by a git commit: git add *.py or (git add --all) to add all files under the folder then git commit -m "Initial project version"
2. You can clone an existing Git repository from elsewhere. Cloning an Existing Repository
  - git clone https://github.com/libgit2/libgit2
  - Git has a number of different transfer protocols you can use. The previous example uses the https://protocol, but you may also see git:// or user@server:path/to/repo.git , which uses the SSH transfer protoco

### checking and change the status of your files
- git status
- git add file: untracked (not included in git yet) : by git add xxx to add it to git. then it's status changed to staged (included in git but not commited). This is a new file
- git add --all or git add * : add all files
- unmodified (commited files): edit those files will change their status to modified (commited before then edited but not staged). by git add xxx to add the edited version to staged (included in git but not commited yet)
- If you modify a file after you run git add, you have to run git add again to stage the latest version of the file
- git restore --staged filename or git reset HEAD filename: only change staged to modified.
- git checkout filename or git restore filename: unmodifying a modified file. change the file from staged to be unmodified (unstage your change and your change will be lost). use it carefully
- git diff: this command will show you the details of the changes made but not staged yet.
- git diff --staged:  what you’ve staged that will go into your next commit, you can use

### commiting your changes
- git commit -m "message for your commit"
- git commit -a -m "message for your commit": Adding the -a option to the git commit command makes Git automatically stage every file that is already tracked before doing the commit, letting you skip the git add part
- Every time you perform a commit, you’re recording a snapshot of your project that you can revert to or compare to later
- git commit --amend -m "new message for the last commit"

### removing files
- git rm filename then git commit
- you may want to keep the file on your hard drive but not have Git track it anymore. This is particularly useful if you forgot to add something to your .gitignore: file and accidentally staged it. to do this. you add --cached option: git rm --cached filename
- git rm \*~ : This command removes all files whose names end with a ~

### rename a file
- git mv file_from file_to

### view the commiting history
- git log 
- git log -p -2 --shortstat --graph
- git log --oneline
- git log --pretty=short (or full)
- git log -S function_name
- git log --since=2.weeks
- git log --pretty="%h - %s" --author='Junio C Hamano' --since="2008-10-01" \--before="2008-11-01" --no-merges -- t/

### Ignoring files
- Often, you’ll have a class of files that you don’t want Git to automatically add or even show you as being untracked. These are generally automatically generated files such as log files or files produced by your build system. In such cases, you can create a file listing patterns to match them named .gitignore
- You may also include a log, tmp, or pid directory; automatically generated documentation; and so on. Setting up a .gitignore file for your new repository before you get going is generally a good idea so you don’t accidentally commit files that you really don’t want in your Git repository

### working with remotes (collabrate with others. internet or local network or your own computer)
1. git remote -v: show your remotes
2. git remote add <shortname> <url> : Adding Remote Repositories. if you are in a new folder. use git init firstly.
3. git fetch shortname: The command goes out to that remote project and pulls down all the data from that remote project
that you don’t have yet. It’s important to note that the git fetch command only downloads the data to your local repository. it doesn’t automatically merge it with any of your work or modify what you’re currently working on. You have to merge it manually into your work when you’re ready.
4. git pull <remote url> : fetches data from the server you originally cloned from and automatically tries to merge it into the code you’re currently working on. generally "git clone" = "git remote add xxx" + "git fetch xxx" + "git pull <url>" + set tracking to remote
5. git branch --set-upstream-to=xxx/main : this set the tracking for local branch to remote.
6. git config --global pull.rebase false : to config what to do when you pull from remote. false=merge. true=rebase
7. git remote show xxx : detail information about a remote
8. git remote rename xxx yyy: rename remote xxx to yyy
9. git remote remove xxx : remove a remote all remote-tracking branches and configuration settings associated with that remote are also deleted

### tagging
1. git tag -a v0.1 -m "my first tag 0.1" : add a tag v0.1 with message. then you can show it with git tag or git show v0.1
2. git tag -d v0.1 : delete tage v0.1

### git alias
1. git config --global alias.unstage 'reset HEAD --' : then you can use git unstage filename 


## advanced functions

### Branching
- Because a branch in Git is actually a simple file that contains the 40 
- character SHA-1 checksum ofthe commit it points to, branches are cheap 
- to create and destroy. Creating a new branch is as quick and simple as 
- writing 41 bytes to a file (40 characters and a newline)

1. git branch testing or git switch -c testing: 
    - creating a new branch. it's a new pointer to a specific commit snapshot
    - your working branch is not swithced to the new branch yet. 
    - git log --oneline --decorate : will show you current working branch
    - HEAD point to the current working branch
2. git checkout testing or git switch testing:
    - switch to branch 'testing'. the HEAD now point to testing
    - if you make new commits here. then the main branch won't know it.
    - git log only show commit history below the branch you checked out. you can use "git log branchname"
    - Switching branches changes files in your working directory
    - you can switch back and forth between the branches and merge them together when you’re ready
    - git log --oneline --decorate --graph --all : showing where your branch pointers areand how your history has diverged
3. git checkout main and then git merge testing:
    - merge the testing branch back to your main branch
    - after the merge, you can delete the branch testing by
4. git branch -d testing :
    - delete the branch testing
    - git branch --all (show all branches)
    - git branch --no-merged
    - git branch --merged

## cheat-sheet for git commands
### Configure tooling
Configure user information for all local repositories

$ git config --global user.name "[name]"

Sets the name you want attached to your commit transactions

$ git config --global user.email "[email address]"

Sets the email you want attached to your commit transactions

$ git config --global color.ui auto

Enables helpful colorization of command line output


### Branches
Branches are an important part of working with Git. Any commits you make will be made on the branch you’re currently “checked out” to. Use git status to see which branch that is.

$ git branch [branch-name]

Creates a new branch

$ git switch -c [branch-name]

Switches to the specified branch and updates the working directory

$ git merge [branch]

Combines the specified branch’s history into the current branch. This is usually done in pull requests, but is an important Git operation.

$ git branch -d [branch-name]

Deletes the specified branch

### Make changes
Browse and inspect the evolution of project files

$ git log

Lists version history for the current branch

$ git log --follow [file]

Lists version history for a file, beyond renames (works only for a single file)

$ git diff [first-branch]...[second-branch]

Shows content differences between two branches

$ git show [commit]

Outputs metadata and content changes of the specified commit

$ git add [file]

Snapshots the file in preparation for versioning

$ git commit -m "[descriptive message]"

Records file snapshots permanently in version history
