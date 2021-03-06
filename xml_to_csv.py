import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(member.find('bndbox')[0].text),
                     int(member.find('bndbox')[1].text),
                     int(member.find('bndbox')[2].text),
                     int(member.find('bndbox')[3].text),

                     )
            xml_list.append(value)
    column_name = ['filename','startX','startY','endX','endY']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for directory in ['train']:
        image_path = os.path.join(os.getcwd(), 'images')
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('data/car_plate_annotation.csv', index=None)
        print('Successfully converted xml to csv.')






main()
