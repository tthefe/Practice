#include <iostream>

int main()
{
	using namespace std;
	int num1;
	int num2;

	cout << "ù ��° ���ڸ� �Է��ϼ���: ";
	cin >> num1;
	cout << "�� ��° ���ڸ� �Է��ϼ���: ";
	cin >> num2;

	/*int num1, num2;
	cout << "�ΰ��� ���ڸ� �Է��ϼ���: ";
	cin >> num1 >> num2;*/


	if (num1 >= num2) {
		cout << "�ִ��� " << num1 << "�Դϴ�.";
	}
	else if{
		cout << "�ִ��� " << num2 << "�Դϴ�.";
	}
	else {
		cout << "equal number" << endl;
	}

	return 0;
}