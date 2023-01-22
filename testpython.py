from github import Github

print("hello world - inside python script")

g = Github(base_url="https://github.com/api/v3", login_or_token="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")

repo = g.get_user().get_repo("hello-world")
print(repo.full_name)
contents = repo.get_contents("README.md", ref="main")
print(contents)
response = repo.update_file(contents.path, "pygithub-test-from-local", "temp data", contents.sha, branch="main")
print(response)
