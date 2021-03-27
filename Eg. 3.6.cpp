#include <iostream>

int main()
{
	using namespace std;
	int num;

	do {
		cout << "Enter the number(is zero, stop): ";
		cin >> num;
		cout << "You entered " << num << endl;
	} while (num != 0);

	cout << "The number is " << num << ". So terminate the loop." << endl;
	return 0;
}