import sys
import os
from paths_filter import get_files_endswith
from wixdocs_adapter import update_wixdocs_with 

def extract_details_from(repo_details_string):
    #  format of repo_details_string: OWNER/REPO@BRANCH
    owner, repo_and_branch = repo_details_string.split('/')

    if not ('@' in repo_and_branch):
        repo_and_branch += '@master'

    repo, branch = repo_and_branch.split('@')
    
    return owner, repo, branch

def main():    
    token = None if sys.argv[1] == "no-token" else sys.argv[1]
    wixdocs_api = sys.argv[2]

    repo_full_name = os.getenv("GITHUB_REPOSITORY")
    
    print(repo_full_name)
    
    owner, repo = repo_full_name.split("/")
    branch = "master"
    endswith = "wixdocs.yaml"
    print("owner, repo, branch, endswith:", owner, repo, branch, endswith)

    paths = get_files_endswith(endswith, owner, repo, branch, token)
    print(paths)

    update_wixdocs_with(paths, owner, repo, wixdocs_api)

if __name__ == "__main__":
    main()
