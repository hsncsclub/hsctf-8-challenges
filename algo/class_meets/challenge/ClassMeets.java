import java.util.Scanner;

public class ClassMeets {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int sMonth = Integer.parseInt(in.next().substring(1));
		int sDay = Integer.parseInt(in.next().substring(1));
		int sDayIndx = sMonth * 30 + sDay;
		int eMonth = Integer.parseInt(in.next().substring(1));
		int eDay = Integer.parseInt(in.next().substring(1));
		int eDayIndx = eMonth * 30 + eDay;
		int inPerson1 = Integer.parseInt(in.next().substring(1));
		int virtual1 = Integer.parseInt(in.next().substring(1));
		int inPerson2 = Integer.parseInt(in.next().substring(1));
		int virtual2 = Integer.parseInt(in.next().substring(1));
		int person1Counter = 0;
		boolean isInPerson1 = true;
		int person2Counter = 0;
		boolean isInPerson2 = true;
		int total = 0;
		for (int i = 0; i <= eDayIndx; i++) {
			if (i >= sDayIndx && isInPerson1 == isInPerson2) {
				total++;
			}
			if (i % 7 != 5 && i % 7 != 6) {
				person1Counter++;
				person2Counter++;
				if (isInPerson1) {
					if (person1Counter >= inPerson1) {
						isInPerson1 = false;
						person1Counter = 0;
					}
				} else {
					if (person1Counter >= virtual1) {
						isInPerson1 = true;
						person1Counter = 0;
					}
				}
				if (isInPerson2) {
					if (person2Counter >= inPerson2) {
						isInPerson2 = false;
						person2Counter = 0;
					}
				} else {
					if (person2Counter >= virtual2) {
						isInPerson2 = true;
						person2Counter = 0;
					}
				}
			}
		}
		System.out.println(total);
		in.close();

	}

}
