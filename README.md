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


- 네이버 영화 리뷰 수집 : https://movie.naver.com/


- Amazon 리뷰 수집 : https://www.amazon.com/
1. BeautifulSoup을 이용해 50페이지 Crawling
2. Selenium을 이용해 50페이지 Crawling
3. 이 둘의 구동 시간을 비교

### 결과
time.sleep 함수를 감안한 구동시간 측정 -> Selenium이 더 빠른 것으로 확인

원래 BeautifulSoup이 더 빨라야 함. 결과가 다르게 나온 이유 조사하기.




- Covid-19 90개국 데이터 수집 : https://coronaboard.kr/
1. 전세계 인구 top 90 개국의 10개 정보(국가, 확진자, 환자, 사망자, 완치, 치명율, 완치율, 발생율, 인구수, 국토 면적)를 추출
2. 이 parameter 중 하나를 중점으로 다른 parameter와의 상관관계를 조사
3. 데이터를 시각화

---

## 자연어 처리

### konlpy를 이용한 자연어 처리 및 영화 리뷰정보 시각화

- 구글 Colab 환경에서 구동

| Module | Version |  설명  |
| ------ | ------- | ------ |
| konlpy | 0.5.2 | 한국인이 개발한 한글 자연어 처리 모듈 |
| nltk | 3.2.5 | nltk를 이용해 더 많은 자연어 처리 기능을 사용할 수 있음 |
| matplotlib | 3.3.2 | 그래프 출력 및 추가 정보 삽입 등 모든 plot의 기초를 지원 | 
| wordcloud | 1.5.0 | 텍스트 시각화를 지원하는 모듈 |
| PIL | 7.1.2 | 외부 이미지를 불러옴 |

- Okt, Kkma, Hannanum, mecap 등 다양한 한글 자연어 처리기를 이용하고 성능을 비교함
- 이를 이용해 네이버 영화리뷰를 불러와 의미있는 정보만을 WordCloud를 이용해 시각화를 진행함
- 불용어 처리를 이용해 정보를 정제

---
## Team_Project
### Covid_19_Analysis_GDP
- Covid_19_Analyze_GDP : GDP가 가장 높은 10개국과 가장 낮은 10개국을 중심으로 다양한 parameter 간의(확진자, 인구수, 국토면적, 사망자, GDP, 완치, 인구밀도 등) 상관관계와 수치를 분석했습니다. 
- 결과에 대해서 팀원과 토론했고 이를 시각화 해보았습니다.

### Medical_Check_Analysis
- 국민건강보험공단에서 베포하는 건강검진 정보를 여러 방면으로 분석해보았습니다.
- https://www.data.go.kr/data/15007122/fileData.do
- 2016년 ~ 2019년의 총 400만 데이터를 분석해보았으며 매우 낮은 확률로 검진 대상이 중복될 것이라고 판단해 취합하여 데이터를 사용했습니다.
- 연령대 별, 지역 별 분류해 그 특징을 파악하고 비정상적인 수치를 가진 검진자의 프로필을 파악해 경각심을 주기위한 목적입니다.
- 데이터를 여러 plotting을 이용해 시각화 해보았습니다.


---
## Today_Learn
 - 매일 공부하는 내용에 대한 리스트를 업데이트.

### 목표
 - 매일 작성을 통해서 하루의 리스트에 대한 목표를 확인한다.
 - 기록을 남겨 내가 무엇을 했는지에 대한 리스트를 나중에 확인할 수 있다.

### 방식
 - 하루에 한 번 또는 두번 올리기

### 폴더 구조
 - 현재(2020/06/24)시점, 텍스트 파일로 정리하고 있음.
 - 추후 파일이 많아지면 폴더 구조로 정리할 계획

```
├── README.md
├── today_learn_xxxxx : 내용
├── week1 : 추후 폴더
```

#### And so on..
