#include<iostream>

int main()
{
	using namespace std;

	int total = 0;
	for (int i = 2; i <= 100; i += 2)
	{
		total = total + i;
	}
	cout << "1부터 100까지의 짝수의 합은 " << total << "입니다." << endl;
	return 0;
}