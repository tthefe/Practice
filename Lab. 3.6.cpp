#include <iostream>

int main()
{
	using namespace std;
	int i = 1;
	int total = 0;

	/*for (i = 1; i <= 100; i = i + 2) {
		cout << i << endl;
		sum = sum + i;
	}*/

	while (i <= 100) {
		total += i;
		i = i + 2;
	}

	cout << "1���� 100������ Ȧ���� ���� " << total << endl;
	return 0;
}