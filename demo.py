txt = open("/Users/bhuvaneshd/Desktop/Task/text_extractor/input/Employee_Roadmap_Only_unpacked/xl/worksheets/sheet1.xml" , "r")
data = txt.read()

start = data.find("<x:v>")
end = data.find("</x:v>", start)
value = data[start +5 : end]
print(value)

end_1 = data.find("<x:v>",end)
start_2 = data.find("</x:v>", end_1)
value_1 = data[end_1 +5 : start_2]
print(value_1)

end_2 = data.find("<x:v>",start_2)
startr_3 = data.find("</x:v>", end_2)
value_2 = data[end_2 +5 : startr_3]
print(value_2)


end_3 = data.find("<x:v>",startr_3)
start_4= data.find("</x:v>", end_3)
value_3 = data[end_3 +5 : start_4]
print(value_3)

end_4 = data.find("<x:v>",start_4)
start_5 = data.find("</x:v>", end_4)
value_4 = data[end_4 +5 : start_5]
print(value_4)

end_5 = data.find("<x:v>",start_5)
start_6 = data.find("</x:v>", end_5)
value_5 = data[end_5 +5 : start_6]
print(value_5)

end_6 = data.find("<x:v>" , start_6)
start_7 = data.find("</x:v>", end_6)
value_6 = data[end_6 +5 : start_7]
print(value_6)