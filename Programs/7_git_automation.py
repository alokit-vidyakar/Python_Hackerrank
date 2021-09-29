from github import Github
g= Github("vidyakaralokit@gmail.com","Github67@#")
#repos =g.search_repositories()
rep = g.get_user().get_repos("Python_Hackerrank")
print(rep)
rep.get_contents("/Programs/7_git_automation.py")