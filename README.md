# CST 205 Flask Lab, Part 1

## Run locally

From this folder, create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\\Scripts\\activate      # Windows PowerShell
pip install -r requirements.txt
flask --app app --debug run
```

Open the routes below in your browser while the server is running:

- `http://127.0.0.1:5000/` — Task 2, classmates' acronyms generated directly in the view function.
- `http://127.0.0.1:5000/julius` — Task 3, Jinja template.
- `http://127.0.0.1:5000/julius/bootstrap` — Task 4, template plus remote image and Bootstrap styling.
