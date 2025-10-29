import os
import sys
from bs4 import BeautifulSoup
from datetime import datetime
from collections import defaultdict
import html2text
from dateutil import parser

def parse_html(file_path):
    """Parse the HTML file and extract necessary elements."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        
    title_tag = soup.find('div', class_='title')
    title = title_tag.text.strip() if title_tag else None
    
    heading_tag = soup.find('div', class_='heading')
    creation_time = heading_tag.text.strip() if heading_tag else None
    
    try:
        parsed_time = parser.parse(creation_time) if creation_time else datetime.now()
    except (parser.ParserError, TypeError, ValueError):
        parsed_time = datetime.now()  # Use current time if parsing fails
    
    chips_div = soup.find('div', class_='chips')
    tags = [chip.text.strip() for chip in chips_div.find_all('span', class_='label-name')] if chips_div else []
    
    content_div = soup.find('div', class_='content')
    content = html2text.html2text(str(content_div)) if content_div else ''
    
    attachments_div = soup.find('div', class_='attachments')
    attachments = [img['src'] for img in attachments_div.find_all('img')] if attachments_div else []

    return {
        'title': title,
        'creation_time': parsed_time,
        'tags': tags,
        'content': content,
        'attachments': attachments
    }

def format_markdown(data):
    """Convert extracted data into Markdown format."""
    markdown = []
    markdown.append(f"# {data['title'] if data['title'] else 'Untitled'}\n")
    markdown.append(f"**Created:** {data['creation_time'].strftime('%Y-%m-%d %H:%M:%S')}\n")
    if data['tags']:
        tags_links = ' '.join([f"[[{tag}]]" for tag in data['tags']])
        markdown.append(f"**Tags:** {tags_links}\n")
    markdown.append(data['content'] + "\n")
    if data['attachments']:
        for attachment in data['attachments']:
            markdown.append(f"![{os.path.basename(attachment)}]({attachment})\n")
    return '\n'.join(markdown)

def save_markdown(data, output_dir, date_count_dict):
    """Save the Markdown formatted data into a file with specific naming convention."""
    date_str = data['creation_time'].strftime('%Y-%m-%d')
    title = data['title'] if data['title'] else clean_content(data['content'])
    title = title.replace('/', '-').replace('\\', '-')  # Sanitize title
    count = date_count_dict[date_str]
    filename = f"{date_str} - {title} ({count}).md" if count > 1 else f"{date_str} - {title}.md"
    date_count_dict[date_str] += 1
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as file:
        file.write(format_markdown(data))

def clean_content(content):
    """Clean and truncate content for use as a filename."""
    clean = ' '.join(content.split())[:30]  # Remove excessive whitespace, truncate to 30 chars
    return ''.join(c for c in clean if c.isalnum() or c in ' -_').strip()

def main():
    # TODO: paste the path to the folder containing your Keep HTML exports.
    input_dir = ""  # Example: "/path/to/your/html_files"
    
    # TODO: paste the path to the folder where Markdown files should be written.
    output_dir = ""  # Example: "/path/to/your/markdown_files"
    
    if not input_dir or not output_dir:
        raise ValueError("input_dir and output_dir must be set before running the script.")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    html_files = [f for f in os.listdir(input_dir) if f.endswith('.html')]
    print(f"Total HTML files detected: {len(html_files)}")

    # Read command-line argument for the number of files to process
    num_files_to_process = int(sys.argv[1]) if len(sys.argv) > 1 else len(html_files)
    
    date_count_dict = defaultdict(int)
    
    for html_file in html_files[:num_files_to_process]:
        file_path = os.path.join(input_dir, html_file)
        try:
            data = parse_html(file_path)
            save_markdown(data, output_dir, date_count_dict)
            print(f"Converted {html_file} to Markdown")
        except Exception as e:
            print(f"Failed to convert {html_file}: {e}")

if __name__ == "__main__":
    main()
