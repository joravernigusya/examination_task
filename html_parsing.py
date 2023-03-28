import os
from bs4 import BeautifulSoup

project_folder = "C:/Users/Yan/Desktop/PythonAutomation/examination_task/" \
                 "test-i18n"
tags_to_check = ["p", "button", "h2", "h"]

for root, dirs, files in os.walk(project_folder):
    for file_name in files:
        if file_name.endswith(".html"):
            with open(os.path.join(root, file_name), "r",
                      encoding="utf-8") as f:
                content = f.read()
                soup = BeautifulSoup(content, "html.parser")
                for tag in tags_to_check:
                    for el in soup.find_all(tag):
                        if not el.has_attr("i18n"):
                            print(
                                f"{os.path.join(root, file_name)}, "
                                f"line {el.sourceline}: {el}"
                            )