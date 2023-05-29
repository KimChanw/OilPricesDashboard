import requests
import pandas as pd
    
def request_oil_data_to_koreabank(code, start_month='201301', end_month='202305'):
    """한국은행 api에서 2013년 1월 데이터를 시작으로 2023년 5월 데이터를 json 형식으로 가져 옴"""
    url = f"http://ecos.bok.or.kr/api/StatisticSearch/31UBAU5ICJLA5OP0XUD4/json/kr/1/200/902Y003/M/{start_month}/{end_month}/{code}/" 
    
    res = requests.get(url)
    
    if res.status_code != 200:
        raise ConnectionError
    
    result_json = res.json()['StatisticSearch']['row']
    return result_json

def make_oil_price_df(response_json):
    """json 응답 결과를 토대로 시간과 """
    time_list = []
    oil_price_list = []
    
    # 결과 json 내 가격 및 날짜 value를 리스트에 추가
    for price_infomation in response_json:
        time_data = price_infomation['TIME']
        
        # TIME 컬럼의 데이터는 202305 형식이므로 YYYY-MM 형식으로 재구성
        time_data = f'{time_data[:4]}-{time_data[4:]}'
        
        oil_price = price_infomation['DATA_VALUE']

        
        time_list.append(time_data)
        oil_price_list.append(oil_price)
    
    oil_price_df = pd.DataFrame({
        'time' : time_list,
        'oil_price' : oil_price_list
    })
    
    return oil_price_df
    
if __name__ == '__main__':
    # 1. wti 가격 데이터 csv
    wti_code = 4010101
    wti_json = request_oil_data_to_koreabank(wti_code)
    wti_df = make_oil_price_df(wti_json)
    
    wti_df.to_csv('wti.csv')

    # 2. 브렌트유 가격 데이터 csv
    brent_code = 4010103
    brent_json = request_oil_data_to_koreabank(brent_code)
    brent_df = make_oil_price_df(brent_json)
    
    brent_df.to_csv('brent.csv')