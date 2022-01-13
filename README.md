# Update WixDocs GitHub Action

## The Pain/Problem
There are some repos that don't run `Bazel`, so when we update wixdocs yaml file, wixdocs won't update automatically.
This action will update wixdocs in every push to master, by posting all the files that ends with `.wixdocs.yaml` to wixdocs API

## How to Use
Add new .yml file under `.github/workflows` directory in your repo:

```yml
name: Update WixDocs
on: 
  push:
    branches:
      - master

jobs:
  build:
    name: Update WixDocs API
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v1
      - uses: wix-playground/update-wixdocs-action/update-wixdocs-action@master
        with:
          TOKEN: ${{ secrets.GITHUB_TOKEN }}
          WIXDOCS_API: "<WIX-DOCS-API>"

```
---
**NOTE**
You need to replace `<WIX-DOCS-API>` with the WixDocs API endpoint, you can find that [here](https://github.com/wix-private/p13n/blob/master/wixplorer/docs-internal-rnd/guides/How%20to%20Generate%20Documentation.md#manual-update-by-post-request)
___
