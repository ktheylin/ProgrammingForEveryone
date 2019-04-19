text = "X-DSPAM-Confidence:    0.8475";
s_pos = text.find(':')
num_text = text[s_pos+1:]
num = float(num_text)
print num