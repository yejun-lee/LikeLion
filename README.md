# LikeLion
 멋쟁이 사자처럼

## Web_crawling

### BeautifulSoup과 selenium을 이용해 웹 상의 다양한 정보를 수집해 csv 파일로 저장

| Module | Version |  설명  |
| ------ | ------- | ------ |
| pandas | 1.1.3 | 수집한 정보를 DataFrame화 |
|  bs4   | 4.9.3 | 페이지 내부의 html정보에 직접적으로 접근 |
| selenium | 3.141.0 | 페이지 상에서 동작 후 find_element를 통해 정보에 접근 |

- 네이버 영화 리뷰 수집

- Amazon 리뷰 수집
1. BeautifulSoup을 이용해 50페이지 Crawling
2. Selenium을 이용해 50페이지 Crawling
3. 이 둘의 구동 시간을 비교
