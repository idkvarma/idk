
# Git Commands Reference

This README.md file serves as a reference guide for Git commands categorized by proficiency level.

Here's a table outlining Git commands categorized from basic to advanced/professional levels:

## Basic Commands

| Command                   | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| `git init`                | Initialize a new Git repository.                              |
| `git clone <repository-url>` | Clone a repository from a remote server.                    |
| `git add <file>`          | Stage changes for commit.                                     |
| `git commit -m "Commit message"` | Record changes to the repository.                        |
| `git status`              | Show the status of files in the repository.                   |
| `git log`                 | Show commit logs.                                             |
| `git push`                | Update remote refs along with associated objects.              |
| `git pull`                | Fetch from and integrate with another repository or a local branch. |

## Intermediate Commands

| Command                   | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| `git branch`              | List, create, or delete branches.                             |
| `git checkout <branch-name>` | Switch branches or restore working tree files.              |
| `git merge <branch-name>` | Join two or more development histories together.               |
| `git rebase <branch-name>` | Reapply commits on top of another base tip.                 |
| `git fetch <remote>`      | Download objects and refs from another repository.            |
| `git remote`              | Manage set of tracked repositories.                           |
| `git stash`               | Stash changes in a dirty working directory.                   |

## Advanced/Pro Commands

| Command                   | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| `git cherry-pick <commit>` | Apply changes introduced by some existing commits.           |
| `git reset <commit>`      | Reset current HEAD to the specified state.                    |
| `git reflog`              | Manage reflog information.                                    |
| `git bisect`              | Use binary search to find the commit that introduced a bug.  |
| `git submodule`           | Initialize, update or inspect submodules.                     |
| `git filter-branch`       | Rewrite branches to remove commits.                           |
| `git worktree`            | Manage multiple working trees attached to the same repository.|

## Expert/Pro Commands

| Command                   | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| `git notes`               | Add or inspect object notes.                                  |
| `git rerere`              | Reuse recorded resolution of conflicted merges.               |
| `git fsck`                | Verifies the connectivity and validity of the objects in the database. |
| `git bundle`              | Move objects and refs by archive.                             |
| `git archive`             | Create an archive of files from a named tree.                 |
| `git bisect--helper`      | Manage a bisect session.                                      |
