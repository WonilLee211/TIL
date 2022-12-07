package ch11_logger;

@SuppressWarnings("serial")
public class StudentNameFormatException extends IllegalArgumentException{
	public StudentNameFormatException(String message) {
		super(message);
	}
}
