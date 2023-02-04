def number_cardinality(samples):
    samp_vals = {"0":"zero", "1":"one","2": "two","3": "three","4" :"four", "5":"five", "6":"six","7": "seven"}
    for samp in samples :
        last_numb = str(samp) [-1]
        print(f"Last number for {samp} is {samp_vals [last_numb]}")
samples =("22", "35", "10", "41", "77", "56")
number_cardinality(samples)
