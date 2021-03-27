#include<iostream>

int main()
{
	using namespace std;
	int a, b;
	int max;

	cout << "Enter two numbers: ";
	cin >> a >> b;

	max = (a > b) ? a : b;

	cout << "The maximum number is " << max << endl;

	return 0;
}