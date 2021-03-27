#include <iostream>

int main()
{
	using namespace std;
	int num;

	cout << "Enter the number(if zero, stop) : ";
	cin >> num;
	while (num != 0) {
		cout << "You entered " << num << endl;
		cout << "Enter the number(if zero, stop) : ";
		cin >> num;
	}

	cout << "The number is " << num << " . So terminate the loop." << endl;
	return 0;
}