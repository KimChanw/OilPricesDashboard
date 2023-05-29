import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import base64

from io import BytesIO

def _visualize_all_oils_data(total_df: pd.DataFrame):
    """정규화한 wti / 브렌트유 가격 데이터를 받아 시각화 이미지를 만든 후 decode 수행"""

    # Seaborn 스타일 설정
    sns.set_style('darkgrid')

    # 그림의 크기를 설정
    plt.figure(figsize=(20, 16))

    # 데이터프레임에서 정규화된 금과 은 가격 열만 선택
    normalize_df_list = total_df[['WTI', 'BRENT']]

    # 정규화된 금과 은 가격 데이터를 그래프로 그림
    plt.plot(normalize_df_list, label=['Wti', 'Brent'])

    # x축 레이블 설정
    plt.xlabel('Date')
    # y축 레이블 설정
    plt.ylabel('Price')
    # x축 틱 레이블 회전 설정
    plt.xticks(rotation=30)
    # 범례 위치 설정
    plt.legend(loc='best')
    
    # 그래프 이미지를 저장하지 않고 바이트 데이터로 변환하기 위해 버퍼 사용
    buffer = BytesIO()
    # 그래프를 png 형식으로 버퍼에 저장
    plt.savefig(buffer, format='png')
    # 버퍼 포인터를 처음으로 되돌림
    buffer.seek(0)

    # 버퍼에서 바이트 값을 가져옴
    visialization_png = buffer.getvalue()
    # 버퍼를 닫음
    buffer.close()

    # 바이트 값을 base64로 인코딩
    graphic = base64.b64encode(visialization_png)
    # 인코딩된 값을 utf-8로 디코딩하여 문자열로 변환
    graphic = graphic.decode('utf-8')

    # 최종 결과 반환
    return graphic


def _visualize_price_data(price_df: pd.DataFrame, column_name: str):
    """입력된 데이터를 토대로 시각화 이미지를 만든 후 decode하는 함수"""

    # 데이터프레임의 모든 열 이름은 대문자로 구성
    if column_name.islower():
        column_name = column_name.upper()
    
    sns.set_style('darkgrid')

    plt.figure(figsize=(20, 16))
    plt.plot(price_df[column_name])

    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Price ($)', fontsize=14)

    plt.xticks(rotation=30)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    visialization_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(visialization_png)
    graphic = graphic.decode('utf-8')

    return graphic
