#include <iostream>

int main()
{
	using namespace std;

	for (int i = 100; i >= 0; i = i - 5) {
		int j = i * 1.8 + 32;
		cout << "���� " << i << "�� : ȭ�� " << j << "��" << endl;
	}
	return 0;
}