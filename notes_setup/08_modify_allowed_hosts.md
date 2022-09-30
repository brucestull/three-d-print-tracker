# Modify ALLOWED_HOSTS

## Resources:
* [Deploy a Django App to Heroku - Video - Pretty Printed](https://www.youtube.com/watch?v=GMbVzl_aLxM)

## Process:

1. Edit `ALLOWED_HOSTS` property in `production.py` ([production.py](../print_tracker/settings/production.py)) to include the heroku application root domain:  
    `ALLOWED_HOSTS = ['totally-new-heroku-app-name.herokuapp.com']`

1. Git `add`, `commit`, and `push` to `origin` (the repository created earlier):  
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> git status
        On branch main
        Your branch is up to date with 'origin/main'.

        Changes not staged for commit:
        (use "git add <file>..." to update what will be committed)
        (use "git restore <file>..." to discard changes in working directory)
                modified:   print_tracker/settings/production.py

        no changes added to commit (use "git add" and/or "git commit -a")
        PS C:\Users\Bruce\Programming\my-local-repository> git add .
        PS C:\Users\Bruce\Programming\my-local-repository> git commit -m "Changed 'ALLOWED_HOSTS' in 'production.py'."
        [main 8d5c94b] Changed 'ALLOWED_HOSTS' in 'production.py'.
        1 file changed, 1 insertion(+), 1 deletion(-)
        PS C:\Users\Bruce\Programming\my-local-repository> git push
        Enumerating objects: 9, done.
        Counting objects: 100% (9/9), done.
        Delta compression using up to 8 threads
        Compressing objects: 100% (5/5), done.
        Writing objects: 100% (5/5), 486 bytes | 486.00 KiB/s, done.
        Total 5 (delta 4), reused 0 (delta 0), pack-reused 0
        remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
        To https://github.com/brucestull/new-remote-repository.git
        0aa205e..8d5c94b  main -> main
        ```

1. Proceed to [Push to Heroku and Create Superuser](09_push_to_heroku_and_createsuperuser.md)

## Repository Links:
[README.md](../README.md)
