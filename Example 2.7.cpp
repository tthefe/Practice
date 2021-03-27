#include<iostream>

int main()

{
	using namespace std;

	int a = 100;

	cout << a << endl;   //100
	cout << a++ << endl;   //100
	cout << a << endl;   //101
	cout << ++a << endl;   //102

	return 0;
}