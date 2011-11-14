cd myapp
rm -rf `find . -mindepth 2 -name .git`
git rm --cache `git submodule | cut -f2 -d' '`
git rm .gitmodules
git add .
git config -l | grep '^submodule' | cut -d'=' -f1 | xargs -n1 git config --unset-all
git commit -m "brought submodules into the main repo"
