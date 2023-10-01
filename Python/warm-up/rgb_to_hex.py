def rgb_to_hex(r, g, b):
    values = (r,g,b)
    hexa = ""
    for index in range(3):
        if values[index] > 255:
            values[index]=255
        elif values[index] < 0:
            values[index]=0
    for item in range(3):
        hexa += hex(values[item])
        hexa = hexa.replace('0x', '')
    if '0' in hexa:
            position = hexa.find('0')
            hexa = hexa[ : position]  + '0' + hexa[position : ]
    return hexa


result1 = rgb_to_hex(0,255,45)
print(result1)
result2 = rgb_to_hex(255,255,255)
print(result2)
