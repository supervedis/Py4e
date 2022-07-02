text = "X-DSPAM-Confidence:    0.8475"
t_index = text.find(" ")
print(float(text[t_index:]))