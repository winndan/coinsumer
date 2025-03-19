import os
from fasthtml.common import *
from monsterui.all import *
from homepage.homepage import home

app, rt = fast_app(hdrs=Theme.neutral.headers(daisy=True), live=True)

# 🏠 Frontend Routes
@rt("/")
def landing_page():
    return home()


if __name__ == "__main__":
    serve()