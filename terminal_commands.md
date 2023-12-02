# commands used in the terminal
## basic commands used daily 

1. cat

2. ls

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
    
13 super user command: sudo vi /etc/paths

14 input and output stream
>   Use a right angle bracket to redirect command output to a file.

<   Use a left angle bracket to use the contents of a file as input to the command.

>>  Use two right angle brackets to append output from a command to a file.

the following command passes the formatted contents of the zsh man page to the grep tool, which searches the contents for lines containing the word commands. The result is a list of lines with the specified text, instead of the entire man page.
% man zsh | grep commands


Standard pipes include:
stdin: The standard input pipe is where a command receives input. By default, you enter input from the command-line interface. You can redirect the output from files or other commands to stdin.

stdout: The standard output pipe is where command output is sent. By default, command output is sent to the command line. You can redirect the output from the command line to other commands and tools.

stderr: The standard error pipe is where error messages are sent. By default, errors are displayed on the command line along with standard output.