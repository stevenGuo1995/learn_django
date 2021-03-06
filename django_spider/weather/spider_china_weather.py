import requests
from bs4 import BeautifulSoup


def get_china_by_url(url: str):
    # 获取数据
    response = requests.get(url)
    requests_str = response.content.decode('utf-8')

    # 解析数据
    soup = BeautifulSoup(requests_str, 'lxml')
    get_content01 = soup.find('div', id="selectprovince")
    provinces = get_content01.find_all('div', attrs={'value': True})
    provinces_list = []
    for index, province in enumerate(provinces):
        if index == 0:
            continue

        province_url = 'http://www.nmc.cn/publish/forecast/' + province.attrs['value'] + '.html'
        provinces_dict = {
            province.text.strip(): get_data_by_url(province_url)[1],
            'provinceURL': province_url
        }
        provinces_list.append(provinces_dict)
    return provinces_list


def get_data_by_url(url: str):
    # 获取数据
    response = requests.get(url)
    requests_str = response.content.decode('utf-8')

    # 解析数据
    soup = BeautifulSoup(requests_str, 'lxml')
    one_province = soup.find_all('div', class_='area')
    res_list = []
    for item in one_province:
        cities = item.find_all('div', class_='cname')
        weathers = item.find_all('div', class_='weather')
        temps = item.find_all('div', class_='temp')
        temp_list = []

        for index, city in enumerate(cities):
            temp = str(temps[index].text).strip().replace('\n', '')
            max_temp, min_temp = temp[:-1].split('/')
            temp_dict = {
                'city': str(city.text).strip().replace('\n', ''),
                'weather': str(weathers[index].text).strip().replace('\n', ''),
                'max_temp': max_temp,
                'min_temp': min_temp
            }
            temp_list.append(temp_dict)
        res_list.append(temp_list)
    return res_list


if __name__ == '__main__':
    # url = 'http://www.nmc.cn/publish/forecast/china.html'
    # province_all = get_china_by_url(url)
    # print(province_all)
    import datetime
    s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(s)
