#include <iostream>

int main()
{
	using namespace std;
	int total = 0;
	int i;

	for (i = 1; i <= 10; i++) {
		if (i % 2 == 0) {
			continue;
		}
		total += i;
	}

	cout << "When i= " << i << ", escape the loop" << endl;
	cout << "total: " << total << endl;

	return 0;
}