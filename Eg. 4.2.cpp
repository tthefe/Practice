#include <iostream>

int main()
{
	using namespace std;
	const int ArSize = 20;   //const==������ ����� ������ �� ���, ���α׷� �߰��� ArSize�� �ٸ� ���� ���ԵǸ� ���� �߻�
                             //#define Arsize 20�� ������ �ǹ�=������ ���� ��ó���⿡ ���ؼ� ���ڷ� ġȯ
	char name[ArSize];
	char dessert[ArSize];

	cout << "Enter your name: " << endl;;
	cin >> name;
	cout << "Enter your favorite dessert: " << endl;
	cin >> dessert;
	cout << "I will serve delicious " << dessert;
	cout << " for you, " << name << "!" << endl;

	return 0;
}