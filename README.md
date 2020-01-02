# auto-push-with-notifications
Hooks for windows 10 to automatically pushee the **entire** repository to remote upon commit.
Shows notifications of the pushing progress.

# requirements
* Windows 10
* Python 3
* [Windows 10 Tost Notifications](https://github.com/jithurjacob/Windows-10-Toast-Notifications)

# installation
* copy [hooks](https://github.com/pepeworld/auto-push-with-notifications/tree/master/hooks) folder to inside .git in your repository.

![CopyAnim](https://user-images.githubusercontent.com/56680359/71655339-2aead500-2d2e-11ea-8583-e84796b1e383.gif)

# usage
* commit your new changes, and the notifications will appear

![Notification](https://user-images.githubusercontent.com/56680359/71655497-ef043f80-2d2e-11ea-8f6a-cb2597418611.gif)

# To-Do
* find a way to validate that the push did happen
* notify if no changes were made, and thus a push didn't happen
* push the current branch only
