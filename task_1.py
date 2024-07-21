class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True
    
    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i in range(0, len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    self.table[key_hash].pop(i)
                    return True
        return False
    

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))   # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30

# Додаємо тести для видалення:
print(H.delete("apple"))   # Виведе: True
print(H.get("apple"))      # Виведе: None, бо "apple" було видалено
print(H.delete("orange"))  # Виведе: True
print(H.get("orange"))     # Виведе: None, бо "orange" було видалено
print(H.delete("banana"))  # Виведе: True
print(H.get("banana"))     # Виведе: None, бо "banana" було видалено

# Спробуємо видалити ключ, якого немає в таблиці
print(H.delete("grape"))   # Виведе: False, бо "grape" немає в таблиці