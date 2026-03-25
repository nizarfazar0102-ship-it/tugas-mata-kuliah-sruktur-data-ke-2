# Node merepresentasikan 1 elemen pada linked list
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai
        self.next = None      # pointer ke node berikutnya

# Singly Linked List
class LinkedList:
    def __init__(self):
        self.head = None      # awal list

    # 1. Insert di depan (push front)
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head   # node baru menunjuk head lama
        self.head = new_node        # head pindah ke node baru

    # 2. Insert di belakang (push back)
    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:       # kalau list kosong
            self.head = new_node
            return
        temp = self.head
        while temp.next:            # cari node terakhir
            temp = temp.next
        temp.next = new_node        # sambungkan node baru di akhir

    # 3. Delete nilai tertentu
    def delete(self, key):
        temp = self.head

        # jika node pertama yang harus dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return True

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:            # tidak ditemukan
            return False

        prev.next = temp.next       # lewati node yang dihapus
        temp = None
        return True

    # 4. Search nilai
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # 5. Print list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# =========================
# Contoh Penggunaan
# =========================
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_front(30)
    ll.insert_front(20)
    ll.insert_back(40)
    ll.insert_back(50)

    ll.display()

    print("Cari 40:", ll.search(40))
    print("Hapus 20:", ll.delete(20))

    ll.display()
