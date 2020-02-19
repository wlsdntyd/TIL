```java
package util;

import java.sql.Connection;
import java.sql.DriverManager;

public class DatabaseUtil {
	
	public static Connection getConnection() {
		try {
			String dbURL = "jdbc:mysql://localhost:3306/LectureEvaluation";
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

> 데이터 베이스에 접근해서 현재 접근된 상태인 그 객체(Connection)을 반환해주는 함수.