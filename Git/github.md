# Git Clone Repository/ Commit / Push Changes 


**`Set up a GitHub Account`**

**Create an account in [github.com](http://github.com)**

**`If you haven’t done so already, make a GitHub.com account, it’s free! This is where you’ll be creating a repo and putting in files.  Once you’re in your GitHub account, click Create a repository (or New Repository), which will take you to a page where you can add details for your repo.`**

<img width="1094" alt="1" src="https://github.com/idkvarma/idk/assets/89244462/fd6e44eb-4948-4ef9-9091-846aac8511fc">

# Create a Repo ([Click Here](https://github.com/new))

**`Fill out the details for your repo and be sure to take note your repo name, you’ll need it later in this.`**

<img width="1367" alt="2" src="https://github.com/idkvarma/idk/assets/89244462/21846afd-b974-470f-b048-24bbdedfd8b7">

**`Once created, you’ll see two files in your repository if you chose the licensing and README file.`**

<img width="1375" alt="3" src="https://github.com/idkvarma/idk/assets/89244462/2a28097e-6cdb-4f95-814b-5002d6e845c6">

**`Installing Git in debian system Ex: UBUNTU`**

<img width="547" alt="7" src="https://github.com/idkvarma/idk/assets/89244462/148df264-0e19-46e7-b630-bec2fbfeae87">

# Create A Directory

**`When you create a directory, you can use this space to sync newly written/edited code to your GitHub account.`**

<img width="579" alt="8" src="https://github.com/idkvarma/idk/assets/89244462/5d26cecb-7446-44a3-b911-62fdd144c969">

**`After installing Git, configuration is needed for commit messages to be sent out.  Without setting the name and email address you’ll see warnings when making commitments to git. If you have multiple user who utilize git, make an entry for each user. You can easily set these details for a user with two commands within your server’s terminal. (If you need to access the information set you can find it in the .gitconfig file.)`**

![9](https://github.com/idkvarma/idk/assets/89244462/4f9b873d-a304-4a9c-9f94-2247b4082df0)

**`Copy your GitHub URL`**

**`First, its necessary to clone or download our already pre-existing README and licensing file from our GitHub account.  Jump back to your GitHub account, click Clone or download and copy your GitHub link.`**

<img width="1371" alt="10" src="https://github.com/idkvarma/idk/assets/89244462/cbd3f731-a409-4313-babc-6b8ac3c15b93">

# Clone your Repo

**`In your terminal, you should find yourself in the GitHub directory.  We will first clone our repo with our copied GitHub URL and then change directories to our project name.`**

**`By listing the student-folder directory, you’ll see the README.md file in your repo, verifying that the cloning has worked.`**

![11](https://github.com/idkvarma/idk/assets/89244462/7af5f5fa-d5c9-475d-af57-1396609611a2)

**`Now we will see how to commit and push changes to GitHUB`**

**`EX: Create a JavaScript File`**

![12](https://github.com/idkvarma/idk/assets/89244462/e9d0cc5c-fde3-4fcd-8434-cf254ebf7c05)

![13](https://github.com/idkvarma/idk/assets/89244462/c553277a-9b3d-40ae-8470-d8c8dfc16ccc)

**`Check the New Script's Status`**

```git status```

**`The output shows the file name highlighted in red, indicating the changes have not been pushed to GitHub from the terminal and the file is not tracked by Git.`**

![14](https://github.com/idkvarma/idk/assets/89244462/c2c71780-1f40-4209-9a33-e87d46f0e0a8)

**`Add an Index to GitHub`**

**`To add an index to GitHub so that Git tracks the script, use the git add command.`**

```git add .```

![15](https://github.com/idkvarma/idk/assets/89244462/bb411345-0772-46be-90fc-0743b4ae0458)

**`Check **`git status`** for better understanding`**

![16](https://github.com/idkvarma/idk/assets/89244462/213fdf79-0b63-4f67-a42c-c581bb21c109)

# Commit Changes to Local Repository

**`The following command commits your script to your local repository. Use this syntax.`**

**`git commit -m "First java program" helloworld.java`**

**`Committing the script changes uses the commit command followed by the -m flag. A description of the commit goes in quotes, followed by the file name. The following output is displayed.`**

![17](https://github.com/idkvarma/idk/assets/89244462/1859f81c-9674-46bc-8f6b-a131816ec6ac)

**`Before we push the chnages to GitHub we should create a access token in github.com`**

**`When ever we push a file from terminal it will ask your username & password so from next when ever it asks password while you push a file instead of giving GitHub password copy & paste access token key, please follow the screenshots.`**

<img width="753" alt="18" src="https://github.com/idkvarma/idk/assets/89244462/d4ff5245-5890-4601-a0b3-fa799085209f">

<img width="751" alt="20" src="https://github.com/idkvarma/idk/assets/89244462/54f3e34c-780a-4ad1-9831-a4e3c1794c48">

<img width="751" alt="21" src="https://github.com/idkvarma/idk/assets/89244462/2498391b-a468-41ac-80e3-9aba36e6bdd8">

<img width="751" alt="22" src="https://github.com/idkvarma/idk/assets/89244462/08b66ce1-7b9d-422d-85c4-13be6efd32b4">

<img width="750" alt="24" src="https://github.com/idkvarma/idk/assets/89244462/42b2001b-0613-40c2-8c14-00284cd6c99a">

<img width="746" alt="25" src="https://github.com/idkvarma/idk/assets/89244462/2f271f4a-ed77-4aac-8350-3b4781648628">

<img width="480" alt="26" src="https://github.com/idkvarma/idk/assets/89244462/c7794baa-7b9f-4c13-8a2a-3a8f126453d8">

<img width="748" alt="27" src="https://github.com/idkvarma/idk/assets/89244462/cc376824-0bde-4d9e-949b-4672a0d45d49">

**`Push Script/File to GitHub From Terminal`**

**`The git push command commits and records the changes to your remote repository or your GitHub account.`**

**`To push the script/file to GitHub from the terminal, use the following command.`**

```git push -u origin master```

You will receive a prompt for your GitHub account username and password. After logging in, the following output will display.`**


<img width="681" alt="28" src="https://github.com/idkvarma/idk/assets/89244462/2d21d58b-5609-4127-b438-88f05095f501">

**`Verify the Push`**

**`To verify the script commit on GitHub, log into the account. Refresh the screen for the particular repository if you are already logged in. It shows both the file name and the description provided.`**

<img width="926" alt="29" src="https://github.com/idkvarma/idk/assets/89244462/1c54ce6b-9f1a-458f-992e-623775c647a8">


