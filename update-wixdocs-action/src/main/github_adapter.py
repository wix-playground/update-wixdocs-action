import requests

def get_github_tree_of(owner, repo, branch, token=None):
    url = f'https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1'
    print("url:", url)

    headers = {}
    
    if token:
        print("There is a token")
        headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    print("response:", response)

    if response.status_code != requests.codes.ok:
        return {}
    
    return response.json()['tree']
