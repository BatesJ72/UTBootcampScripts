# Why set up SSH
Private repos.

# Setting Up SSH
You only have to do this once in a instance.

How to connect to GitHub with ssh:
1) Generate an ssh key by running `ssh-add` and accepting the defaults by leaving them blank and pressing the enter key.
2) Get your public ssh key and copy it to your clipboard. One way to do this is by running `cat ~/.ssh/id_rsa` to open the public key file, display its contents, and then copy with the mouse and keyboard.
3) Go to github.com and log in.
4) Click your profile image in the top right and then click "Settings".
5) On the left-hand side, click "SSH and GPG keys"
6) On the top right, click "New SSH key"
7) Set the title to whatever you like. The "Title" is your choice, but it will help you identify what computer this authorization authorizes. Paste the copied key into the "Key" field and press "Add SSH key".
8) Go back to your computer and run  `eval `ssh-agent -s`` to start your ssh authentication agent.
9) Run `ssh-add ~/.ssh/id_rsa` to add you private key so that the agent can authenticate the public key.
10) Set your git configuration so that GitHub knows who you are by running `git config --global user.email you@email.com` and `git config --global user.name username`, where the email and username correspond to the ones you used to make your GitHub account.
