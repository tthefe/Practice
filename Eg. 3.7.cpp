#include <iostream>

int main()
{
	using namespace std;
	int num;

	cout << "Enter the number: ";
	cin >> num;

	if (num < 0) {
		num = -num;
	}

	cout << "The absolute value is " << num << endl;
	return 0;
}