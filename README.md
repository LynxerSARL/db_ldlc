# db_ldlc

This repository demonstrates a small Python GUI and a web-based alternative.
Running `main.py` opens a mid-sized window that fades in to reveal a dark theme login form.
The title **Hackboot** slides down before the username and password fields appear.
`webview_main.py` instead displays the **Hackboot** login page using a WebView.

## Requirements

- Python 3
- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) for a modern look
- [pywebview](https://github.com/r0x0r/pywebview) to display the web interface

## Usage

Install the dependencies and run either example:

```bash
pip install ttkbootstrap pywebview
# Traditional Tk GUI
python main.py

# WebView version
python webview_main.py
```

Entering your credentials and pressing **Login** will display them in a simple dialog box.
