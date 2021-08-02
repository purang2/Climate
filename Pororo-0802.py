# -*- coding: utf-8 -*-
"""
Pororo at 카카오브레인 

@은찬 


@author: PC
"""

from pororo import Pororo 


import pandas as pd

train= pd.read_csv('train_maxlen_500.csv')
#test=pd.read_csv('test_maxlen_500.csv')
#sample_submission=pd.read_csv('data/dacon-data/sample_submission.csv')


example = train[:100]


#print(Pororo.available_tasks())



#Zero-shot Topic Classification
#https://kakaobrain.github.io/pororo/


zsl = Pororo(task="zero-topic", lang= "ko")



#zsl_1 = zsl('''라리가 사무국, 메시 아닌 바르사 지지..."바이 아웃 유효" [공식발표]''', ["스포츠", "사회", "정치", "경제", "생활/문화", "IT/과학"])

#print(zsl_1)


#1줄에 5개씩 보기좋게 끊어서 쓰기 

'''
data_query 양식 

"21. 온실가스 고정 CCUS" 



'''

data_query = ["기후변화로 인하여 작물 및 가축 생산에 영향을 이해하는 데 필요한 기술 및 기후변화로 인한 농업 축산 생산성 감소 등 부정적 영향을 최소화 시키는 기술 유전자 개량","기후변화로 인하여 작물 및 가축 생산에 영향을 이해하는 데 필요한 기술 및 기후변화로 인한 농업 축산 생산성 감소 등 부정적 영향을 최소화 시키는 기술 작물 재배 생산 농약 아열대 작물 농산물 가공","기후변화로 인하여 작물 및 가축 생산에 영향을 이해하는 데 필요한 기술 및 기후변화로 인한 농업 축산 생산성 감소 등 부정적 영향을 최소화 시키는 기술 폐기물 생물학적 스트레스","기후변화로 인하여 작물 및 가축 생산에 영향을 이해하는 데 필요한 기술 및 기후변화로 인한 농업 축산 생산성 감소 등 부정적 영향을 최소화 시키는 기술 농산물 가공 저장 유통 가축 관리 축산 부산물"
              "1. 비재생 에너지 원자력 발전", "2. 비재생 에너지 핵융합 발전" ,"3. 비재생 에너지 청정화력 발전,효율화", "4. 재생 에너지 수력","5. 재생 에너지 태양광",
         "6. 재생 에너지 태양열","7. 재생 에너지 지열","8. 재생 에너지 풍력","9. 재생 에너지 해양에너지","10. 재생 에너지 바이오에너지",
         "11. 재생 에너지 폐기물","12.신에너지 수소제조","13.신에너지 연료전지","14. 에너지 저장 전력저장","15. 에너지 저장 수소저장",
         "16. 송배전 전력 IT 송배전 시스템","17. 송배전 전력 IT 전기지능화 기기","18.에너지 수요 수송효율화","19.에너지 수요 산업효율화","20.에너지 수요 건축효율화",
         "21. 온실가스 고정 CCUS 이산화탄소 포집,활용,저장","22. 온실가스 고정 NON-Co2 이산화탄소 저감","23.농업, 축산 유전자원 유전개량","24.농업 축산 작물재배 생산","25.농업 축산 가축 질병 관리",
         "26. 농업 축산 가공, 저장, 유통","27. 물관리 수계 수생태계","28.물관리 수자원 확보 및 공급","29.물관리 수처리","30.물관리 수재해 재해 관리",
         "31. 기후변화예측 및 모니터링 기후 예측 및 모델링","32. 기후변화예측 및 모니터링 기후 정보, 경보 시스템","33.해양 수산 연안 해양생태계","34.해양 수산 연안 수산자원","35.해양 수산 연안 연안재해 관리",
         "36. 건강 감염 질병 관리","37. 건강 식품 안전 예방","38.산림 육상 산림 생산 증진","39.산림 육상 산림 피해 저감","40.산림 육상 생태 모니터링 ,생태 복원",
         "41. 다분야 융복합 신재생에너지 하이브리드","42. 다분야 융복합 저전력 소모 장비","43.다분야 융복합 에너지하베스팅 에너지 하베스팅","44.다분야 융복합 인공광합성 인공 광합성","45.다분야 융복합 분류체계로 다루기 어려운 기후변화 관련 기타 기술",
         "비재생 에너지 원자력 발전", "비재생 에너지 핵융합 발전" ,"비재생 에너지 청정화력 발전,효율화", "재생 에너지 수력","재생 에너지 태양광",
         "재생 에너지 태양열","재생 에너지 지열","재생 에너지 풍력","재생 에너지 해양에너지","재생 에너지 바이오에너지",
         "재생 에너지 폐기물","신에너지 수소제조","신에너지 연료전지","에너지 저장 전력저장","에너지 저장 수소저장",
         "송배전 전력 IT 송배전 시스템","송배전 전력 IT 전기지능화 기기","에너지 수요 수송효율화","에너지 수요 산업효율화","에너지 수요 건축효율화",
         "온실가스 고정 CCUS 이산화탄소 포집,활용,저장","온실가스 고정 NON-Co2 이산화탄소 저감","농업, 축산 유전자원 유전개량","농업 축산 작물재배 생산","농업 축산 가축 질병 관리",
         "농업 축산 가공, 저장, 유통","물관리 수계 수생태계","물관리 수자원 확보 및 공급","물관리 수처리","물관리 수재해 재해 관리",
         "기후변화예측 및 모니터링 기후 예측 및 모델링","기후변화예측 및 모니터링 기후 정보, 경보 시스템","해양 수산 연안 해양생태계","해양 수산 연안 수산자원","해양 수산 연안 연안재해 관리",
         "건강 감염 질병 관리","건강 식품 안전 예방","산림 육상 산림 생산 증진","산림 육상 산림 피해 저감","산림 육상 생태 모니터링 ,생태 복원",
         "다분야 융복합 신재생에너지 하이브리드","다분야 융복합 저전력 소모 장비","다분야 융복합 에너지하베스팅 에너지 하베스팅","다분야 융복합 인공광합성 인공 광합성","다분야 융복합 분류체계로 다루기 어려운 기후변화 관련 기타 기술"]


