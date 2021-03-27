#include<iostream>

int main()
{
	using namespace std;
	int i;
	int j;

	cout << "원하는 단을 입력하시오: ";
	cin >> i;
	for (j = 1; j <= 9; j = j + 1) {
		cout << i << " * " << j << " = " << i * j << endl;
	}

	return 0;
}