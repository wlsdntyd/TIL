```java
package util;

import java.sql.Connection;
import java.sql.DriverManager;

public class DatabaseUtil {
	
	public static Connection getConnection() {	// 접속한 상태 자체를 반환하도록
		try {
			String dbURL = "jdbc:mysql://localhost:3306/TUTORIAL?serverTimezone=Asia/Seoul&useSSL=false";
			String dbID = "root";
			String dbPassword = "1234";
			Class.forName("com.mysql.jdbc.Driver");
			return DriverManager.getConnection(dbURL, dbID, dbPassword);
		}	catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}
}
```

> 실제로 데이터베이스와 연동된 상태인 연결 자체를 관리할 수 있다.