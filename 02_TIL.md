## Git

- ### 파일 생성 및 제거

  - `rm`: 파일을 지우는 명령어
  - `rm -r` : 폴더를 지우는 명령어
  - `mkdir` :  폴더 생성하는 명령어
  - `touch 파일명.확장자명` : 파일 생성하는 명령어

- ### Git 상태 및 추적

  - `git log` : 기록 보기
  - `git log --oneline` : 기록 한줄 보기
  - `git status` : git 상태보기

- ### Github 파일 추가

  - `git add` <파일이름> -이 명령어로 인덱스에 추가
  - `git commit -m` : "메모" - head에 반영

- ## 이것 저것

  - `ls` : 폴더 내부 파일, 폴더 나열
  - `ls -a` : 숨김파일 같이 나열
  - `pwd` : 현재 폴더 경로 추적
  - `cd` 폴더명 : 폴더로 이동
  - `cd ..` : 상위 폴더로 이동
  - `cd ~` : 홈으로 이동
  - `git init` : 폴더를 깃으로 설정(master)

- ### 이메일, 이름 설정하기

  - **git config --global user.email["이메일"]**
  - **git config --global user.name["이름"]**

- ### Github에 파일 추가

  - `git remote add` <원격저장소 이름> <원격 서버 주소>
  - `git pull origin(폴더명) master`
  - `git add` 파일이름

- ### Git branch

  - 가상 세계를 만들고 작업을 하기 위함,
  - `git branch new ` new라는 세상을 만듬
  - `git switch new` new라는 세상으로 이동
  - Head 