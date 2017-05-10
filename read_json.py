from json_loader import SearchItemLoader
from py2neo import Graph, Node, Relationship

graph = Graph('http://localhost:7474/db/data', user='neo4j', password='gbpltwdctve')

def main():
    search_items = [
        ('data/product/cases_pc.json'),
        ('data/product/cpu.json'),
        ('data/product/drive_pc.json'),
        ('data/product/hdd.json'),
        ('data/product/memory_for_pc.json'),
        ('data/product/motherboards.json'),
        ('data/product/power_supply.json'),
        ('data/product/videocards.json'),
    ]

    for (search_path) in search_items:
        print("load items: %s" % search_path)
        items = SearchItemLoader.load(search_path)

        if search_path == 'data/product/cpu.json':
            for item in items:
                try:
                    cpu = Node("CPU", id = item.id, name=item.name, type = item.type, model = item.model, rating = item.rating, socket = item.characteristics['socket'], technology_process = item.characteristics['technology_process'],
                        core_num = item.characteristics['core_number'], cpu_frequency = item.characteristics['cpu_frequency'])
                    graph.create(cpu)
                except:
                    next
        elif search_path == 'data/product/cases_pc.json':
            for item in items:
                try:
                    cases = Node("Cases_pc", id = item.id, name=item.name, type = item.type, model = item.model, rating = item.rating, format = item.characteristics['format'], type_mather = item.characteristics['type_mather'],
                            power_supply = item.characteristics['power_supply'])
                    graph.create(cases)
                except:
                    next
        elif search_path == 'data/product/drive_pc.json':
            for item in items:
                try:
                    drive = Node("Drive_pc", id = item.id, name=item.name, type = item.type, model = item.model, rating = item.rating,  delivery_type = item.characteristics['delivery_type'], type_hdd = item.characteristics['type_hdd'])
                    graph.create(drive)
                except:
                    next
        elif search_path == 'data/product/hdd.json':
            for item in items:
                try:
                    hdd = Node("HDD", id = item.id, name=item.name, type = item.type, model = item.model, rating = item.rating, form_factor = item.characteristics['form_factor'], volume_hdd = item.characteristics['volume_hdd'], type_hdd = item.characteristics['type_hdd'])
                    graph.create(hdd)
                except:
                    next
        elif search_path == 'data/product/memory_for_pc.json':
            for item in items:
                try:
                    memory = Node("Memorys", id = item.id, name=item.name, type = item.type, model = item.model, rating = item.rating, type_ram = item.characteristics['type_ram'], volume = item.characteristics['volume'], capacity = item.characteristics['capacity'])
                    graph.create(memory)
                except:
                    next
        elif search_path == 'data/product/motherboards.json':
            for item in items:
                try:
                    mather = Node("Motherboards", id = item.id, name=item.name, type = item.type, model = item.model, rating = item.rating, io = item.characteristics['io'], chipset = item.characteristics['chipset'], socket = item.characteristics['socket'], ram = item.characteristics['ram'], form_factor = item.characteristics['form_factor'],
                                  manufacturer = item.characteristics["manufacturer"])
                    graph.create(mather)
                except:
                    next
        elif search_path == 'data/product/power_supply.json':
            for item in items:
                try:
                    power = Node("PS", id = item.id, name=item.name, type = item.type, model = item.model, rating = item.rating, standart = item.characteristics['standart'], col_power = item.characteristics['col_power'])
                    graph.create(power)
                except:
                    next
        elif search_path == 'data/product/videocards.json':
            for item in items:
               try:
                    video = Node("VideoCards", id = item.id, name=item.name, type = item.type, rating = item.rating, interface = item.characteristics['interface'], shina = item.characteristics['shina'], technology_process = item.characteristics['technology_process'], capacity_ram = item.characteristics['capacity_ram'],
                             type_video = item.characteristics['type_video'], volume = item.characteristics['volume'], chipset = item.characteristics['chipset'])
                    graph.create(video)
               except:
                   next
        else:
            print('Error: not data json')

if __name__ == '__main__':
    print("Start save to NoSQL products...")
    main()
