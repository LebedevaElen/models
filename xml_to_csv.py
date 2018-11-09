import os
import glob
import sys
import pandas as pd
import xml.etree.ElementTree as ET

path = sys.argv[1]
os.chdir(path)
for set_type in ['train', 'eval']:
    xml_list = []
    with open(f'{set_type}.txt') as f:
        for xml_file in f:
            tree = ET.parse(f'xmls/{xml_file}.xml')
            root = tree.getroot()
            for member in root.findall('object'):
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    xml_df.to_csv(f'{set_type}_labels.csv', index=None)
    print('Successfully converted xml to csv.')
