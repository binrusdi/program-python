# Untuk menggunakan regex, Anda perlu mengimpor modul re terlebih dahulu.
import re

# Anda dapat menggunakan re.search() untuk mencocokkan pola dalam teks.

text = "Ini adalah contoh teks yang berisi angka 12345."
pattern = r'\d+'  # Ini adalah pola regex untuk mencocokkan angka-angka.
result = re.search(pattern, text)
if result:
    print("Pola ditemukan:", result.group())

# Anda dapat menggunakan re.sub() untuk mengganti teks berdasarkan pola.

text = "Hello, namaku jhon. Apakabarmu?"
pattern = r'jhon'
new_text = re.sub(pattern, 'Alice', text)
print(new_text)
