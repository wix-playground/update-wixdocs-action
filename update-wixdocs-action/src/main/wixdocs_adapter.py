import requests

def update_wixdocs(path, owner, repo, wixdocs_api):
    full_path = f"{repo}/{path}"
    headers = {"Content-Type": "application/json"}
    data = {"org": owner, "url": full_path}
    
    response = requests.post(wixdocs_api, data=data, headers=headers)
    print(f"wixdos api response for {owner}/{full_path}: status - {response} content - {response.content}")

def update_wixdocs_with(paths, owner, repo, wixdocs_api):
    for path in paths:
        update_wixdocs(path, owner, repo, wixdocs_api)
