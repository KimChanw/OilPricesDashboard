# 일별 금/은 원자재 가격 분석 및 시각화
> ### 5조 2팀 프로그래머스 데이터 엔지니어링 데브코스 1차 팀 프로젝트 

<BR>

## 프로젝트 소개
> ###  안전자산으로 취급받는 원자재인 금/은의 일별 가격 변동을 나스닥 API를 이용하여 차트 형태로 제공하고, 기술적 분석을 이용한 원자재 매수/매도 신호를 제공하는 프로젝트

<BR>

## 제공 서비스
### 설정 기간 기준 일자 별 WTI / Brent유 가격 추세 그래프

<BR>

## 참여 조원
- #### 공동 작업 : 백엔드 로직 및 S3와 Snowflake를 이용한 데이터 웨어하우스 구축
1. 김찬우 : 데이터 시각화 및 프론트엔드 작업
2. 이태현 : API를 통한 데이터 수집
3. 김동석 : API를 통한 데이터 수집
4. 국승원 : 데이터 시각화 및 프론트엔드 작업
5. 임찬우 : 데이터 시각화 및 프론트엔드 작업

<BR>

## 개발 과정
1. 한국인행 Open API를 통해 2013년 1월~ 2023년 5월 2일까지 WTI / 브렌트유 가격 정보를 수집
2. 받은 데이터를 csv 형식으로 S3에 저장, Snowflake에 Bulk
3. 유가 차트 및 분석 결과 시각화 제공
4. 프로젝트 결과물 통합 실험 및 데모

<BR>

## 활용 기술 및 프레임워크
#### 1. front-end : `html/css`
    - visualization : matplotlib, seaborn

#### 2. back-end : `Python, Django`
    - Data Preprocessing : pandas

#### 3. Data Warehouse
    - 데이터 적재 : AWS S3, Snowflake

#### 4. 협업 도구 : `GitHub, Slack, Notion, Gather`

## 예시 화면
![image](https://github.com/KimChanw/OilPricesDashboard/assets/50550972/a14bb7b0-dff1-491a-b7a8-84e5fc56b88a)

![image](https://github.com/KimChanw/OilPricesDashboard/assets/50550972/4c458e00-cefd-4668-b28c-5c0dd4fd4578)

![image](https://github.com/KimChanw/OilPricesDashboard/assets/50550972/694d1834-9336-4591-817f-7da8c87c03cd)
