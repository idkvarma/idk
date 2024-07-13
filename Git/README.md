
# Git Commands Reference

This README.md file serves as a reference guide for Git commands categorized by proficiency level.

Here's a table outlining Git commands categorized from basic to advanced/professional levels:




## Basic Commands

| Command                   | Description                                                  | Example Usage                                               |
|---------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| `git init`                | Initialize a new Git repository.                              | `git init`                                                  |
| `git clone <repository-url>` | Clone a repository from a remote server.                     | `git clone https://github.com/user/repo.git`                |
| `git add <file>`          | Stage changes for commit.                                     | `git add file.txt`                                          |
| `git commit -m "Commit message"` | Record changes to the repository.                        | `git commit -m "Add feature X"`                              |
| `git status`              | Show the status of files in the repository.                   | `git status`                                                |
| `git log`                 | Show commit logs.                                             | `git log`                                                   |
| `git push`                | Update remote refs along with associated objects.              | `git push origin main`                                      |
| `git pull`                | Fetch from and integrate with another repository or a local branch. | `git pull origin main`                                   |

## Intermediate Commands

| Command                   | Description                                                  | Example Usage                                               |
|---------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| `git branch`              | List, create, or delete branches.                             | `git branch`                                                |
| `git checkout <branch-name>` | Switch branches or restore working tree files.              | `git checkout development`                                  |
| `git merge <branch-name>` | Join two or more development histories together.               | `git merge feature-branch`                                  |
| `git rebase <branch-name>` | Reapply commits on top of another base tip.                 | `git rebase main`                                           |
| `git fetch <remote>`      | Download objects and refs from another repository.            | `git fetch origin`                                          |
| `git remote`              | Manage set of tracked repositories.                           | `git remote -v`                                             |
| `git stash`               | Stash changes in a dirty working directory.                   | `git stash`                                                 |

## Advanced/Pro Commands

| Command                   | Description                                                  | Example Usage                                               |
|---------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| `git cherry-pick <commit>` | Apply changes introduced by some existing commits.           | `git cherry-pick abc123`                                    |
| `git reset <commit>`      | Reset current HEAD to the specified state.                    | `git reset HEAD~2`                                          |
| `git reflog`              | Manage reflog information.                                    | `git reflog`                                                |
| `git bisect`              | Use binary search to find the commit that introduced a bug.  | `git bisect start`                                          |
| `git submodule`           | Initialize, update or inspect submodules.                     | `git submodule update --init`                                |
| `git filter-branch`       | Rewrite branches to remove commits.                           | `git filter-branch --tree-filter 'rm -rf path/to/unwanted' HEAD` |
| `git worktree`            | Manage multiple working trees attached to the same repository.| `git worktree add ../branch-2 branch-2`                     |

## Expert/Pro Commands

| Command                   | Description                                                  | Example Usage                                               |
|---------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| `git notes`               | Add or inspect object notes.                                  | `git notes add -m "Note message"`                            |
| `git rerere`              | Reuse recorded resolution of conflicted merges.               | `git rerere`                                                |
| `git fsck`                | Verifies the connectivity and validity of the objects in the database. | `git fsck --full`                                        |
| `git bundle`              | Move objects and refs by archive.                             | `git bundle create repo.bundle master`                       |
| `git archive`             | Create an archive of files from a named tree.                 | `git archive --format=tar --output=repo.tar master`         |
| `git bisect--helper`      | Manage a bisect session.                                      | `git bisect--helper`                                        |

