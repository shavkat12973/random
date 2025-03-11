# Python bazaviy imidjini ishlatamiz
FROM python:3.10

# Ishchi katalogni yaratamiz va unga o'tamiz
WORKDIR /app

# Kerakli fayllarni konteynerga nusxalash
COPY requirements.txt .
COPY game.py .

# Kutubxonalarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# Botni ishga tushiramiz
CMD ["python", "game.py"]
