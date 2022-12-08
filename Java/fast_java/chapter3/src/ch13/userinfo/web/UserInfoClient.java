package ch13.userinfo.web;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

import ch13.domain.userinfo.UserInfo;
import ch13.domain.userinfo.dao.UserInfoDao;
import ch13.domain.userinfo.dao.mysql.UserInfoMySqlDao;
import ch13.domain.userinfo.dao.oracle.UserInfoDaoOracle;

public class UserInfoClient {

	public static void main(String[] args) throws IOException {
        // db.properties 파일을 바이트스트림으로 읽기위한 객체 생성
		FileInputStream fis = new FileInputStream("db.properties");
		// [ Properties 클래스 ]

        //     MAP 계열의 컬렉션 프레임워크와 비슷하게 동작하는 파일
        //     "Key = Value" 형태로 된 "파일이름.properties" 파일 또는 Xml 파일
        //     key를 주면 Value를 반환하는 기능을 가짐
        //     DB의 연결정보 등을 저장해두는 용도로 많이 쓰임
		Properties prop = new Properties();
		prop.load(fis);

		// db.properties 파일 안에 DBTYPE 키의 value 가져오기
		String dbType = prop.getProperty("DBTYPE");
		
		UserInfo userInfo = new UserInfo();
		userInfo.setUserId("12345");
		userInfo.setPassword("!@#$%");
		userInfo.setUserName("이순신");
		
		UserInfoDao userInfoDao = null;

		if(dbType.equals("ORACLE")){
			userInfoDao = new UserInfoDaoOracle();
		}
		else if(dbType.equals("MYSQL")){
			userInfoDao = new UserInfoMySqlDao();
		}
		else{
			System.out.println("db support error");
			return;
		}

		userInfoDao.insertUserInfo(userInfo);
		userInfoDao.updateUserInfo(userInfo);
		userInfoDao.deleteUserInfo(userInfo);

	}

}
