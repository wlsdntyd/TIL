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
  - `git switch new` new라는 세상으로 이동 (=checkout)
  - git merge new 합치는 과정, 중심이 될 곳에서 병합
    - 관리자모드에서 esc연타 후 wq 작성(저장 후 나옴)
  - git log --oneline --graph 그래프 형식으로 보여줌
  - https://git-school.github.io/visualizing-git/  git 연습 도구
  - git branch -d new 뉴라는 세상을 지움
  - merge fast forward
  - git merge new --no-ff : fast forward 하지 않는 법
  - git switch -c new 브랜치 만들면서 이동
  
- ### Merge Conflict

  #### 1. Fast Forward Merge

  branch merge가 일어났지만 merge시점에서 branch 한쪽에서만 commit들이 쌓여있는 경우

  새로운 세계(new)에서만 commit이 잇고 master에는 없었을때

  #### 2. Auto-merge

  merge 시점에 양쪽 브랜치에 commit이 쌓여있지만 conflict가 발생하지 않는 경우, 

  #### 3. Merge Conflic 발생

  merge 시점에 양쪽 브랜치에 commit이 쌓여있지만 conflict가 발생하는 경우, 

  - 같은 파일내에 상충하는 내용이 있을 경우

- ### Merge 과정

  1. 브랜치 생성 후 일부 내용 수정 
  2. 마스터로 이동 후 머지
  3. 충돌 파일 메모장으로 열어 둘 중 하나 고르기 원하는 내용 남기고 저장
  4. git add (파일명) 수정 파일 등록
  5. git commit -m "내용" 