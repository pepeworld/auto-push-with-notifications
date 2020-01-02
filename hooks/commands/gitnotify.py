# include standard modules
import argparse
import subprocess
from win10toast import ToastNotifier


# initiate notifier
notifier = ToastNotifier()
# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-pp", "--prepush", help="show program version", action="store_true")
parser.add_argument("-pr", "--postreceive", help="show program version", action="store_true")

# read arguments from the command line
args = parser.parse_args()

# get repo name
repoPath = subprocess.Popen("git rev-parse --show-toplevel", stdout=subprocess.PIPE).stdout.readline().decode().split('/')
repoName = repoPath[len(repoPath)-1]

# get vscode icon
iconPath = ".git/hooks/commands/vscode.ico"

# arguments responses
if args.prepush:
    notifier.show_toast(repoName, "pushing commit... ", duration=2, icon_path=iconPath)

if args.postreceive:
    notifier.show_toast(repoName, "commit pushed! ✔️", duration=2, icon_path=iconPath)
