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

### checking your status of your files
- git status
- untracked (not included in git yet) : by git add xxx to add it to git. then it's status changed to staged (included in git but not commited). This is a new file
- unmodified (commited files): edit those files will change their status to modified (commited before then edited but not staged). by git add xxx to add the edited version to staged (included in git but not commited yet)
- If you modify a file after you run git add, you have to run git add again to stage the latest version of the file

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
