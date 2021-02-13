from math import ceil

class Popluation:

  def __init__(self, size, prevalance, accuracy):
    self.size = size
    self.prevalance = prevalance
    self.accuracy = accuracy
    self.diseased = size * self.prevalance

  def return_positives(self):
    positives = self.diseased * (self.accuracy)
    self.positives = positives
    return positives

  def reutrn_falsepositives(self):
    remaining = self.size - (self.diseased*self.accuracy)
    falsepositives = remaining - round(remaining * self.accuracy)
    self.falsepositives = falsepositives
    return ceil(falsepositives)

  def calculate_probability_of_disease(self):
    return self.prevalance
  
  def calculate_accuracy_of_test(self):
    return f'{self.accuracy*100}%'

  def calculate_likelihood_of_disease_presence(self):
    likelihood = f'{self.diseased} out of every {ceil(self.positives+self.falsepositives)}.'
    return likelihood


pop = Popluation(100, 1/100, 90/100)
print(pop.diseased, 'are infected')
print(pop.return_positives(), 'are correctly identified')
print(pop.reutrn_falsepositives(), 'are falsely identified')
print(pop.calculate_likelihood_of_disease_presence())
