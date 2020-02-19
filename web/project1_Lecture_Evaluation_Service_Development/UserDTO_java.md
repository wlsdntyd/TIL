```java
package user;
						// DTO : data transfer object 데이터 객체 전송
public class UserDTO {	// 실질적으로 접근하는 건 DAO, DTO는 데이터 객체 저장과 전송

	private String userID;
	private String userPassword;
	private String userEmail;
	private String userEmailHash;
	private boolean userEmailChecked;
	public String getUserID() {
		return userID;
	}
	public void setUserID(String userID) {
		this.userID = userID;
	}
	public String getUserPassword() {
		return userPassword;
	}
	public void setUserPassword(String userPassword) {
		this.userPassword = userPassword;
	}
	public String getUserEmail() {
		return userEmail;
	}
	public void setUserEmail(String userEmail) {
		this.userEmail = userEmail;
	}
	public String getUserEmailHash() {
		return userEmailHash;
	}
	public void setUserEmailHash(String userEmailHash) {
		this.userEmailHash = userEmailHash;
	}
	public boolean isUserEmailChecked() {
		return userEmailChecked;
	}
	public void setUserEmailChecked(boolean userEmailChecked) {
		this.userEmailChecked = userEmailChecked;
	}
    // 생성자 만들어줌. 빈 것과 안 빈 것 ㅋ
    public UserDTO() {
        // 하나의 user라는 이름의 인스턴스를 처리할 수 있도록 만듬.
        // 즉 초기화 시키기위해 만듬.
    }
	public UserDTO(String userID, String userPassword, String userEmail, String userEmailHash,
			boolean userEmailChecked) {
		super();
		this.userID = userID;
		this.userPassword = userPassword;
		this.userEmail = userEmail;
		this.userEmailHash = userEmailHash;
		this.userEmailChecked = userEmailChecked;
	}
	
}

```

> package 를 user로 같게 써서 DB 의 USER 테이블과 1 : 1 매칭 시켜줌. java source code 로 모델링을 해줌.
>
> getters and setters 로 각 변수에 함수 형태로 접근 가능하게 해줌.
>
> 마우스 우 클릭 source >> generate constructor using field >> 현재 변수의 생성자를 만들어 줌.
>
> 생성자 함수 : 객체 변수에 값을 무조건 설정해야만 객체가 생성될 수 있도록 강제하는 법
>
> 생성자 규칙 : 클래스명과 메소드명이 동일해야한다. 리턴 타입을 정의하지 않는다.