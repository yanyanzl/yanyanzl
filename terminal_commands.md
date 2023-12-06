# commands used in the terminal


## basic commands used daily 

1. cat

2. ls
    - view the current permissions of a file or directory? : ls -l
    - To see all the permissions that a particular directory or file has. : ls -l file
        - -rw-r--r--  1 root  wheel   1.9K 12 Oct 12:10 ssh_config
        - Field Explanation
            – normal file
            d : directory
            s : socket file
            l : link file
            Field 1 – File Permissions: Next characters specifyes the files permission. Every 3 characters specify read, write, execute permissions for user(root), group and others respectively in order. Taking the above example, -rw-rw-r– indicates read-write permission for user(root), read permission for group, and no permission for others respectively. If all three permissions are given to user(root), group and others, the format looks like -rwxrwxrwx
            Field 2 – Number of links: Second field specifies the number of links for that file. In this example, 1 indicates only one link to this file.
            Field 3 – Owner: Third field specifies owner of the file. In this example, this file is owned by username ‘maverick’.
            Field 4 – Group: Fourth field specifies the group of the file. In this example, this file belongs to” maverick’ group.
            Field 5 – Size: Fifth field specifies the size of file in bytes. In this example, ‘1176’ indicates the file size in bytes.
            Field 6 – Last modified date and time: Sixth field specifies the date and time of the last modification of the file. In this example, ‘Feb 16 00:19’ specifies the last modification time of the file.
            Field 7 – File name: The last field is the name of the file. In this example, the file name is 1.c.


3. cd,  cd.., cd+space, 

4. dirs

5. mkdir

6. mv

7. rm

8. cp

9. echo

10. pbcopy

11. open
    - open -a spyder (open that Application, no matter where it is located)
    - open Downloads/Instructions.doc -a TextEdit (open a file with a specific application)
    - Add -F to open a "fresh" copy of the application

12. vim : To save a file in Vim / vi, press Esc key, type :w and hit Enter key. 
    One can save a file and quit vim / Vi by pressing Esc key, type :x and hit Enter key
    
13. super user command: sudo vi /etc/paths

14. input and output stream
```sh
- >   Use a right angle bracket to redirect command output to a file.

- <   Use a left angle bracket to use the contents of a file as input to the command.

- >>  Use two right angle brackets to append output from a command to a file.

- the following command passes the formatted contents of the zsh man page to the grep tool, which searches the contents for lines containing the word commands. The result is a list of lines with the specified text, instead of the entire man page.
% man zsh | grep commands


Standard pipes include:
stdin: The standard input pipe is where a command receives input. By default, you enter input from the command-line interface. You can redirect the output from files or other commands to stdin.

stdout: The standard output pipe is where command output is sent. By default, command output is sent to the command line. You can redirect the output from the command line to other commands and tools.

stderr: The standard error pipe is where error messages are sent. By default, errors are displayed on the command line along with standard output.
```

15. export : this command list all enviorenment parameters set on the system
 - export PATH="/Library/PostgreSQL/16/bin:$PATH" : this command add postgreSQL to PATH
 - export PATH="/Applications/Visual Studio Code.app/Contents/Resources/app/bin:$PATH"
 - export PATH="/Applications/Visual Studio Code.app/Contents/Resources/app/bin /Users/yanyanzhou/miniconda3/envs/ai/bin /Users/yanyanzhou/miniconda3/condabin /usr/local/bin /System/Cryptexes/App/usr/bin /usr/bin /bin /usr/sbin /sbin /Library/Apple/usr/bin /var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin /var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin /var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:$PATH"
 
 
