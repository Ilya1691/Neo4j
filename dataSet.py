from py2neo import Relationship, Node, Graph
import re
import csv

graph = Graph('http://localhost:7474/db/data', user='neo4j', password='gbpltwdctve')

datasPC_AMD = graph.data('MATCH (r:Memorys)-[:RAM]->(m:Motherboards{manufacturer:"AMD"})<-[:CPU]-(c:CPU) return r.name as Memory, '
                     'r.type_ram as Type_RAM, r.volume as Volume_Gb, m.name as Motherboards, m.socket as Socket, m.manufacturer as manufacturer, '
                     'c.name as CPU, c.core_num as Core_Number, c.cpu_frequency as Frequency LIMIT 10')
datasPC_Intel = graph.data('MATCH (r:Memorys)-[:RAM]->(m:Motherboards{manufacturer:"Intel"})<-[:CPU]-(c:CPU) return r.name as Memory, '
                     'r.type_ram as Type_RAM, r.volume as Volume_Gb, m.name as Motherboards, m.socket as Socket, m.manufacturer as manufacturer, '
                     'c.name as CPU, c.core_num as Core_Number, c.cpu_frequency as Frequency LIMIT 10')
datasVideo = graph.data('MATCH (n:VideoCards) RETURN n.volume as volume_video, n.shina as Shina LIMIT 25')
datasHDD = graph.data('MATCH (n:HDD{type_hdd:"Твердотельный накопитель"}) RETURN n.volume_hdd as volume_hdd LIMIT 25')

def write_cvs(datas):
    with open('data/System_unit.cvs', 'a') as f:
        for data in datas:
            writer = csv.writer(f)
            writer.writerow((data['value'],
                             data['core_number'],
                             data['frequency'],
                             data['value_video'],
                             data['shina'],
                             data['volume_hdd'],
                             data['manufacturer']))

datas = []

for dataPC in datasPC_AMD:
    for dataVideo in datasVideo:
        for dataHDD in datasHDD:
            value = re.findall(r'\d+',dataPC["Volume_Gb"])
            value = value[0]
            value_video = re.findall(r'\d+',dataVideo["volume_video"])
            value_video = value_video[0]
            if value_video == "512":
                value_video = 512 / 1024
            #print(value,"|", dataPC["Core_Number"],"|", dataPC["Frequency"],"|", value_video,"|", dataVideo["Shina"],"|", dataHDD["volume_hdd"])
            #datas = value,"|", dataPC["Core_Number"],"|", dataPC["Frequency"],"|", value_video,"|", dataVideo["Shina"],"|", dataHDD["volume_hdd"]
            data = {
                'value': value,
                'core_number': dataPC["Core_Number"],
                'frequency': dataPC["Frequency"],
                'value_video': value_video,
                'shina': dataVideo["Shina"],
                'volume_hdd': dataHDD["volume_hdd"],
                'manufacturer': dataPC['manufacturer']
            }
            datas.append(data)
            print("count: %s" % len(datas))
for dataPC in datasPC_Intel:
    for dataVideo in datasVideo:
        for dataHDD in datasHDD:
            value = re.findall(r'\d+',dataPC["Volume_Gb"])
            value = value[0]
            value_video = re.findall(r'\d+',dataVideo["volume_video"])
            value_video = value_video[0]
            if value_video == "512":
                value_video = 512 / 1024
            data = {
                'value': value,
                'core_number': dataPC["Core_Number"],
                'frequency': dataPC["Frequency"],
                'value_video': value_video,
                'shina': dataVideo["Shina"],
                'volume_hdd': dataHDD["volume_hdd"],
                'manufacturer': dataPC['manufacturer']
            }
            datas.append(data)
            print("count: %s" % len(datas))
write_cvs(datas)