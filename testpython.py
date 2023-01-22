from github import Github

print("hello world - inside python script")

g = Github(base_url="https://github.com/api/v3", login_or_token="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")
repo = g.get_user().get_repo("helllo-world")
print(repo.full_name)
contents = repo.get_contents("README.md", ref="main")
print(contents)
response = repo.update_file(contents.path, "pygithub-test-from-local", "temp data", contents.sha, branch="main")
print(response)