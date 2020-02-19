```java
package user;	// 실질적으로 데이터 베이스에 접근하는 DAO.
// 접근에 성공한 데이터베이스 객체를 이용해서 실제로 회원가입과 로그인 등 함수를 정의할 페이지.
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import util.DatabaseUtil;

public class UserDAO {
	// 로그인 함수.
	public int login(String userID, String userPassword) {
		String SQL = "SELECT userPassword FROM USER WHERE userID = ?";
        // 해당하는 userID의 비밀번호를 SQL로 가져온다.
		Connection conn = null;
        // PreparedStatement : 자바에서 데이터베이스로 쿼리문을 전송할 때 사용하는 인터페이스
        // 그냥 Statement 두 가지가 있음. 여러번 수행할 땐 preparedstatement가 빠름.
		PreparedStatement pstmt = null;
        // ResultSet : sql문의 결과값에 대해서 처리를 하고자 할 때 사용 (select)
		ResultSet rs = null;
		try {
            // conn에 user 패키지의 DatabaseUtil.java의 getConnection함수를 통해 DB에
            // 접근한 상태를 반환해줌. 초기화해줌.
			conn = DatabaseUtil.getConnection();
            // SQL문장을 실행할 수 있는 형태로 준비시켜줌
			pstmt = conn.prepareStatement(SQL);
            // 사용자로부터 입력받은 userID를 ? 부분에 넣어줌.
			pstmt.setString(1, userID);
            // query의 실행 결과 해당 userPassword 반환 그리고 rs에 넣어줌.
			rs = pstmt.executeQuery();
			if(rs.next()) {	// .next() 읽어올 때 데이터의 처음부터 읽어오므로 next를 만나면 한
                // 로우를 읽어오고 다음 로우로 내려간다. 끝까지 내려가면 끝난다.
                // rs.getString(1) >> DB에서 가져온 거, userPassword >> 사용자가 입력한 거.
				if(rs.getString(1).equals(userPassword)) {
					return 1; // 로그인 성공
				}
				else {
					return 0; // 비밀번호 틀림
				}
			}
			return -1; // 아이디 없음
		} catch (Exception e) {
			e.printStackTrace();
		} finally {	// 한번 사용하면 연결을 해제해야한다. 해제를 안시키면 다른 사람이 쓸 수 없으므로.
            // finally 문은 파이썬 문법과 같이 무조건 실행되는 구문.
			try {if(conn != null) conn.close();} catch (Exception e) {e.printStackTrace();}
			try {if(pstmt != null) pstmt.close();} catch (Exception e) {e.printStackTrace();}
			try {if(rs != null) rs.close();} catch (Exception e) {e.printStackTrace();}
		}
		return -2; // 데이터베이스 오류
	}
	public int join(UserDTO user) {	// 회원가입
		String SQL = "INSERT INTO USER VALUES (?, ?, ?, ?, false)";
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		try {
			conn = DatabaseUtil.getConnection();
			pstmt = conn.prepareStatement(SQL);
			pstmt.setString(1, user.getUserID());
			pstmt.setString(2, user.getUserPassword());
			pstmt.setString(3, user.getUserEmail());
			pstmt.setString(4, user.getUserEmailHash());
			return pstmt.executeUpdate();	// 한 개의 데이터가 들어갔다면 1 반환.
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {if(conn != null) conn.close();} catch (Exception e) {e.printStackTrace();}
			try {if(pstmt != null) pstmt.close();} catch (Exception e) {e.printStackTrace();}
			try {if(rs != null) rs.close();} catch (Exception e) {e.printStackTrace();}
		}
		return -1; // 데이터베이스 오류 회원가입 실패
	}
	public boolean getUserEmailChecked(String userID) {
		String SQL = "SELECT userEmailChecked FROM USER WHERE userID = ?";
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		try {
			conn = DatabaseUtil.getConnection();
			pstmt = conn.prepareStatement(SQL);
			pstmt.setString(1, userID);
			rs = pstmt.executeQuery();
			if(rs.next()) {	// 데이터가 존재하면 실행됨.
				return rs.getBoolean(1);	// 첫 번째, 즉 useremailchecked의 값
			}								// (true,false) 중 반환.
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {if(conn != null) conn.close();} catch (Exception e) {e.printStackTrace();}
			try {if(pstmt != null) pstmt.close();} catch (Exception e) {e.printStackTrace();}
			try {if(rs != null) rs.close();} catch (Exception e) {e.printStackTrace();}
		}
		return false; // 데이터베이스 오류 회원가입 실패
	}
	public String getUserEmail(String userID) {	// 이메일 가져오기
		String SQL = "SELECT userEmail FROM USER WHERE userID = ?";
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		try {
			conn = DatabaseUtil.getConnection();
			pstmt = conn.prepareStatement(SQL);
			pstmt.setString(1, userID);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				return rs.getString(1);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {if(conn != null) conn.close();} catch (Exception e) {e.printStackTrace();}
			try {if(pstmt != null) pstmt.close();} catch (Exception e) {e.printStackTrace();}
			try {if(rs != null) rs.close();} catch (Exception e) {e.printStackTrace();}
		}
		return null;
	}
	public boolean setUserEmailChecked(String userID) {	// 이메일 인증 완료되도록.
		String SQL = "UPDATE USER SET userEmailChecked = true WHERE userID = ?";
		Connection conn = null;		// update로 체크를 true로 바꿔줌
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		try {
			conn = DatabaseUtil.getConnection();
			pstmt = conn.prepareStatement(SQL);
			pstmt.setString(1, userID);
			pstmt.executeUpdate();
			return true;
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {if(conn != null) conn.close();} catch (Exception e) {e.printStackTrace();}
			try {if(pstmt != null) pstmt.close();} catch (Exception e) {e.printStackTrace();}
			try {if(rs != null) rs.close();} catch (Exception e) {e.printStackTrace();}
		}
		return false; // 데이터베이스 오류 회원가입 실패
	}

}

```

> user 테이블 데이터 모델링 페이지.