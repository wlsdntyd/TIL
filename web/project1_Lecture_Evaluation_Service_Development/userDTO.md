```java
package user;

public class UserDTO {
	
	String ID;
	String PASSWORD;
	public String getID() {		// GET 데이터를 가져오는 명령어
		return ID;
	}
	public void setID(String ID) {		// SET 데이터를 기록하는 명령어
		this.ID = ID;
	}
	public String getPASSWORD() {
		return PASSWORD;
	}
	public void setPASSWORD(String PASSWORD) {
		this.PASSWORD = PASSWORD;
	}	
}
```

