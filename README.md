# project_3 (PPT 있습니다!)


눈치싸움이라는 말, 들어본 적 있으시죠?

눈치싸움 실패도, 성공도 해보셨으리라 생각됩니다.

2022년 05월 05일 서울대공원을 간 차량은 최소 1,749대로 한 차량에 두 명만 잡아도 3,498명이라는 걸 알 수 있습니다.

날씨를 이용하여 굉장히 많은 인파가 한꺼번에 몰릴 수 있는 날을 예측해보고자 합니다.



## ⭐ 프로젝트 주제 : 서울대공원 눈치 싸움에서 이겨보자 !  (기온 및 강수량에 따른 일 방문객 혼잡도 예측)

------------------------------------------------------------------------------------------------------------------------------

## 결론


### <데이터>

- 서울대공원 입장객 정도.csv(서울 열린 데이터 광장), 서울 일별 강수량.csv, 서울 일별 기온.csv(기상청 기상자료개방포털)

- 컬럼 : 날짜, 요일, 일 고객 방문 수(유료, 무료), 평균 기온, 최저 기온, 최고 기온, 강수량   <- 중 날짜, 일 고객 방문 수, 평균 기온, 강수량 사용

- 2018.01.01 ~ 2022.06.31 기간

- ⭐ 타겟 : 일 고객 방문 수 (혼잡도를 파악하기 위해 월 별 7,000명 미만 - 0,  7,000명 이상 - 1)

------------------------------------------------------------------------------------------------------------------------------

### <서비스 소개>

- 기온 및 강수량에 따른 일 방문객 혼잡도 예측 서비스

- 사용자가 기온과 강수량을 입력하면 서울대공원이 혼잡 예정인지 아닌지를 알려주는 서비스

------------------------------------------------------------------------------------------------------------------------------

### <파이프라인>

- 데이터 : 서울대공원 입장객 정도.csv(서울 열린 데이터 광장), 서울 일별 강수량.csv, 서울 일별 기온.csv(기상청 기상자료개방포털)

- 파이썬으로 전처리

- sqlite에 DB 적재

- Metabase에 대시보드 생성

- 랜덤 포레스트로 모델링

- Flask를 통해 서버를 개발

------------------------------------------------------------------------------------------------------------------------------

### <대시보드>

- row : 1,642

- 평균 기온 가장 높은 달 : 2018년 7월(27.8도), 8월(28.7도) 굉장히 높음  /  2021년 7월(28.1도), 8월(25.8도) 굉장히 높음

- 월 방문객 입장 수 : 2018년 7월(76,303명), 8월(65,551명) 굉장히 낮음  /  2018년 7월(35,687명), 8월(74,651명) 굉장히 낮음

------------------------------------------------------------------------------------------------------------------------------

- 평균 강수량 가장 높은 달 : 2020년 7월(22건), 8월(20건) 굉장히 높음  /  2021년 8월(20건) 굉장히 높음

- 월 방문객 입장 수 : 2020년 7월(87,991명), 8월(40,331명) 굉장히 낮음  /  2021냔 8월(35,687명) 굉장히 낮음

------------------------------------------------------------------------------------------------------------------------------

- 2019년 12월 31일부터 시작된 코로나 바이러스의 일환으로 방문객 수가 급격히 줄어든 점 감안해야 함

- 가정의 달인 5월과 추석과 단풍이 예쁜 9월 10월은 항상 방문객 수가 높았음  -->  참고하여 방문할 것


------------------------------------------------------------------------------------------------------------------------------

### <대시보드>

- 로지스틱 회귀 분석을 사용한 모델링

- 11월 2일부터 11월 12일까지의 서울대공원 기상 정보 

- [10.5, 0], [4.0, 0], [9.5, 0], [10.5, 0], [13, 0], [9, 0], [6.5, 0], [9.0, 0], [11.0, 0], [12.5, 0], [11, 0], [17, 0]  (기온, 강수량)

- [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1]  (혼잡 - 1, 혼잡 X - 0)

- 예시로 [17, 0]을 넣으면 1이 나옴  /  [17, 3]을 넣으면 0이 나옴

------------------------------------------------------------------------------------------------------------------------------

### <플라스크>

- 혼잡할 경우(결과값 1) 결과값 : 혼잡할 예정입니다. 참고하여 방문하세요. ㅠ_ㅠ

- 혼잡하지 않을 경우(결과값 0) 결과값 : 혼잡하지 않을 예정입니다. 즐거운 방문 되세요! ^_^

------------------------------------------------------------------------------------------------------------------------------

### <개선 방향>

- 대시보드 2018부터 2022년 모든 월 별로 제작  -->  각 년도의 월 별로 제작하면 더 보기 편할 것 같음 (e.g. 2022년 01~06월 강수량)

- 모델링 할 때 요일을 구분하여 제작하지 못 함  -->  평일과 주말을 구분하여 제작한다면 더 정확한 결과를 얻을 수 있을 것 같음



