# LikeLion
 멋쟁이 사자처럼

## Web_crawling

### BeautifulSoup과 selenium을 이용해 웹 상의 다양한 정보를 수집해 csv 파일로 저장

| Module | Version |  설명  |
| ------ | ------- | ------ |
| pandas | 1.1.3 | 수집한 정보를 DataFrame화 |
|  bs4   | 4.9.3 | 페이지 내부의 source에 직접적으로 접근 |
| selenium | 3.141.0 | 페이지 상에서 동작 후 find_element를 통해 정보에 접근 |
| seaborn | 0.11.0 | 스캐터 플롯, 히트맵 등 다양한 시각화 지원 |
| matplotlib | 3.3.2 | 그래프 출력 및 추가 정보 삽입 등 | 

---

- 네이버 영화 리뷰 수집 : https://movie.naver.com/

---

- Amazon 리뷰 수집 : https://www.amazon.com/
1. BeautifulSoup을 이용해 50페이지 Crawling
2. Selenium을 이용해 50페이지 Crawling
3. 이 둘의 구동 시간을 비교

---

- Covid-19 90개국 데이터 수집 : https://coronaboard.kr/
1. 전세계 인구 top 90 개국의 10개 정보(국가, 확진자, 환자, 사망자, 완치, 치명율, 완치율, 발생율, 인구수, 국토 면적)를 추출
2. 이 parameter 중 하나를 중점으로 다른 parameter와의 상관관계를 조사
3. 데이터를 시각화

---
#### And so on..
