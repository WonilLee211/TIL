package ch09_exception;

@SuppressWarnings("serial")
public class PasswordException extends IllegalArgumentException{
	
	public PasswordException(String message) {
		super(message);
	}
}
