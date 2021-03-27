#include <iostream>

int main()   //main함수는 {부터 }까지
{
	using namespace std;
	int i;
	int total = 0;

	for (i = 1; i <= 10; i++) {
		cout << "1st for: " << i << endl;

		for (i = 1; i <= 10; i++) {
			cout << "2nd for: " << i << endl;
			total += i;
		}
	}

	//모든 변수가 i이기 때문

	cout << "1부터 10까지의 합은 " << total << endl;
	return 0;
}