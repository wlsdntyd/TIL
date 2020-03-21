## CSS 

글자 수 초과 (...) 으로 보이게 하기 : **white-space: nowrap; overflow: hidden; text-overflow: ellipsis;**

toggle 사용법 익혀두기

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

