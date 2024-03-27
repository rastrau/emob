git checkout --orphan temp d925dbaeebc00b54afb8d410e9eb1442467ac932 # create a new branch without parent history from commit d925dbaeebc00b54afb8d410e9eb1442467ac932 (adjust this commit ID)
git commit -m "Truncated history" # create a first commit on this branch
git rebase --onto temp d925dbaeebc00b54afb8d410e9eb1442467ac932 main # now rebase the part of master branch that we want to keep onto this branch
git branch -D temp # delete the temp branch
git prune --progress # delete all the objects w/o references
git gc --aggressive # aggressively collect garbage; may take a lot of time on large repos
git push origin --force