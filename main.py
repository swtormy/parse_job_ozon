import requests, json
from urllib.parse import unquote, quote


def parse_offers(limit=50, **kwargs):
    if kwargs.get("query") == None: kwargs.update({'query': 'query='})
    if kwargs.get("city") == None: kwargs.update({'city': ''})
    if kwargs.get("departments") == None: kwargs.update({'departments': ''})
    if kwargs.get("employment") == None: kwargs.update({'employment': ''})
    if kwargs.get("experience") == None: kwargs.update({'experience': ''})
    if kwargs.get("specialization") == None: kwargs.update({'specialization': ''})
    if kwargs.get("level") == None: kwargs.update({'level': ''})

    r = requests.get(f'https://job.ozon.ru/api/vacancy?{kwargs.get("query")}&limit={limit}{kwargs.get("city")}{kwargs.get("departments")}{kwargs.get("employment")}{kwargs.get("experience")}{kwargs.get("specialization")}{kwargs.get("level")}')

    return r.json() 

def set_query(query='query='):
    if query != 'query=': query = 'query=' + quote(query)
    return query

def get_city(city=''):
    if city != '': city = '&city=' + quote(city)
    return city

def get_departments(allDeps=False, dep_num_one=False, dep_num_two=False, dep_num_three=False,
                    dep_num_four=False, dep_num_five=False):
    if allDeps == True:
        dep_num_one = True
        dep_num_two = True
        dep_num_three = True
        dep_num_four = True
        dep_num_five = True

    if dep_num_one == True:
        dep_num_one = '&department=Ozon+Express'
    else:
        dep_num_one = ''
    if dep_num_two == True: 
        dep_num_two = '&department=Ozon+' + quote('Офис') + '+' + quote('и') + '+' + quote('Коммерция')
    else:
        dep_num_two = ''
    if dep_num_three == True: 
        dep_num_three = '&department=Ozon+' + quote('Логистика') + '+'
    else:
        dep_num_three = ''
    if dep_num_four == True: 
        dep_num_four = '&department=Ozon+' + quote('Информационные') + '+' + quote('технологии')
    else:
        dep_num_four = ''
    if dep_num_five == True: 
        dep_num_five = '&department=Ozon+' + quote('Производство')
    else:
        dep_num_five = ''

    return dep_num_one + dep_num_two + dep_num_three + dep_num_four + dep_num_five

def get_employment(allEmpls=False, full_employment=False, project_work=False, parttime_employment=False):
    if allEmpls == True: 
        full_employment = True
        project_work = True
        parttime_employment = True
    
    if full_employment == True:
        full_employment = '&employment=' + quote('Полная занятость')
    else:
        full_employment = ''
    if project_work == True:
        project_work = '&employment=' + quote('Проектная работа')
    else:
        project_work = ''
    if parttime_employment == True:
        parttime_employment = '&employment=' + quote('Частичная занятость')
    else:
        parttime_employment = ''

    return full_employment + project_work + parttime_employment

def get_experience(allExpers=False, no_experience=False, little_experience=False, average_experience=False, great_experience=False):
    if allExpers == True: 
        no_experience = True
        little_experience = True
        average_experience = True
        great_experience = True
    
    if no_experience == True:
        no_experience = '&experience=' + quote('Нет опыта')
    else:
        no_experience = ''
    if little_experience == True:
        little_experience = '&experience=' + quote('От 1 года до 3 лет')
    else:
        little_experience = ''
    if average_experience == True:
        average_experience = '&experience=' + quote('От 3 до 6 лет')
    else:
        average_experience = ''
    if great_experience == True:
        great_experience = '&experience=' + quote('Более 6 лет')
    else:
        great_experience = ''

    return no_experience + little_experience + average_experience + great_experience

