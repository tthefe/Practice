#include <iostream>

int main()
{
	using namespace std;
	int i = 2;
	int total = 0;

	while (i <= 100) {
		total += i;
		i = i + 2;
	}

	cout << "1���� 100������ ¦���� ���� " << total << endl;
	return 0;
}