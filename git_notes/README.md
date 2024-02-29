## Git

![img.png](img.png)

- Version Control:
    - Working on a document, got  a new version and don’t want to lose first one so save as new, can end up with loads of drafts
    - git is the industry standard of version control. It’s distributed: local copies on everyone’s machine that are independent until pushed back up.
    - Folder with document in:
        1. git init to make it a repo (repo adds tracking to the folder .git) -initialise
        2. git add: I want to stage these changes - putting changes into cardboard box
        3. git commit: added all changes need and add a label to it. git commit -m to add a message, always do this. Committing to this part being done - take a git snapshot
        4. commit often to keep track of work
    - Create a specific git folder
    - Don’t nest repos
    - Try to keep an organised easy to navigate file system
- GitHub:
    - Dropbox for GitHub
    - clone down a project from git
    - git push to push it to GitHub
    - git pull to get latest changes from GitHub

- HEAD is a reference / marker to most recent commit
- `git diff <old-commit-id> <new-commit-id>`
  - Second commit 2c542af4a5778ee95fb76f0eaafce380210e97bf 
  - first commit 6bd6adde35c05eb81c7a9a12f8ffe7bfe61615ab
     - `git diff 6bd6adde35c05eb81c7a9a12f8ffe7bfe61615ab 2c542af4a5778ee95fb76f0eaafce380210e97bf`
    
- View previous commits versions of file folders
    - `git checkout <old-commit-id>`
        - Switched you to the old version
        - Detached commit - we’ve forced it to go to a previous commit, detatched head, not the latest version.
- Reverting to previous commit (lose changes made after this commit) (**DANGEROUS**)
    - `git reset --hard <commit-id>`