#include<iostream>

int main()
{
	using namespace std;
	int i;
	int j;

	cout << "���ϴ� ���� �Է��Ͻÿ�: ";
	cin >> i;
	for (j = 1; j <= 9; j = j + 1) {
		cout << i << " * " << j << " = " << i * j << endl;
	}

	return 0;
}