import pandas as pd
import random
from datetime import datetime, timedelta

NUM_BOOKS = 300
NUM_BORROWERS = 8000
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# kategori buku
categories = {
   "Fiksi": ["Novel", "Cerita Pendek", "Drama", "Puisi"],
   "Historis": ["Biografi", "Sejarah Dunia", "Sejarah Lokal"],
   "Teknologi": ["Pemrograman", "Jaringan", "Keamanan Siber", "AI"],
   "Sains": ["Fisika", "Kimia", "Biologi", "Matematika"],
   "Seni": ["Seni Rupa", "Musik", "Teater", "Fotografi"],
}

titles_templates = [
    "The {adjective} {noun}", "A Journey through {place}", "Understanding {concept}", "The Art of {skill}",
    "Exploring {topic}", "The History of {event}", "Mastering {subject}", "The Science of {phenomenon}",
    "The World of {field}", "The Future of {technology}"
]

first_names = ["Agus", "Budi", "Citra", "Dewi", "Eka", "Fajar", "Gita", "Hadi", "Indah", "Joko", 
               "Kiki", "Lina", "Maya", "Nina", "Oka", "Putri", "Rina", "Sari", "Tina", "Umar"]

lasts_names = ["Santoso", "Wijaya", "Pratama", "Setiawan", "Kusuma", "Lestari", "Sari", "Hidayat",
               "Nugroho", "Wibowo", "Saputra", "Yulianto", "Ramadhan", "Putra", "Sukma", "Halim", 
               "Fauzi", "Kurniawan", "Prasetyo", "Gunawan"]

# generate book data
books = []
book_id_counter = 1000
for _ in range(NUM_BOOKS):
    category = random.choice(list(categories.keys()))
    subcategory = random.choice(categories[category])
    title_template = random.choice(titles_templates)
    title = title_template.format(
        adjective=random.choice(["Great", "Mysterious", "Ancient", "Modern", "Innovative"]),
        noun=random.choice(["Adventure", "Mystery", "Science", "Art", "History"]),
        place=random.choice(["the World", "the Universe", "the City", "the Jungle"]),
        concept=random.choice(["Love", "Courage", "Wisdom", "Power"]),
        skill=random.choice(["Painting", "Writing", "Programming", "Cooking"]),
        topic=random.choice(["Technology", "Nature", "Culture", "Society"]),
        event=random.choice(["War", "Revolution", "Discovery", "Invention"]),
        subject=random.choice(["Mathematics", "Physics", "Biology", "Chemistry"]),
        phenomenon=random.choice(["Gravity", "Evolution", "Relativity", "Quantum Mechanics"]),
        field=random.choice(["Medicine", "Engineering", "Astronomy", "Ecology"]),
        technology=random.choice(["AI", "Blockchain", "VR", "IoT"])
    )
    author = f"{random.choice(first_names)} {random.choice(lasts_names)}"
    publication_year = random.randint(1990, 2023)
    books.append({
        'book_id': book_id_counter,
        'title': title,
        'author': author,
        'category': category,
        'subcategory': subcategory,
        'publication_year': publication_year
    })
    book_id_counter += 1

# generate borrower data
start_date = datetime.now().date() - timedelta(days=365*2)
user_depts = ["HR", "Finance", "IT", "Marketing", "Sales", "Operations", "R&D", "Customer Service"]
combined_data = []

for i in range(NUM_BORROWERS):
    borrower_id = 5000 + i
    borrower_name = f"{random.choice(first_names)} {random.choice(lasts_names)}"
    dept = random.choice(user_depts)
    num_borrows = random.randint(1, 5)
    borrowed_books = random.sample(books, num_borrows)
    
    for book in borrowed_books:
        borrow_date = start_date + timedelta(days=random.randint(0, 365*2))
        return_date = borrow_date + timedelta(days=random.randint(7, 30))
        combined_data.append({
            'borrower_id': borrower_id,
            'borrower_name': borrower_name,
            'department': dept,
            'book_id': book['book_id'],
            'title': book['title'],
            'author': book['author'],
            'category': book['category'],
            'subcategory': book['subcategory'],
            'publication_year': book['publication_year'],
            'borrow_date': borrow_date,
            'return_date': return_date
        })

# create DataFrame and save to CSV
df = pd.DataFrame(combined_data)
df.to_csv('library_borrowing_book_data.csv', index=False)

print("Data berhasil disimpan ke library_borrowing_book_data.csv")
print(df.head())

# generate data holidays dan libur ujian
holiday_events = {
    "holiday": ["New Year's Day", "Independence Day", "Christmas", "Eid al-Fitr", "Eid al-Adha",
                "Labor Day", "Thanksgiving", "Halloween", "Valentine's Day", "National Heroes Day"],
    "exam_break": ["Midterm Exams", "Final Exams", "Semester Break", "Winter Break", "Summer Break"]
}

holiday_data = []
for year in range(2022, 2025):
    for month in range(1, 13):
        if random.random() < 0.3:  
            day = random.randint(1, 28)  
            event_type = random.choice(list(holiday_events.keys()))
            event_name = random.choice(holiday_events[event_type])
            holiday_data.append({
                'date': datetime(year, month, day).date(),
                'event': event_name,
                'type': event_type
            })

holiday_df = pd.DataFrame(holiday_data)
holiday_df.to_csv('library_holidays_exams.csv', index=False)
print("Data libur dan ujian berhasil disimpan ke library_holidays_exams.csv")