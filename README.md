Here's a cleaned-up version that keeps the self-aware tone but delivers it with PM clarity and engineering competence:

```markdown
# Keep to Markdown

A Python script that converts exported Google Keep HTML files into clean Markdown notes. Works locally, outputs to standard `.md` format, and integrates smoothly with Obsidian, Fleeting Notes, or any Markdown-based system.

## What it does

Processes Google Keep Takeout exports and generates properly formatted Markdown files. Handles titles, timestamps, labels, content blocks, and image references. File naming follows a consistent `YYYY-MM-DD - Title.md` pattern for easy sorting and search.

Currently command-line only. Web-based version with UI planned for later.

## Features

- Converts Keep HTML exports to Markdown with preserved metadata
- Maintains creation dates, labels, and inline image references
- Configurable batch processing via CLI argument
- No external services required—runs entirely locally

## Requirements

- Python 3.9+
- `beautifulsoup4`
- `html2text`
- `python-dateutil`

Install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Setup

1. Export your Keep notes from [takeout.google.com](https://takeout.google.com)
2. Extract the archive and locate the folder containing `.html` files
3. Edit `convert_keep_to_md.py` and set your paths:

```python
input_dir = ""   # Path to extracted Keep folder
output_dir = ""  # Destination for Markdown files
```

Path configuration is currently manual. Web UI will handle this automatically in future release.

## Usage

```bash
python convert_keep_to_md.py [optional_limit]
```

- Run without arguments to process all files
- Pass an integer (e.g., `25`) to convert only the first N files

Output files use format: `YYYY-MM-DD - Note Title.md`

Image references point to original attachment paths—keep the attachments folder structure intact to maintain working links.

## Roadmap

- Web interface with drag-and-drop upload
- Real-time conversion preview
- API wrapper for programmatic access
- Enhanced Markdown formatting options

## Known limitations

- Tested with standard Keep exports only
- Requires manual path configuration (temporary)
- Does not deduplicate attachment files
- Image paths assume original folder structure

## Contributing

Issues and PRs welcome. Focus areas: error handling improvements, export edge cases, and Markdown output refinement.

## License

MIT
