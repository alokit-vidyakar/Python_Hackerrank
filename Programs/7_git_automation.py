from github import Github
g= Github("vidyakaralokit@gmail.com","Github67@#")
#repos =g.search_repositories()
for repo in g.get_user().get_repos():
	print(repo)