def get_specialization(allSpecs=False, HR=False, Commerce=False, Corporate_IT_systems=False,
                    Marketing_advertising_PR=False, Logistics_development=False, Platform_development=False,
                    Development_of_search_technologies=False, Warehouse_development=False, Occupational_Safety_and_Health_Service=False,
                    Support_service=False, Own_sales=False, Marketplace=False, Incident_management=False, Finance=False, 
                    Data_storage_and_processing=False, Lawyers=False):
    if allSpecs == True: 
        HR = True
        Commerce = True
        Corporate_IT_systems = True
        Marketing_advertising_PR = True
        Logistics_development = True
        Platform_development = True
        Development_of_search_technologies = True
        Warehouse_development = True
        Occupational_Safety_and_Health_Service = True
        Support_service = True
        Own_sales = True
        Incident_management = True
        Finance = True
        Data_storage_and_processing = True
        Lawyers = True
    
    if HR == True:
        HR = '&specialization=' + quote('HR')
    else:
        HR = ''
    if Commerce == True:
        Commerce = '&specialization=' + quote('Коммерция')
    else:
        Commerce = ''
    if Corporate_IT_systems == True:
        Corporate_IT_systems = '&specialization=' + quote('Корпоративные ИТ системы')
    else:
        Corporate_IT_systems = ''
    if Marketing_advertising_PR == True:
        Marketing_advertising_PR = '&specialization=' + quote('Маркетинг, реклама, PR')
    else:
        Marketing_advertising_PR = ''
    if Logistics_development == True:
        Logistics_development = '&specialization=' + quote('Разработка логистики')
    else:
        Logistics_development = ''
    if Platform_development == True:
        Platform_development = '&specialization=' + quote('Разработка платформы')
    else:
        Platform_development = ''
    if Development_of_search_technologies == True:
        Development_of_search_technologies = '&specialization=' + quote('Разработка поисковых технологий')
    else:
        Development_of_search_technologies = ''
    if Warehouse_development == True:
        Warehouse_development = '&specialization=' + quote('Разработка склада')
    else:
        Warehouse_development = ''
    if Occupational_Safety_and_Health_Service == True:
        Occupational_Safety_and_Health_Service = '&specialization=' + quote('Служба безопасности и охраны труда')
    else:
        Occupational_Safety_and_Health_Service = ''
    if Support_service == True:
        Support_service = '&specialization=' + quote('Служба поддержки')
    else:
        Support_service = ''
    if Own_sales == True:
        Own_sales = '&specialization=' + quote('Собственные продажи')
    else:
        Own_sales = ''
    if Marketplace == True:
        Marketplace = '&specialization=' + quote('Торговая площадка')
    else:
        Marketplace = ''
    if Incident_management == True:
        Incident_management = '&specialization=' + quote('Управление инцидентами')
    else:
        Incident_management = ''
    if Finance == True:
        Finance = '&specialization=' + quote('Финансы')
    else:
        Finance = ''
    if Data_storage_and_processing == True:
        Data_storage_and_processing = '&specialization=' + quote('Хранение и обработка данных')
    else:
        Data_storage_and_processing = ''
    if Lawyers == True:
        Lawyers = '&specialization=' + quote('Юристы')
    else:
        Lawyers = ''


    return HR + Commerce + Corporate_IT_systems + Marketing_advertising_PR + Logistics_development + Platform_development + Development_of_search_technologies + Warehouse_development + Occupational_Safety_and_Health_Service + Support_service + Own_sales + Incident_management + Finance + Data_storage_and_processing + Lawyers

def get_level(allLevs=False, Trainee=False, Junior_Specialist=False, Specialist=False, Senior_Specialist=False, Leader=False):
    if allLevs == True:
        Trainee = True
        Junior_Specialist = True
        Specialist = True
        Senior_Specialist = True
        Leader = True

    if Trainee == True:
        Trainee = '&level=' + quote('Стажер')
    else:
        Trainee = ''   
    if Junior_Specialist == True:
        Junior_Specialist = '&level=' + quote('Младший специалист')
    else:
        Junior_Specialist = ''   
    if Specialist == True:
        Specialist = '&level=' + quote('Специалист')
    else:
        Specialist = ''   
    if Senior_Specialist == True:
        Senior_Specialist = '&level=' + quote('Старший специалист')
    else:
        Senior_Specialist = ''   
    if Leader == True:
        Leader = '&level=' + quote('Руководитель')
    else:
        Leader = ''   
    
    return Trainee + Junior_Specialist + Specialist + Senior_Specialist + Leader



