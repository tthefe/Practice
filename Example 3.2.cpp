#include <iostream>
int main()
{
	using namespace std;

	cout << "�� 5���� �հ�� ����� ���մϴ�." << endl;
	cout << "�� 5���� �Է��Ͻ�����." << endl;

	double number;
	double sum = 0.0;

	for (int i = 1; i <= 5; i++) {
		cout << "��" << i << ":";
		cin >> number;
		sum += number;   //sum=sum+number

		cout << "checking sum"<< sum << endl;   //sumȮ��
	}

	cout << "�� 5���� ��� �ԷµǾ����ϴ�." << endl;
	cout << "�Է��� �� 5���� �հ�� " << sum << "�Դϴ�." << endl;
	cout << "�Է��� �� 5���� ����� " << sum / 5 << "�Դϴ�." << endl;
	cout << "�����մϴ�." << endl;

	return 0;
}