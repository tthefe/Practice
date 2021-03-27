#include<iostream>
int main()
{
	using namespace std;
	char ch;

	cout << "원하는 문자 하나를 입력하시오: " << endl;
	cin >> ch;

	cout << "당신이 입력한 문자는 " << ch << "입니다."<<endl;
	cout << "당신이 입력한 문자의 ASCII 코드 값은 " << (int)ch << " 입니다." << endl;

	cout << 'A' << '\t' << (int)'A' << endl;
	cout << 'A' + 1 << '\t' << (char)('A' + 1) << endl;

	return 0;
}