16. curl: curl is a command-line tool to transfer data to or from a server, using any of the supported protocols (HTTP, FTP, IMAP, POP3, SCP, SFTP, SMTP, TFTP, TELNET, LDAP, or FILE). curl is powered by Libcurl. This tool is preferred for automation since it is designed to work without user interaction. curl can transfer multiple files at once. 
- curl https://www.geeksforgeeks.org (This should display the content of the URL on the terminal.)
- Options: 
    - o: saves the downloaded file on the local machine with the name provided in the parameters. 
    - curl -o [file_name] [URL...]
    - -C -: This option resumes download which has been stopped due to some reason. This is useful when downloading large files and was interrupted. 
    - curl -C - -O ftp://speedtest.tele2.net/1MB.zip
    - -u: curl also provides options to download files from user authenticated FTP servers. 
    - curl -u {username}:{password} [FTP_URL] (example curl -u demo:password -O ftp://test.rebex.net/readme.txt)
    - -T: This option helps to upload a file to the FTP server. 
    - curl -u {username}:{password} -T {filename} {FTP_Location}
    - Sending mail: As curl can transfer data over different protocols, including SMTP, we can use curl to send mails. 
    - curl –url [SMTP URL] –mail-from [sender_mail] –mail-rcpt [receiver_mail] -n –ssl-reqd -u {email}:{password} -T [Mail text file] 
    - DICT protocol: The Libcurl defines the DICT protocol which can be used to easily get the definition or meaning of any word directly from the command line. 
    - curl dict://dict.org/d:overclock
    
17. change PATH permanently
- a very neat way to do this in OS X, the /etc/paths file!  The file contains a list (one per line) of paths that are added to the $PATH variable in the shell

```sh
sudo nano /etc/paths 
Enter your password, when prompted.
Go to the bottom of the file, and enter the path you wish to add.
Hit control-x to quit.
Enter “Y” to save the modified buffer.

```

18. Combining two or more commands on the command line is also known as "command chaining".
    - Option One: The Semicolon (;) Operator. Example (ls ; pwd ; whoami)
    - If you want the second command to only run if the first command is successful, separate the commands with the logical AND operator, which is two ampersands ( && ). For example, we want to make a directory called MyFolder and then change to that directory--provid. 
    - Example: mkdir MyFolder && cd MyFolder
    
    
19. Use at and batch to Schedule Commands
- To use at, you have to assign it a date and time to run. You can pipe commands into at, like this:
- echo "sh ~/sweep.sh" | at 08:45 AM
- Using at with Files of Commands. You can use the -f (file) option in the following way to pass a filename to at: at now + 5 minutes < clean.txt
- atq to show the queue of task list.
- atrm to remove one task.

20.  chmod command is used to change the access mode of a file. The name is an abbreviation of change mode.
- Which states that every file and directory has a set of permissions that control the permissions like who can read, write or execute the file. In this the permissions have three categories: read, write, and execute simultaneously represented by `r`, `w` and `x`
- chmod [options] [mode] [File_name] 
    - Options: 
        - `-R`	Apply the permission change recursively to all the files and directories within the specified directory.
        - `-v`	It will display a message for each file that is processed. while indicating the permission change that was made.
        - `-c`	It works same as `-v` but in this case it only displays messages for files whose permission is changed.
        - `-f`	It helps in avoiding display of error messages.
        - `-h`	Change the permissions of symbolic links instead of the files they point to.
    - mode:
        - The “mode” helps in setting new permissions that have to be applied to files or directories.
        - `+`	Add permissions
        - `-`	Remove permissions
        - `=`	Set the permissions to the specified values
        - `r`	Read permission
        - `w`	Write permission
        - `x`	Execute permission
        - u	Owner
        - g	Group
        - o	Others
        - a	All (owner,groups,others)
    - example: 
        - Read, write and execute permissions to the file owner: chmod u+rwx [file_name]
        - 
    - Octal mode : It is also a method for specifying permissions. In this method we specify permission using three-digit number. Where..
        -  First digit specify the permission for Owner.
        - Second digit specify the permission for Group. 
        - Third digit specify the permission for Others. 
            - Value	Permission
            - 4	Read Permission
            - 2	Write Permission
            - 1	Execute Permission
        - example : chmod 674 [file_name]
            - 6 represent permission of file Owner which are (rw).
            - 7 represent permission of Group which are (rwx).
            - 4 represent permission of Other which is (r).

## glossory

### Files
```sh
tar · pv · cat · tac · chmod · grep ·  diff · sed · ar · man · pushd · popd · fsck · testdisk · seq · fd · pandoc · cd · $PATH · awk · join · jq · fold · uniq · journalctl · tail · stat · ls · fstab · echo · less · chgrp · chown · rev · look · strings · type · rename · zip · unzip · mount · umount · install · fdisk · mkfs · rm · rmdir · rsync · df · gpg · vi · nano · mkdir · du · ln · patch · convert · rclone · shred · srm · scp · gzip · chattr · cut · find · umask · wc · tr
```

### Processes
```sh
alias · screen · top · nice · renice · progress · strace · systemd · tmux · chsh · history · at · batch · free · which · dmesg · chfn · usermod · ps · chroot · xargs · tty · pinky · lsof · vmstat · timeout · wall · yes · kill · sleep · sudo · su · time · groupadd · usermod · groups · lshw · shutdown · reboot · halt · poweroff · passwd · lscpu · crontab · date · bg · fg · pidof · nohup · pmap
```
### Network
```sh
netstat · ping · traceroute · ip · ss · whois · fail2ban · bmon · dig · finger · nmap · ftp · curl · wget · who · whoami · w · iptables · ssh-keygen · ufw · arping · firewalld
```    
    
    
    
    
    