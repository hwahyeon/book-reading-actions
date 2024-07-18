# Markdown Issue Tracker
This repository contains a workflow script that automatically detects Markdown files in a specified folder, creates issues for each task listed, and closes issues as tasks are marked complete.


## Usage
1. Place your Markdown files in the `/books/` directory. Each Markdown file should follow this structure:

```markdown
# Book Title

**Labels:** label1, label2

- [ ] Chapter 1
- [ ] Chapter 2
- [x] Chapter 3
```
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
3. Once the workflow file is added to the repository, GitHub Actions will automatically run the script to scan the books folder, create issues for unchecked tasks, and close issues for checked tasks.

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



