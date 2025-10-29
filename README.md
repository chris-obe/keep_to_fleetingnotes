# Keep to Markdown (because apparently I enjoy rewriting wheels)

> A humble Python script that scrapes your exported Google Keep HTML files and turns them into Markdown notes—because I wanted automation, but evidently not enough to build a proper UI. Yet.
> Bonus: the output plays nicely with Obsidian, Fleeting Notes, and whatever other Markdown playground you prefer.

## What is this?

This project is a glorified batch converter. Point it at the folder where Google Keep dumps its painfully verbose HTML files, and it spits out Markdown notes that are actually pleasant to read. Titles, timestamps, tags, content, attachments—the script does its best to wrangle everything into shape while I pretend this is a long-term maintainable solution.

Spoiler: I fully intend to terraform this into a web-hosted app with an actual front end once I stop high-fiving myself for getting the command-line version to work.

## Features (if we squint)

- Converts Google Keep HTML exports into Markdown with sensible file names.
- Preserves creation dates, tags, and even those awkward inline images.
- Gives you control over how many files to process via a command-line argument.
- Works without any external service because apparently I enjoy subjecting myself to local tooling.

## Requirements

- Python 3.9+
- `beautifulsoup4`
- `html2text`
- `python-dateutil`

Install dependencies the low-tech way:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt  # or install the packages individually
```

## Setup

1. Clone this repository (or copy the script—you do you).
2. Export your Google Keep notes from [takeout.google.com](https://takeout.google.com/).
3. Extract the archive and find the folder containing all the `.html` files.
4. Open `convert_keep_to_md.py` and replace the empty `input_dir` and `output_dir` strings with your actual paths.

```python
input_dir = ""   # e.g., "/path/to/Takeout/Keep"
output_dir = ""  # e.g., "/path/to/MarkdownNotes"
```

Yes, you have to edit the script. No, the irony is not lost on me.

## Usage

Run the script from your terminal once the paths are in place:

```bash
python convert_keep_to_md.py [optional_number_of_files]
```

- Omit the argument to convert everything.
- Supply an integer (e.g., `25`) to process only the first N HTML files, in case you enjoy incremental progress.

Converted notes land in the output directory with filenames like `2024-05-01 - Grocery List.md`. Images are referenced relative to their original paths, so keep your attachments folder nearby unless you like broken links.

## Roadmap (a.k.a. future ambition)

- [ ] Build a web front end so normal humans can use this tool.
- [ ] Add drag-and-drop uploads and real-time previews.
- [ ] Maybe wrap it in a tiny API instead of playing folder roulette.
- [ ] Polish the Markdown output until it looks like I knew what I was doing all along.

If you wait long enough, there will be a browser-based version you can share with friends without apologizing first.

## Limitations

- Only tested with standard Google Keep exports—your mileage may vary if you do something clever.
- Requires manual path configuration (see: “front end coming soon-ish”).
- Doesn’t deduplicate attachments, read your mind, or fix your note organization habits.

## Contributing

Issues and pull requests are welcome, especially if they remove technical debt I proudly introduced. If you're here for the upcoming front end, feel free to remind me that I promised one.

## License

MIT. Mostly because copying and pasting this section is easier than thinking about it.
