try:
    with open("/Users/bhuvaneshd/Desktop/Task/text_extractor/input/tmt_large_sample.txt", "r") as text:
        text_extract_data = text.read()

except FileNotFoundError:
    print ("File Not Found")
    
cleaned_data = []
for data in text_extract_data.splitlines():
    clean_data = data.strip()
    if clean_data:
        cleaned_data.append(clean_data)

with open("/Users/bhuvaneshd/Desktop/Task/text_extractor/output/output.txt", "w") as output_data:
    for line in cleaned_data:
        output_data.write(line + "\n")


