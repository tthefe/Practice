#include <iostream>

int main()   //main�Լ��� {���� }����
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

	//��� ������ i�̱� ����

	cout << "1���� 10������ ���� " << total << endl;
	return 0;
}