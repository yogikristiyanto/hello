def word_frequency(sentence):
 words = sentence.split()
 frequency = {}
 for word in words:
  if word in frequency:
   frequency[word] += 1
  else:
   frequency[word] = 1
 return frequency
sentence = "Python is great and Python is fun"
print("Frekuensi kata:", word_frequency(sentence))
