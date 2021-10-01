#ssh key is added
#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
import git
import os
from github import Github
g = Github("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")

""" g.get_user() is bit lazy load kind of. So printing u will give not give your user-name. 
Instead try logging in first in order to get output"""

"""u=g.get_user()
login = u.login
print(u)"""

for repos in g.get_user().get_repos():
	"""print(repos.name,":",repos.stargazers_count)
	content = repos.get_contents("")"""
	#print("repos are: ",repos)	
	#print(*(repos.get_labels()))

"""repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha
print(sha)"""
repo = g.get_repo("alokit-vidyakar/Python_Hackerrank")
branches = list(repo.get_branches()) # get branches
print(branches)
branch = repo.get_branch(branch ="test") #get a particular branch for the repo
print(branch)
content = repos.get_contents("")
print(content)
#I get a list of all commit ids
#for all_commits
commit = repo.get_commit(sha="88d015355eab103011305c6fbf4f407bba31ff30")
print(commit.commit.author.date)
