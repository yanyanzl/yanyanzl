# Conda Basics


### conda activate myenv

- To retain the current environment in the PATH, you can activate the new environment using:
 
### conda activate --stack myenv



### To see a list of all of your environments,run:

- conda info --envs Or
- conda env list

### Viewing a list of the packages in an environment

- If the environment is not activated, in your terminal window or an Anaconda Prompt, run:

- conda list -n myenv

- If the environment is activated, in your terminal window or an Anaconda Prompt, run:

- conda list

### To see if a specific package is installed in an environment, in your terminal window or an Anaconda Prompt, run:

conda list -n myenv scipy
