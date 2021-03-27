#include <iostream>

int main()
{
	using namespace std;
	int num;

	cout << "Enter the number: ";
	cin >> num;

	if (num % 2 == 1) {
		cout << num << " is odd number." << endl;
	}
	else {
		cout << num << " is even number." << endl;
	}

	return 0;
}