#다분야 융복합이라는 말 뺀 쿼리
data_query2 = ["23.기후변화로 인하여 작물 및 가축 생산에 영향을 이해하는 데 필요한 기술 및 기후변화로 인한 농업 축산 생산성 감소 등 부정적 영향을 최소화 시키는 기술 유전자 개량","기후변화로 인하여 작물 및 가축 생산에 영향을 이해하는 데 필요한 기술 및 기후변화로 인한 농업 축산 생산성 감소 등 부정적 영향을 최소화 시키는 기술 작물 재배 생산 농약 아열대 작물 농산물 가공","기후변화로 인하여 작물 및 가축 생산에 영향을 이해하는 데 필요한 기술 및 기후변화로 인한 농업 축산 생산성 감소 등 부정적 영향을 최소화 시키는 기술 폐기물 생물학적 스트레스","기후변화로 인하여 작물 및 가축 생산에 영향을 이해하는 데 필요한 기술 및 기후변화로 인한 농업 축산 생산성 감소 등 부정적 영향을 최소화 시키는 기술 농산물 가공 저장 유통 가축 관리 축산 부산물"
              "1. 비재생 에너지 원자력 발전", "2. 비재생 에너지 핵융합 발전" ,"3. 비재생 에너지 청정화력 발전,효율화", "4. 재생 에너지 수력","5. 재생 에너지 태양광",
         "6. 재생 에너지 태양열","7. 재생 에너지 지열","8. 재생 에너지 풍력","9. 재생 에너지 해양에너지","10. 재생 에너지 바이오에너지",
         "11. 재생 에너지 폐기물","12.신에너지 수소제조","13.신에너지 연료전지","14. 에너지 저장 전력저장","15. 에너지 저장 수소저장",
         "16. 송배전 전력 IT 송배전 시스템","17. 송배전 전력 IT 전기지능화 기기","18.에너지 수요 수송효율화","19.에너지 수요 산업효율화","20.에너지 수요 건축효율화",
         "21. 온실가스 고정 CCUS 이산화탄소 포집,활용,저장","22. 온실가스 고정 NON-Co2 이산화탄소 저감","23.농업, 축산 유전자원 유전개량","24.농업 축산 작물재배 생산","25.농업 축산 가축 질병 관리",
         "26. 농업 축산 가공, 저장, 유통","27. 물관리 수계 수생태계","28.물관리 수자원 확보 및 공급","29.물관리 수처리","30.물관리 수재해 재해 관리",
         "31. 기후변화예측 및 모니터링 기후 예측 및 모델링","32. 기후변화예측 및 모니터링 기후 정보, 경보 시스템","33.해양 수산 연안 해양생태계","34.해양 수산 연안 수산자원","35.해양 수산 연안 연안재해 관리",
         "36. 건강 감염 질병 관리","37. 건강 식품 안전 예방","38.산림 육상 산림 생산 증진","39.산림 육상 산림 피해 저감","40.산림 육상 생태 모니터링 ,생태 복원",
         "41.신재생에너지 하이브리드","42.저전력 소모 장비","43.에너지하베스팅 에너지 하베스팅","44.인공광합성 인공 광합성","45.분류체계로 다루기 어려운 기후변화 관련 기타 기술",
         "비재생 에너지 원자력 발전", "비재생 에너지 핵융합 발전" ,"비재생 에너지 청정화력 발전,효율화", "재생 에너지 수력","재생 에너지 태양광",
         "재생 에너지 태양열","재생 에너지 지열","재생 에너지 풍력","재생 에너지 해양에너지","재생 에너지 바이오에너지",
         "재생 에너지 폐기물","신에너지 수소제조","신에너지 연료전지","에너지 저장 전력저장","에너지 저장 수소저장",
         "송배전 전력 IT 송배전 시스템","송배전 전력 IT 전기지능화 기기","에너지 수요 수송효율화","에너지 수요 산업효율화","에너지 수요 건축효율화",
         "온실가스 고정 CCUS 이산화탄소 포집,활용,저장","온실가스 고정 NON-Co2 이산화탄소 저감","농업, 축산 유전자원 유전개량","농업 축산 작물재배 생산","농업 축산 가축 질병 관리",
         "농업 축산 가공, 저장, 유통","물관리 수계 수생태계","물관리 수자원 확보 및 공급","물관리 수처리","물관리 수재해 재해 관리",
         "기후변화예측 및 모니터링 기후 예측 및 모델링","기후변화예측 및 모니터링 기후 정보, 경보 시스템","해양 수산 연안 해양생태계","해양 수산 연안 수산자원","해양 수산 연안 연안재해 관리",
         "건강 감염 질병 관리","건강 식품 안전 예방","산림 육상 산림 생산 증진","산림 육상 산림 피해 저감","산림 육상 생태 모니터링 ,생태 복원",
         "신재생에너지 하이브리드","저전력 소모 장비","에너지하베스팅 에너지 하베스팅","인공광합성 인공 광합성","다분야 융복합 분류체계로 다루기 어려운 기후변화 관련 기타 기술"]



data_sam ='유전정보를 활용한 새로운 해충 분류군 동정기술 개발 외래 및 돌발해충의 발생조사 및 종 동정 대상해충 : 최근 새롭게 발견된 돌발 및 외래해충 외래 및 돌발해충의 분포확산 모니터링 대상해충 돌발 및 외래해충 외래 및 돌발해충의 유전적 다양성 조사 시험곤충 해충별 전국 단위 채집표본 새로운 해충분류군의 동정기술 개발 및 유입확산 추적 새로운 돌발 및 외래해충의 신속, 정확한 동정법 향상 돌발 및 외래해충의 유입 및 확산 추적 및 유전정보 확보뉴클레오티드 염기서열, 분자마커, 종 동정, 침샘, 전사체'


output_1 = zsl(example.iloc[0]['data'],data_query)

print(output_1)
james = max(output_1, key=output_1.get)

print(james)



output_2 = zsl(data_sam,data_query)

print(output_2)
james2 = max(output_2, key=output_2.get)

print(james2)


output_3 = zsl(data_sam,data_query2)

print(output_3)
james3 = max(output_3, key=output_3.get)

print(james3)

