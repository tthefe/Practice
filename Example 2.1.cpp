#include <iostream>

int main()
{
	using namespace std;

	int n = SHRT_MAX;
	cout << n << endl;
	
	//sizeof(): 자료형의 크기를 바이트 단위로 표시
	cout << "Size of short: " << sizeof(char) << "byte" << "\n\n";

	//변수 초기화 방법
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