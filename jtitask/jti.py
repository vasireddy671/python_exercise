infile = r"C:\Users\syste\Downloads\Compressed\Python_exercises_QA_Engr (5)_2\Updated_Python_exercises_QA_Engr\Jmeter_log1.jtl"
important = []
keep_phrases = ['504']
with open(infile) as f:
    f = f.readlines()
for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            important.append(line)
            break
print(important)