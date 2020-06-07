''' Type your code here. '''
import math

class Piano:
    def __init__(self, frequency, key_frequencies = 0, frequency1 = 0, frequency2 = 0, frequency3 = 0, frequency4 = 0, frequency5 = 0):
        self.frequency = frequency
        self.frequency1 = frequency1
        self.frequency2 = frequency2
        self.frequency3 = frequency3
        self.frequency4 = frequency4
        self.frequency5 = frequency5
        self.key_frequencies = 2 # r value r = 2^(1/12)
        
    def process_information(self):
        self.frequency1 = float(self.frequency) * math.pow(self.key_frequencies, 1.0 / 12.0)
        self.frequency2 = float(self.frequency) * math.pow(self.key_frequencies, 2.0 / 12.0)
        self.frequency3 = float(self.frequency) * math.pow(self.key_frequencies, 3.0 / 12.0)
        self.frequency4 = float(self.frequency) * math.pow(self.key_frequencies, 4.0 / 12.0)
        self.frequency5 = float(self.frequency) * math.pow(self.key_frequencies, 5.0 / 12.0)
        self.frequency = float(self.frequency)
    
    def output_information(self):
        return '%0.2f %0.2f %0.2f %0.2f %0.2f' % (self.frequency, self.frequency1, self.frequency2, self.frequency3, self.frequency4)

musician = Piano(frequency = input())
musician.process_information()
print(musician.output_information())
