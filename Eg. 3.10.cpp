#include <iostream>

int main()
{
	using namespace std;
	int total = 0;
	int i;
	int j;

	for (i = 1; i <= 10; i++) {
	    if (i % 3 == 0) {
			break;
		}
	    total += i;
		for (j = 1; j <= 10; j++) {
			cout << "When j is " << j << endl;
		}
	}

	cout << "When i= " << i << ", escape the loop" << endl;
	cout << " total: " << total << endl;

	return 0;
}