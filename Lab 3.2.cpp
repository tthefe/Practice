#include<iostream>

int main()
{
	using namespace std;

	int total = 0;
	for (int i = 2; i <= 100; i += 2)
	{
		total = total + i;
	}
	cout << "1���� 100������ ¦���� ���� " << total << "�Դϴ�." << endl;
	return 0;
}