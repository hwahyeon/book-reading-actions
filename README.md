# Markdown Issue Tracker
This repository contains a workflow script that automatically detects Markdown files in a specified folder, creates issues for each task listed, and closes issues as tasks are marked complete.


## 🔴Important Notice
The default GitHub Actions token (`GITHUB_TOKEN`) prevents new workflows from being triggered by actions it performs. This means that if you create or modify issues using `GITHUB_TOKEN`, other workflows will not detect and execute these actions. This is to prevent infinite loops and enhance security.

**Example**
1. **Workflow A**: Uses `GITHUB_TOKEN` to create a new issue.
2. **Expected Trigger**: Normally, creating a new issue would trigger **Workflow B** to run.
3. **Actual Result**: Issues created using `GITHUB_TOKEN` do not trigger **Workflow B**.

Therefore, this repository is intended for situations where you cannot use a Personal Access Token. If you want full issue tracking functionality, please move to [this repository](https://github.com/hwahyeon/book-reading-actions-ptk), which is configured to use a Personal Access Token.

## Usage

1. Configure Actions Permissions:
    1. Click on the `Settings` tab of the repository where you want to apply this workflow.
    2. Click `Actions` under `Code and automation`.
    3. Under `Actions permissions`, select `Allow all actions and reusable workflows`.
    4. Under `Workflow permissions`, select `Read and write permissions`.

2. Create a workflow file named `use-common-workflow.yml` in the `/.github/workflows` directory of your repository with the following content:
```yml
name: Use Common Workflow

on:
  push:
    paths:
      - 'books/**.md'
  workflow_dispatch:

jobs:
  callCommonWorkflow:
    uses: hwahyeon/book-reading-actions/.github/workflows/common-workflow.yml@main
    secrets: inherit
```


3. Place your Markdown files in the `/books/` directory. Each Markdown file should follow this structure:

```markdown
# Book Title

**Labels:** label1, label2

- [ ] Chapter 1
- [ ] Chapter 2
- [x] Chapter 3
```

4. Once the workflow file is added to the repository and changes are committed, GitHub Actions will automatically run the script to scan the books folder, create issues for unchecked tasks, and close issues for checked tasks.

5. Go to the `Actions` tab in your repository and ensure the workflow is enabled and configured correctly.

## Example
Given a Markdown file named `example_book.md` in the `/books/` folder with the following content:
```markdown
# Book Title

**Labels:** reading, example

- [ ] Chapter 1: Introduction
- [ ] Chapter 2: Getting Started with Examples
- [x] Chapter 3: Advanced Example
```

The script will:
- Create issues for "Introduction" and "Chapter 1" with titles in the format `[Book Title] Chapter: Chapter Title`, such as `[Example Book] Chapter1: Introduction`.
- Attach the specified labels (`reading`, `example`) to the created issues.
- Not create an issue for "Chapter 2" since it is marked as completed.
- Close the issue for "Chapter 2" if it is open.

## Markdown Issue Tracker GitHub Action Flowchart
```text
Start (Push to Repository / Manual Trigger)
          ↓
Check for Markdown File Changes in 'books' Directory
          ↓
Changed Markdown Files Found?  ----→ No ----→ End
          ↓
          Yes
          ↓
Load Issues Data from 'issues.json'
          ↓
Issues File Exists?  ----→ No ----→ Initialize Issues Data
          ↓
          Yes
          ↓
For Each Changed Markdown File:
          ↓
Extract Book Title and Labels
          ↓
Extract Unchecked Chapters
          ↓
For Each Unchecked Chapter:
          ↓
Issue Already Exists in issues.json? ----→ Yes ----→ Skip
          ↓
          No
          ↓
Create Issue with Labels
          ↓
Add New Issue Number to issues.json
          ↓
Extract Checked Chapters
          ↓
For Each Checked Chapter:
          ↓
Issue Already Exists and Open? ----→ No ----→ Skip
          ↓
          Yes
          ↓
Close Issue
          ↓
Remove Issue from issues.json
          ↓
Save Updated issues.json
          ↓
End
```
