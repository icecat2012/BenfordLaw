# Benford's Law
If the distribution of the leading digits in data is much different from Benford's law, the data might be fake.

### When to use Benford's Law?
1. Numbers are not generated by artificial rules, such as phone numbers.
2. The span of the numbers is large
3. There are many numbers in the data

### How to use the code?
1. Create a txt file called 'text.txt'
2. Save all the words and numbers in the file
3. Run 'BenfordLaw.py'

An other method
```python
from BenfordLaw import BenfordLaw
Filename = 'FILENAME.txt'
ShowFigure = True
DigitCount, TotalNumbers = BenfordLaw(Filename, ShowFigure)
# DigitCount is a list from 1-9. TotalNumbers is a float number.
```

Example
The population of the countries in the world  

![image](https://github.com/icecat2012/BenfordLaw/blob/main/Population.PNG)
