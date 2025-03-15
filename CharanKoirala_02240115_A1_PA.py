import math

def primenumber(n) :
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
def primesum (start, end):
     return sum(n for n in range (start, end + 1 ) if primenumber(n))

def convertlength(value, unit):
     if unit.upper() == 'M':
          return round(value * 3.280, 2)
     elif unit.upper() == 'F':
          return round(value / 3.280, 2)
     else :
          return 'Invalid unit'
     
def consonantcounter(string):
     consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' 
     return number(1 for char in text if char in consonants)

def minmax():
     try:
          number = int(input('type the amount of numbers you want to list:'))
          number1 = [float(input(f'Enter number {i+1}:'))for i in range(number)]
          return f'Minimum:{min(number1)}, Maximum:{max(number1)}'
     except ValueError:
          return 'Incorrect input, please enter numbers carefully!'
     
def palindrome(string):
     text = ''.join(text.lower().split())
     return text == text[::-1]

def wc(n):
    wtc = ['the''was''and']
    try :
          with open(n, 'r') as file:
               text = file.read().lower()
          return {word: text.split().count(word) for word in wtc}
    except FileNotFoundError:
        return 'file not found'

def main():
     while True:
          print ('Select a function:')
          print ('1. calculate sum of prime numbers within a range of two numbers')
          print ('2.length unit converter')
          print ('3.count number of consonants in a text')
          print ('4.find minimun and maximum numbers')
          print ('5.palindrome checker')
          print ('6.word counter')
          print ('7.Exit program')

          choice = input('Enter the number against the list of operations accordingly:')
        
          if choice == '1':
                start = int(input('start of range:'))
                end = int(input('End of range:'))
                print(f'Sum of primes: {primesum(start, end)}')

            
          elif choice == '2':
                value = float(input('Enter length: '))
                unit = input('Type m for metres to feet or f for feet to metres: ')
                print (f'converted length: {convertlength(value, unit)}')

          elif choice == '3':
                x = input('Enter text: ')
                print (f'Number of consonants in the text: {consonantcounter(t)}')

          elif choice == '4':
                print(minmax())
          elif choice == '5':
                x = input('Enter text: ')
                print (f'palindrome:{palindrome(x)}')

          elif choice == '6':
                x = input('Enter: ')
                print (wc(x))

          elif choice == '7':
                print ('Exiting...')
                break

          else :
                print('Please select the required numbers for each operation')

if __name__ == "__main__":
           main()



            
     

    



    


    


