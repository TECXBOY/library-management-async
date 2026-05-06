import asyncio
from typing import List, Dict

# DATA
books: List[Dict] = [
    {"id": 1, "title": "Python Basics", "available": True},
    {"id": 2, "title": "Async Programming", "available": True},
    {"id": 3, "title": "Async Programming", "available": True},
    {"id": 4, "title": "introduction to programming", "available": True}

]

# BORROW FUNCTION
async def borrow_book(user_id: int, book_id: int) -> str:
    await asyncio.sleep(1)  # simulate delay

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return f"User {user_id} borrowed {book['title']}"
            else:
                return f"User {user_id}: Book not available"

    return f"User {user_id}: Book not found"


# RETURN FUNCTION
async def return_book(user_id: int, book_id: int) -> str:
    await asyncio.sleep(1)

    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            return f"User {user_id} returned {book['title']}"

    return f"User {user_id}: Book not found"


# MULTIPLE USERS SIMULATION

async def simulate_users():
    tasks = [
        borrow_book(1, 1),
        borrow_book(2, 1),
        return_book(1, 1),
        borrow_book(3, 1)
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

# RUN PROGRAM
if __name__ == "__main__":
    asyncio.run(simulate_users())
