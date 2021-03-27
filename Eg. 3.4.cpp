#include <iostream>
int main()
{
	using namespace std;
	int i = 1;
	int total = 0;

	while (i <= 10) {
		total = total + i;
		i++;   //i=i+1
	}

	cout << "1부터 10까지의 합은 " << total << endl;

	return 0;
}