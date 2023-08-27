#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
      self._value = ''
      self.value = value
      
  @property
  def value(self):
      return self._value

  @value.setter
  def value(self, value):
      if isinstance(value, str):
          self._value = value
      else:
          print("The value must be a string.")
    
  def is_sentence(self):
    return self.value.endswith('.')
  
  def is_question(self):
    return self.value.endswith('?')

  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    # Replace all sentence-ending punctuation with periods
    temp = self.value.replace('!', '.').replace('?', '.')
    # Split the string into sentence and count them
    return len([sentence for sentence in temp.split('.') if sentence.strip() != ''])
pass
