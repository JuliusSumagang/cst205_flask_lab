from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

STUDENT_FIRST_NAME = "Julius"
FAVORITE_ACRONYM = "TTYL (Talk To You Later)"

CLASSMATES = [
    {"name": "Pedro", "acronym": "AFAIK (As Far As I Know)"},
    {"name": "Ethan", "acronym": "ICYMI (In Case You Missed It)"},
    {"name": "Samantha", "acronym": "IMO (In My Opinion)"},
]

IMAGE_URL = "https://picsum.photos/id/237/600/400"
IMAGE_ALT = "A dog"


@app.get("/")
def classmates():
    """Task 2: build the HTML directly, without a template."""
    paragraphs = "\n".join(
        f"<p>{person['name']}: {person['acronym']}</p>" for person in CLASSMATES
    )
    return f"<!doctype html><html><head><title>Classmate Acronyms</title></head>" \
        f"<body><h1>Classmate Acronyms</h1>{paragraphs}</body></html>"


@app.get(f"/{STUDENT_FIRST_NAME.lower()}")
def favorite_acronym():
    """Task 3: pass the favorite acronym into a Jinja template."""
    return render_template(
        "template.html",
        student_name=STUDENT_FIRST_NAME.title(),
        acronym=FAVORITE_ACRONYM,
        show_image=False,
        use_bootstrap=False,
    )


@app.get(f"/{STUDENT_FIRST_NAME.lower()}/bootstrap")
def bootstrap_page():
    """Task 4: show a remote Lorem Picsum image with Bootstrap classes."""
    return render_template(
        "template.html",
        student_name=STUDENT_FIRST_NAME.title(),
        acronym=FAVORITE_ACRONYM,
        show_image=True,
        use_bootstrap=True,
        image_url=IMAGE_URL,
        image_alt=IMAGE_ALT,
    )


if __name__ == "__main__":
    app.run(debug=True)
