#include<iostream>
int main()
{
	using namespace std;
	char ch;

	cout << "���ϴ� ���� �ϳ��� �Է��Ͻÿ�: " << endl;
	cin >> ch;

	cout << "����� �Է��� ���ڴ� " << ch << "�Դϴ�."<<endl;
	cout << "����� �Է��� ������ ASCII �ڵ� ���� " << (int)ch << " �Դϴ�." << endl;

	cout << 'A' << '\t' << (int)'A' << endl;
	cout << 'A' + 1 << '\t' << (char)('A' + 1) << endl;

	return 0;
}

