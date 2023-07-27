## 주제 (최종)
- 관심있는 축구 경기 정보 받기

schedule_url = https://sports.news.naver.com/wfootball/schedule/index

- 보고싶은 경기를 시청할 수 없을 때, 스코어에 변화가 생길떄마다 현재 경기 스코어와 득점 정보를 전송
- 보고싶은 경기가 진행되는 카테고리(컵, 리그)를 먼저 정해야 함

category = ['epl', 'primera', 'bundesliga', 'seria', 'ligue1', 'denmark', 'champs', 'europa', 'uecl', 'facup', 'carlingcup', 'copadelrey', 'clubworldcup']

lineup_url = https://m.sports.naver.com/game/2023081465041892243/lineup
- (경기 시작 전) 라인업 정보가 뜨면 각 팀의 선발 명단 크롤링

record_url = https://m.sports.naver.com/game/2023081465041892243/record
- (경기 종료 후) 최종 스코어와 세부 기록 크롤링





## 후보 1
- 좋아하는 팀의 경기가 전날에 있었을 때, 경기 결과를 출력하기
- (검색하는 날을 기준) 해당하는 달의 좋아하는 팀 경기 결과 출력하기

url = https://sports.news.naver.com/wfootball/schedule/index

- 좋아하는 팀의 리그를 선택


## 후보 2
- 네이버 해외축구 기사 제목만 모아서 출력

latest_url = https://sports.news.naver.com/wfootball/news/index?isphoto=N&type=latest  
popular_url = https://sports.news.naver.com/wfootball/news/index?isphoto=N&type=popular

- 네이버 해외축구 기사(최신순) 상위 10개 제목 수집
- 네이버 해외축구 기사(인기순) 상위 10개 제목 수집
- 최신순/인기순 각 항목별로 기사 제목들을 정리해 엑셀파일에 저장
- 메일로 전송??