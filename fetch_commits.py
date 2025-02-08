import requests as request

url= 'https://api.github.com/repos/torvalds/linux/commits'
response = request.get(url)
if response.status_code == 200:
    commits = response.json()
    recent_commits = commits[:10]
    print("Recent Commits:")
    for commit in recent_commits: 
        message = commit["commit"]["message"]
        author = commit["commit"]["author"]["name"]
        print(f"Author: {author} \nMessage: {message} \n\n\n")
else:
    print(f"Error: {response.status_code}")

