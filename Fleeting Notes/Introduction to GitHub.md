2022-04-03 10:00
Status: #idea
Tags: #idea/Git

# Introduction to GitHub
I found GitHub is only for the software developers whixh it is. It is a very helpful tool in managing versions of the softwares. You could just push the software directly from the PC on to the Git using some commands..
https://opensource.com/article/18/1/step-step-guide-git
The web site has an introduction to it, but it may be a bit old i guess, espcially while pushing the code to the hub it uses a username and password instead a autorisation key which you can create on the website itself. just paste it in the userid and just press enter for password.

The commands i used.
Echo "your text here" >>Readme.md
adding Your text here into the readme.md file
add the readme.md to git 
git commit "Comment"
git -m push Readme.md


git add .
git commit -q -m "Last Sync : $(date + "%Y-%m-%d %H:%M:%S")"
git push -q
here use the autentication token for your username and for password just enter. Thats it !!


[[Introduction to GitHub]]



26.06.22 :- **Git and GitHub for Beginners - Crash Course** -- https://www.youtube.com/watch?v=RGOj5yH7evk

What is Git?
Git is a Version Control system.

What is version contol? 
collection of information. go back in time.

### Terms:-
- **Directory** -> Folder
- **Terminal or command line** -> Interface for text commands
- **CLI** -> Command line interface
- **cd** -> chane Directory. like double click in GUI
- **code Editor** -> Word Processor for writing code
- **repository** -> Project, or the folder/ place where your project is kept
- **Github** -> A website to host your repositories online
- **Git** -> is the **tool** that keeps the versions etc

### Git Commands:-
- **Clone** -> Bring a repository that is hosted somewhere like Github into folder on your local machine.
- **add** -> Track your files and changes in Git.
- **commit** -> Save your files in Git
- **push** -> Upload Git commits to remote rep, like Github, bitbucket, gitlab
- **pull** -> Downloads changes from remote repo to your local machine, the opposite of push.


- git status:- This will tell all the files that are modified that are not in Git
- "git add ." :-  the perios in the end is telling git to add all the files, instead of all you can tell the specific file
- ( git commit -m "->your title of message" -m "-> some description") The first m is the message, you can see it is same as in the website when you do it manual from the Github. We only saved it locally not in the remote repository hub online- you need to push

### ssh setup:- 
- you need to tell hub that your can push-- SSH key--> ( ssh-keygen -t rsa -b 4096 -C "email@example.com") 
	 ssh-keygen:- command
	 -t rsa :- type of encryption
	  -b 4096:- the strength of encription
	  my key is "saikey"- Sreenavya
- to search for the key:- ls | grep saikey
	saikey -> private key (not shared, saved in the local machine)
	saikey.pub -> public key (shared)


eval `ssh-agent`

Agent pid 21614

 > I couldnt make the agent add in to the local ssh 

git pull -> it is used to get the code from the github in to the local machine. if you donot have the rights then you need to add a pull request. 

**Steps to add new repository from local machine:-**
- git remote add origin -link of repository-   
- git remote -v
- git push  -u origin master -> // -u is used to upstream in futher to not write origin master.

###   Git Branching
New feature or tryouts are made easy in a branch but commiting in to the main workflow. 
- Master branch:- Main or default branch- everything will be in one all the code.
- feature branch:- code on master and feature will be the same, if changes made on the feature branch are not made in the master.
- hut fix branch:- bugs  
![[Git_Branching.png]]


**Commands:-**
- *git checkout -b feature-readme-instruction*:- ceates a new branch called feature read-me-instructions.
- git branch:- check which branch you are in.
- git checkout master:- will switch between the braches
- git diff :- will show what changes are made, in the Hub + - signs are indicated which are added and which are removed.
- git merge feature-readme-instruction:- will merge to the master branch.
-  git pull origin master :- if upstream is not set. :- "-u"
- git branch -d feature-readme-instructions:- delete the branch

- if the files are modified not newly created one:- git commit -am "updated added"
- staching is a tempereay storing the data, if you are switching the branches before the commit.

### undoing Git
after staging the files using git add file name- use git reset to unstage.
you can also do reset after commit-- git reset HEAD~1 
git log -> to show the all commits with the HASH
git reset HASH-> hash is the key that computer understands shown in log

**Forking**
it is going to make a copy of the rep. if you dont have acces to a repo or do a PR(pull request) you need to fork it.
![[git_Groups.png]]
after forking you will have a complete acces to the code and merge it in your  master repo
# References
