#include <iostream>

int main()
{
	using namespace std;

	for (int i = 2; i <= 9; i++) {
		for (int j = 1; j <= 9; j++) {
			cout << i << " * " << j << " = " << i * j << endl;
		}
	}
	return 0;
}