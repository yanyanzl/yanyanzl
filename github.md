# GitHub basics


- At the heart of GitHub is an open-source version control system (VCS) called Git. 
- Git is responsible for everything GitHub-related that happens locally on your computer.

1. install Git by HomeBrew. (install HomeBrew first) : brew install git
2. Setting your username in Git: Git uses a username to associate commits with an identity. The Git username is not the same as your GitHub username.
     - Setting your Git username for every repository on your computer: git config --global user.name "yanyanzl"
     - Setting your Git username for a single repository: Change the current working directory to the local repository where you want to configure the name that is associated with your Git commits. then : git config user.name "yanyanzl"
3. Set an email address in Git. You can use your GitHub-provided noreply email address or any email address. : git config --global user.email "YOUR_EMAIL"
     - Add the email address to your account on GitHub, so that your commits are attributed to you and appear in your contributions graph.
5. Connect by SSH connection: Generating a new SSH key: You can access and write data in repositories on GitHub.com using SSH (Secure Shell Protocol).When you connect via SSH, you authenticate using a private key file on your local machine.
     - On your local computer, open terminal, replacing the email used in the example with your GitHub email address. by:  ssh-keygen -t ed25519 -C "your_email@example.com". this will generate two files: /Users/YOU/.ssh/id_Ed25519 (this is a private key) and id_ed25519.pub (this is a public key)
     - Adding your SSH key to the ssh-agent. by this commond:  ssh-add --apple-use-keychain ~/.ssh/id_ed25519
     - Add the SSH public key to your account on GitHub. For more information, see "Adding a new SSH key to your GitHub account."
     - test your SSH connection: $ ssh -T git@github.com
     - Adding or changing a passphrase: You can change the passphrase for an existing private key without regenerating the keypair by typing the following command: ssh-keygen -p -f ~/.ssh/id_ed25519
6. Connect by HTTPS: 
     


