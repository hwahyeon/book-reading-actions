import os
import re
import json
from github import Github
from pathlib import Path

def main():
    token = os.getenv('GITHUB_TOKEN')
    repo_name = os.getenv('GITHUB_REPOSITORY')
    g = Github(token)
    repo = g.get_repo(repo_name)
    
    issues_file = Path('issues.json')
    if issues_file.exists():
        with issues_file.open('r', encoding='utf-8') as f:
            issues_data = json.load(f)
    else:
        print("Issues data file not found.")
        return

    books_path = Path('books')
    for md_file in books_path.glob('*.md'):
        with md_file.open('r', encoding='utf-8') as file:
            content = file.read()
            book_title = content.split('\n')[0].strip('#').strip()
            print(f"Processing book: {book_title}")

            if book_title not in issues_data:
                continue

            chapters_to_close = re.findall(r'- \[x\] (.+)', content)
            for chapter in chapters_to_close:
                chapter = chapter.strip()
                if chapter in issues_data[book_title]:
                    issue_number = issues_data[book_title][chapter]
                    issue = repo.get_issue(number=issue_number)
                    if issue.state != 'closed':
                        issue.edit(state='closed')
                        print(f"Closed issue: {issue.title}")

if __name__ == "__main__":
    main()