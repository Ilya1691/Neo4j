from py2neo import Relationship, Node, Graph

graph = Graph('http://localhost:7474/db/data', user='neo4j', password='gbpltwdctve')

datas_CPU = graph.data('MATCH (a:CPU) RETURN a.id, a.name, a.socket, a.technology_process LIMIT 100' )
datas_Mather = graph.data('MATCH (a:Motherboards) RETURN a.id, a.name, a.socket, a.ram, a.form_factor LIMIT 100')
data_Mems = graph.data('MATCH (a:Memorys) RETURN a.id, a.name, a.type_ram, a.volume LIMIT 100')
data_cases = graph.data('MATCH (a:Cases_pc) RETURN a.id, a.name, a.type_mather, a.power_supply LIMIT 100')
datas_PS = graph.data('MATCH (a:PS) RETURN a.id, a.name, a.col_power, a.standart LIMIT 100')

for data_case in data_cases:
    for dataPS in datas_PS:
        if data_case['a.power_supply'] == "Без Блока Питания":
            data_u7 = graph.find_one('Cases_pc', property_key='id', property_value=data_case['a.id'])
            data_u8 = graph.find_one('PS', property_key='id', property_value=dataPS['a.id'])
            ps_case = Relationship(data_u8, "PS", data_u7, power=dataPS['a.col_power'])
            graph.create(ps_case)
    for data_Mather in datas_Mather:
        form_factor = data_case['a.type_mather']
        form_factor = form_factor.split(",")
        if data_Mather['a.form_factor'] in form_factor:
            data_u1 = graph.find_one('Cases_pc', property_key='id', property_value=data_case['a.id'])
            data_u2 = graph.find_one('Motherboards', property_key='id', property_value=data_Mather['a.id'])
            case_mather = Relationship(data_u2, "Form_Factor", data_u1, form_factor=data_Mather['a.form_factor'])
            graph.create(case_mather)
        for data_CPU in datas_CPU:
            if (data_CPU['a.socket'] == data_Mather['a.socket']):
                data_u3 = graph.find_one('CPU', property_key='id', property_value =data_CPU['a.id'])
                data_u4 = graph.find_one('Motherboards', property_key='id', property_value =data_Mather['a.id'])
                cpu_mather = Relationship(data_u3, "CPU", data_u4, socket = data_Mather['a.socket'])
                graph.create(cpu_mather)
        for data_Mem in data_Mems:
            if (data_Mem['a.type_ram'] == data_Mather['a.ram']):
                data_u5 = graph.find_one('Memorys', property_key='id', property_value =data_Mem['a.id'])
                data_u6 = graph.find_one('Motherboards', property_key='id', property_value =data_Mather['a.id'])
                ram_mather = Relationship(data_u5, "RAM", data_u6, type_ram = data_Mather['a.ram'])
                graph.create(ram_mather)

