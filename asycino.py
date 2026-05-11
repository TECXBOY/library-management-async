import asyncio
from typing import List, Dict

# DATA
books: List[Dict] = [
    {"id": 1, "title": "Python Basics", "available": True},
    {"id": 2, "title": "Async Programming", "available": True},
    {"id": 3, "title": "Async Programming", "available": True},
    {"id": 4, "title": "introduction to programming", "available": True}
]

book_locks: Dict[int, asyncio.Lock] = {}
borrowed_log: Dict[int, int] = {}  # book_id -> user_id

def get_lock(book_id: int) -> asyncio.Lock:
    if book_id not in book_locks:
        book_locks[book_id] = asyncio.Lock()
    return book_locks[book_id]

# LIST BOOKS FUNCTION
def list_books():
    print("\n--- Library Status ---")
    for book in books:
        status = f"Borrowed by User {borrowed_log[book['id']]}" if not book["available"] else "Available"
        print(f"[{book['id']}] {book['title']} — {status}")
    print("----------------------\n")

# BORROW FUNCTION
async def borrow_book(user_id: int, book_id: int) -> str:
    async with get_lock(book_id):
        await asyncio.sleep(1)  # simulate delay
        for book in books:
            if book["id"] == book_id:
                if book["available"]:
                    book["available"] = False
                    borrowed_log[book_id] = user_id  # track who borrowed it
                    return f"User {user_id} borrowed {book['title']}"
                else:
                    return f"User {user_id}: Book not available"
    return f"User {user_id}: Book not found"

# RETURN FUNCTION
async def return_book(user_id: int, book_id: int) -> str:
    async with get_lock(book_id):
        await asyncio.sleep(1)
        for book in books:
            if book["id"] == book_id:
                book["available"] = True
                borrowed_log.pop(book_id, None)  # remove from log
                return f"User {user_id} returned {book['title']}"
    return f"User {user_id}: Book not found"

# MULTIPLE USERS SIMULATION
async def simulate_users():
    list_books()  # before
    tasks = [
        borrow_book(1, 1),
        borrow_book(2, 1),
        return_book(1, 1),
        borrow_book(3, 1)
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
    list_books()  # after

# RUN PROGRAM
if __name__ == "__main__":
    asyncio.run(simulate_users())
