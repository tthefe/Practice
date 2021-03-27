#include <iostream>

int main()
{
	using namespace std;

	int a = 10, b = 1, c = 10;
	bool tf;
	tf = a > b;
	cout << "a>b=> " << tf << endl;
	tf = a * b < b + c;
	cout << "a * b < b + c=> " << tf << endl;
	tf = a * b == b * c;
	cout << "a * b == b * c=> " << tf << endl;

	return 0;
}