import re
some_list = []
count_of_barcodes = int(input())
for i in range(count_of_barcodes):
    text = input()
    pattern = r"((@#+)([A-Z][A-Za-z0-9]{4,})([A-Z])(@#+))"
    matched = re.findall(pattern, text)
    if not matched:
        print("Invalid barcode")
    else:
        for i in matched:
            pattern = r'(\d)'
            matched = re.findall(pattern, i[0])
            if matched:
                result = ''.join(matched)
                print(f'Product group: {result}')
            else:
                print('Product group: 00')









