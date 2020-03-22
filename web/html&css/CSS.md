## CSS 

글자 수 초과 (...) 으로 보이게 하기 : **white-space: nowrap; overflow: hidden; text-overflow: ellipsis;**

toggle 사용법 익혀두기( ex. id=toggle & for=toggle )

**@import css/stylesheet.css** : head style 태그 안 상단에 적어서 link 태그 대신에 사용할 수 있는 방법.

```css
div { width: 100%; overflow: hidden; }
div > div:nth-child(1) { width: 250px; float: left; }
div > div:nth-child(2) { width: 100%; float: left; margin-right: -250px; }
div > div:nth-child(2) > p { padding: 250px; }
```

> 태블릿 레이아웃 화면 벗어날 때 처리하는 법.

```css
html { height: 100% }
body { height: 100% }
#top_bar { position: fixed; top: 0; left: 0; right: 0; height: 100px; }
#bottom_bar { posigion: fixed; bottom: 0; left: 0; right: 0; height: 100px; }
#left_bar { position: fixed; top: 100px; bottom: 100px; left: 0; width: 300px; }
#right_bar { position: fixed; top: 100px; bottom: 100px; right: 0; width: 410px; }
#wrap { margin: 100px 410px 100px 300px; }
```

> 주로 테블릿 피시에서 많이 사용되는 위 아래 파티션을 고정해두는 방법.
>
> 주의 할 점은 width와 height을 100%로 주고 이 방법을 사용할 시 가운데 있는 파티션은 영역이 겹치므로
>
> 위의 방법처럼 **margin을 위 아래 양 옆의 겹치는 부분에 대해서 적어주어야 한다.**

```html
<style>
    @media screen {
        #wrap .content { background-color: #525252; }
    }
    @media print { 
        #wrap .content { background-color: #ffffff; }
    }
</style>
<link rel="stylesheet" href="title.css" />
<link rel="stylesheet" href="content.css" media="screen" />
<link rel="stylesheet" href="content.css" media="print" />
<link rel="stylesheet" href="date.css" />
```

> 화면상 보이는 화면과 인쇄 시 출력되는 화면을 다르게 설정할 수 있다.
>
> 보통 컬러가 진하게 들어간 경우 print 속성을 사용하여 흑백을 설정해 줄 수 있다.
>
> style 태그 안에 적용시키는 방법과 link 태그를 사용하는 방법이 있다.

```html
<style>
    @media screen and (max-width:767px) {
        #wrap { width: 100%; }
        #content_wrap #content p { font-size: 3em; font-weight: bold; }
    }

    @media screen and (min-width:768px) and (max-width:959px) {
		#wrap { width: 100%; }
		#content_wrap #content p { font-size: 1.5em; font-weight: bold; }
    }
    
    @media screen and (min-width: 960px) {
    	#wrap { width: 80%; }
    	#content_wrap #content p { font-size: 1em; font-weight: bold; }
    }
</style>
```

> 맨 위부터 가로 0px에서 767px 까지 모바일 화면의 css 설정.
>
> 중간 768 ~ 959 픽셀까지의 태블릿 화면 css 설정, 맨 밑 960픽셀부터 피시화면 css설정
>
> 반응형 웹이라고 한다. 하나의 html과 css를 통해 조금의 설정으로 기기에 따른 반응형 웹을 구축할 수 있따.

### Grid : 미리 정해놓은 레이아웃을 통해 작업하는 것.

> 기존 방식이 익숙하다면 grid를 사용할 필요는 없지만 다른 사람의 소스코드를 본다던가 협업할 시 사용
>
> 할 수 있기 때문에 깊게는 아니더라도 어느정도는 알아두는게 좋다.

### 전체적인 레이아웃 제작할 때 필요한 가상 이미지 사이트

> http://placehold.it/100x100	: 너비  x 높이 설정하면 된다.

