# Adventures_of_the_4_MATEs


Instructions for contributing code
Before making any changes, I suggest making sure your local main is up to date by following steps 4-7.

Create your branch (replace "my_branch" with your name or the feature you're adding).

git checkout -b my_branch
Once you've made your changes, go ahead and stage them.
git add .
Commit your changes and choose a meaningful message summarizing what your changed (replace "commit message" below with your message).
git commit -m "commit message"
Checkout to main branch.
git checkout main
Update your local main branch.
git pull
Switch to your branch (substitute "my_branch" below with whatever you named your branch).
git checkout my_branch
Bring your branch up to date with main.
git rebase main
Push your changes to your remote branch (remember to replace "my_branch" with your branch name).
git push origin my_branch
Once you see your branch has updated on Github, create a pull request and ask someone to review your code.
After your PR approved, merge your branch and you're done.
