from github_adapter import get_github_tree_of

def get_all_paths(tree):
    files = list(map(lambda x: x['path'], tree))
    return files    

def get_files_endswith(endswith, owner, repo, branch, token):      
    tree = get_github_tree_of(owner, repo, branch, token)

    if(tree == {}):
        print(f"Error: can't get the github tree for {owner}/{repo}@{branch}")
        return
    
    paths = get_all_paths(tree)
    filtered_paths = filter(lambda x: x.endswith(endswith), paths)
    return list(filtered_paths)
