```java
package user;

import java.sql.Connection;
import java.sql.PreparedStatement;

import util.DatabaseUtil;

public class UserDAO {	// DAO 데이터 베이스에 직접적으로 접근을 한다는 의미
	
	public int join(String userID, String userPassword) {	// 반환값이 int형, join함수.
		String SQL = "INSERT INTO USER VALUES (?, ?)";
		try {
			Connection conn = DatabaseUtil.getConnection();
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			pstmt.setString(1, userID);	// 첫 번째 ?에 userID 저장
			pstmt.setString(2, userPassword);	// 두 번째 ?에 userPassword 저장
			return pstmt.executeUpdate();	// 명령어를 수행한 결과를 리턴
		} catch (Exception e) {
			e.printStackTrace();
		}
		return -1;
	}
}
```

> pstmt.executeUpdate(); 에서 INSERT 문이 실행이 되서 데이터를 한개 넣었다면 1이란 값이 반환,
>
> 넣지않았다면 0이란 값 반환. INT형식이므로 public int join(){} g형식으로 받음.