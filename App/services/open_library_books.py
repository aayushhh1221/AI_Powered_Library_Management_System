import requests
from sqlalchemy.orm import Session

from App.models import Book


def import_books(q: str, db: Session):

    url = f"https://openlibrary.org/search.json?q={q}&limit=20"

    response = requests.get(url)

    if response.status_code != 200:
        return {
            "message": "Failed to fetch books"
        }

    data = response.json()

    imported = 0

    for item in data.get("docs", []):

        title = item.get("title", "Unknown")

        authors = ", ".join(
            item.get("author_name", ["Unknown"])
        )

        categories = ", ".join(
            item.get("subject", ["General"])[:3]
        )

        existing = (
            db.query(Book)
            .filter(Book.title == title)
            .first()
        )

        if existing:
            continue

        book = Book(
            title=title,
            author=authors,
            category=categories,
            quantity=5
        )

        db.add(book)

        imported += 1

    db.commit()

    return {
        "message": f"{imported} books imported successfully"
    }