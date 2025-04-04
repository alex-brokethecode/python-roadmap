# Version Control (Git)

Can review a more detailed [guide of Git](https://github.com/iBrokeTheCode/git-tutorial/blob/main/README.md)

## Theory

Git is a distributed version control system that allows you to track changes in your code, collaborate with others, and revert to previous versions. 1 It's an essential tool for modern software development.

### Key Concepts

- **Repository (Repo):** A directory containing all your project files and the history of changes.
- **Commit**: A snapshot of your project at a specific point in time.
- **Branch**: A separate line of development.
- **Merge**: Combining changes from one branch into another.
- **Remote Repository:** A repository hosted on a server (e.g., GitHub, GitLab, Bitbucket).
- **Clone**: Creating a local copy of a remote repository.
- **Push**: Uploading local commits to a remote repository.
- **Pull**: Downloading changes from a remote repository to your local repository.
- Staging Area (Index): A place where you prepare changes for a commit.

### Basic Git Commands:

- `git init`: Initializes a new Git repository.
- `git clone <repository_url>`: Clones a remote repository.
- `git add <file>`: Adds a file to the staging area.
- `git commit -m "commit message"`: Creates a commit with the staged changes.
- `git status`: Shows the status of your working directory and staging area.
- `git log`: Shows the commit history.
- `git branch`: Lists branches.
- `git checkout <branch>`: Switches to a branch.
- `git merge <branch>`: Merges a branch into the current branch.
- `git remote add origin <repository_url>`: Adds a remote repository.
- `git push origin <branch>`: Pushes commits to a remote repository.
- `git pull origin <branch>`: Pulls changes from a remote repository.

### Example Workflow

- Initialize a repository: `git init`
- Create a file: `touch my_file.txt`
- Add the file to the staging area: `git add my_file.txt`
- Commit the changes: `git commit -m "Add my_file.txt"`
- Create a branch: `git branch my_branch`
- Switch to the branch: `git checkout my_branch`
- Make changes to the file: `echo "Hello, Git!" >> my_file.txt`
- Add the changes to the staging area: `git add my_file.txt`
- Commit the changes: `git commit -m "Modify my_file.txt"`
- Switch back to the main branch: `git checkout main`
- Merge the branch: `git merge my_branch`
- Push the changes to a remote repository: `git push origin main`
