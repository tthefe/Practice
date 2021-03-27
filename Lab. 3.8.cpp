#include <iostream>

int main()
{
	using namespace std;
	int num1;
	int num2;

	cout << "첫 번째 숫자를 입력하세요: ";
	cin >> num1;
	cout << "두 번째 숫자를 입력하세요: ";
	cin >> num2;

	/*int num1, num2;
	cout << "두개의 숫자를 입력하세요: ";
	cin >> num1 >> num2;*/


	if (num1 >= num2) {
		cout << "최댓값은 " << num1 << "입니다.";
	}
	else if{
		cout << "최댓값은 " << num2 << "입니다.";
	}
	else {
		cout << "equal number" << endl;
	}

	return 0;
}