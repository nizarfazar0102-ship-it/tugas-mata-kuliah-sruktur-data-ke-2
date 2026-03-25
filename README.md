1. Node
Node adalah elemen penyusun Linked List.
Setiap node punya:
•	data → nilai 
•	next → pointer menuju node berikutnya 
Ibarat gerbong kereta, setiap gerbong punya:
•	penumpang → data 
•	sambungan ke gerbong berikutnya → pointer next 
________________________________________
2. LinkedList (penyimpanan data)
Linked List menyimpan alamat node pertama (head).
Kalau head = None, artinya list kosong.
________________________________________
🔧 Operasi Linked List
A. Insert di Depan (insert_front)
new_node.next → head lama  
head → new_node
Seperti menambah mobil baru di paling depan antrian.
B. Insert di Belakang (insert_back)
Cari node terakhir, lalu sambungkan node baru ke belakang.
Seperti menambah mobil di belakang antrian.
________________________________________
C. Delete
Langkah:
1.	Jika node pertama yang akan dihapus → pindahkan head. 
2.	Jika di tengah → putuskan sambungan dari node sebelumnya. 
3.	Jika tidak ditemukan → return False. 
Analogi:
Mengeluarkan satu mobil dari barisan parkir dengan “menggeser sambungan”.
________________________________________
D. Search
Menelusuri satu per satu node hingga menemukan data.
________________________________________
E. Display
Mencetak isi list dalam bentuk:
20 -> 30 -> 40 -> None

# tugas-mata-kuliah-sruktur-data-ke-2
