# DIGITAL_FORENSIC_TOOLKIT

A Python-based digital forensics toolkit for collecting and analyzing Google Chrome browser artifacts. This project helps investigators and cybersecurity students examine browser history and extract useful forensic information from a local Chrome profile.

## Features

* Extract Chrome browsing history
* Read Chrome History SQLite database
* Display visited URLs
* Show page titles
* Display visit timestamps
* Parse URLs and query parameters
* Handle locked browser database by creating a temporary copy
* Simple command-line interface
* Beginner-friendly Python code

## Technologies Used

* Python 3
* SQLite3
* OS Module
* Shutil
* Datetime
* urllib.parse

## Project Structure

```
Browser-Forensics-Toolkit/
│
├── main.py
├── README.md
└── requirements.txt (optional)
```

## How It Works

1. Locates the Chrome History database.
2. Creates a temporary copy of the database (to avoid file lock issues).
3. Connects to the SQLite database.
4. Reads browsing history records.
5. Converts Chrome timestamps into readable date and time.
6. Displays forensic information in the terminal.

## Requirements

* Python 3.9 or newer
* Windows
* Google Chrome installed

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/browser-forensics-toolkit.git
```

Go to the project folder:

```bash
cd browser-forensics-toolkit
```

Run the program:

```bash
python main.py
```

## Example Output

```
Browser Forensics Toolkit

Title: OpenAI
URL: https://openai.com
Visited: 2026-07-27 18:45:12

Title: GitHub
URL: https://github.com
Visited: 2026-07-27 19:10:04
```

## Learning Objectives

This project was created to practice:

* Digital Forensics
* Browser Artifact Analysis
* SQLite Database Investigation
* Python File Handling
* Timestamp Conversion
* Cybersecurity Fundamentals

## Future Improvements

* Download history analysis
* Cookies extraction
* Saved passwords (authorized environments only)
* Autofill data analysis
* Bookmark extraction
* Multiple browser support (Edge, Firefox, Brave)
* Export results to CSV or PDF
* GUI version

## Disclaimer

This project is intended **only for educational purposes and authorized digital forensic investigations**. Use it only on systems and browser data that you own or have explicit permission to examine.

## Author

**Utsav Panchal**

B.Tech Student | Cybersecurity & Python Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub.
