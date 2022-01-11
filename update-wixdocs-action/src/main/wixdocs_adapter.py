import requests

def update_wixdocs(path, owner, wixdocs_api):
    headers = {"Content-Type": "application/json"}
    data = {"org": owner, "url": path}
    
    response = requests.post(wixdocs_api, data=data, headers=headers)
    print(f"wixdos api response for {owner}/{path}: status - {response} content - {response.content}")

def update_wixdocs_with(paths, owner, wixdocs_api):
    for path in paths:
        update_wixdocs(path, owner, wixdocs_api)
