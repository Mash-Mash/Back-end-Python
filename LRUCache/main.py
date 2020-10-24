from LRUCache import LRUCache

if __name__ == '__main__':
    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    cache.get('Jesse')  # вернёт 'James'
    cache.delete('Walter')
    cache.get('Walter')  # вернёт ''