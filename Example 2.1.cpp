#include <iostream>

int main()
{
	using namespace std;

	int n = SHRT_MAX;
	cout << n << endl;
	
	//sizeof(): �ڷ����� ũ�⸦ ����Ʈ ������ ǥ��
	cout << "Size of short: " << sizeof(char) << "byte" << "\n\n";

	//���� �ʱ�ȭ ���
	//short a=0
	//short a(0)
	//shrot a{0}
	short a(0);

	cout << a << endl;

	a = 32767;
	cout << a << endl;

	a = 32768;
	cout << a << endl;

	a = -32768;
	cout << a << endl;

	a = -32769;
	cout << a << endl;
	return 0;

}