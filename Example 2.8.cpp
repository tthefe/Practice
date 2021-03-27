#include<iostream>

int main()
{
	using namespace std;
	int a, b = 2;

	a = 10; a += b; cout << "a= "<<a << endl;
	a = 10; a -= b; cout << "a= "<<a << endl;
	a = 10; a *= b; cout << "a= " << a << endl;
	a = 10; a /= b; cout << "a= " << a << endl;
	a = 10; a %= b; cout << "a= " << a << endl;

	return 0;
}