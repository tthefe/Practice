#include <iostream>

int main()
{
	using namespace std;
	int total = 1;

	for (int i = 1; i <= 7; i = i + 1) {
		cout<< pow(2,i-1) <<" ";
	}

	return 0;
}