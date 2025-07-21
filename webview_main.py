import os
import webview


def main():
    html_path = os.path.join(os.path.dirname(__file__), 'web', 'login.html')
    webview.create_window('Hackboot Login', html_path, width=600, height=500, resizable=False)
    webview.start()


if __name__ == '__main__':
    main()
