from collections import deque
class Antrian Bank:
    def__init__(self):
        self.antrian = deque ()
    
    def masuk (self, peanggan)
        if self._size == len (elf._deque):
            self._resize (2*len(self._data))
        avail = (self._from + self._size) % len (self.data)
        self._data [avail] = pelanggan 
         self._size + = 1
        
    def keluar (self)
       if self. is_empty ('queue is empty')
    answer = self._data[self._front]
    self._data [self._front] = None
    self._front = (self._front + 1) % len(self._data)
    self._size == 1
    return answer